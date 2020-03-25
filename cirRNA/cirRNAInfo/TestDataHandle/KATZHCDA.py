import numpy as np
import pymysql
import math

# 让ndarray输出时不使用省略号
np.set_printoptions(threshold=np.inf, suppress=True)

# 连接数据库
db = pymysql.connect("localhost", "root", "123456", "cirrna")  # 连接数据库
cursor = db.cursor()

# 查询circRNA-Cancer
allCircRNACancerSQL = "select b.id circRNA_id,c.id cancer_id,b.circRNA,c.disease from cirrnainfo_circrna_cancer_test a left join cirrnainfo_cancer_info_test c on a.disease = c.disease left join cirrnainfo_circrna_info_test b on a.circRNA = b.circRNA;"
cursor.execute(allCircRNACancerSQL)
circRNACancerData = cursor.fetchall()

# 查询circRNA_info
allCircRNASQL = "select * from cirrnainfo_circrna_info_test;"
cursor.execute(allCircRNASQL)
circRNAData = cursor.fetchall()
circRNANum = circRNAData.__len__()

# 查询cancer_info
allCancerSQL = "select * from cirrnainfo_cancer_info_test;"
cursor.execute(allCancerSQL)
cancerData = cursor.fetchall()
cancerNum = cancerData.__len__()


# 获取Human circRNA–Disease Associations矩阵(circRNA i为第i行，Cancer j为第j列）
def getCircRNACancerAssociation(cancerNum, circRNANum, circRNACancerData):
    resultMatrix = np.zeros((cancerNum, circRNANum), dtype=np.float)
    for i in range(0, circRNACancerData.__len__()):
        circRNAIndex = int(circRNACancerData[i][0])
        cancerIndex = int(circRNACancerData[i][1])
        resultMatrix[cancerIndex - 1][circRNAIndex - 1] = 1

    return resultMatrix.T


def SC(AMatrix, circRNANum, cancerNum):
    IP_2 = 0.0
    IPi_2 = 0.0
    Nc = circRNANum
    CCMatrix = np.zeros((circRNANum, circRNANum), dtype=np.float)
    for i in range(circRNANum):
        for j in range(cancerNum):
            if (AMatrix[i][j] == 1.0):
                IPi_2 += pow(AMatrix[i][j], 2)
    for i in range(circRNANum):
        for j in range(circRNANum):
            IP = AMatrix[i] - AMatrix[j]

            for k in range(cancerNum):
                IP_2 += math.pow(IP[k], 2)

            CCMatrix[i][j] = math.exp(- Nc / IPi_2 * IP_2)
            IP_2 = 0.0
    return CCMatrix





# 这里的相似性矩阵传参时应该传入它的转置
def SD(AMatrix, circRNANum, cancerNum) :
    IP_2 = 0.0
    IPi_2 = 0.0
    Nd = cancerNum
    DDMatrix = np.zeros((cancerNum, cancerNum), dtype=np.float)
    for i in range(cancerNum):
        for j in range(circRNANum):
            if (AMatrix[i][j] == 1.0):
                IPi_2 += pow(AMatrix[i][j], 2)
    for i in range(cancerNum):
        for j in range(cancerNum):
            IP = AMatrix[i] - AMatrix[j]
            for k in range(circRNANum):
                IP_2 += math.pow(IP[k], 2)
            DDMatrix[i][j] = math.exp(- Nd / IPi_2 * IP_2)
            IP_2 = 0.0
    return DDMatrix


def A_(SCMatrix,SDMatrix,AMatrix):
    resultMatrix = np.vstack((np.hstack((SCMatrix, AMatrix)), np.hstack((AMatrix.T, SDMatrix))))
    return resultMatrix
def S(A_Matrix,circRNANum,cancerNum,y_=0.1):
    # IMatrix = np.zeros((circRNANum+cancerNum,circRNANum+cancerNum),dtype=float)
    # for i in range(circRNANum+cancerNum):
    #     IMatrix[i][i] = 1.0
    #
    # resultMatrix = np.linalg.inv(IMatrix - y_ * A_Matrix) - IMatrix
    # return resultMatrix
    resultMatrix = y_*A_Matrix+pow(y_,2)*np.matmul(A_Matrix,A_Matrix)
    return resultMatrix

def predictCircRNAToCancer(cancerNum,circRNANum,circRNACancerData,circRNAName):
    AMatrix = getCircRNACancerAssociation(cancerNum, circRNANum, circRNACancerData)
    SCMatrix = SC(AMatrix, circRNANum, cancerNum)
    SDMatrix = SD(AMatrix.T, circRNANum, cancerNum)

    A_Matrix = A_(SCMatrix, SDMatrix, AMatrix)
    SMatrix = S(A_Matrix, circRNANum, cancerNum)
    circRNAId = 0
    for i in range(0,circRNANum):
        if(circRNAData[i][1] == circRNAName):
            circRNAId = int(circRNAData[i][0])
            break
    if (circRNAId == 0):
        return None
    resultList = []
    for i in range(cancerNum):
        resultList.append((cancerData[i][1], np.around(SMatrix[circRNAId - 1][circRNANum+i], decimals=9)))
    resultList.sort(key=lambda x:x[1],reverse=True)
    return resultList
def predictCancerToCircRNA(cancerNum,circRNANum,circRNACancerData,cancerName):
    AMatrix = getCircRNACancerAssociation(cancerNum, circRNANum, circRNACancerData)
    SCMatrix = SC(AMatrix, circRNANum, cancerNum)
    SDMatrix = SD(AMatrix.T, circRNANum, cancerNum)
    A_Matrix = A_(SCMatrix, SDMatrix, AMatrix)
    SMatrix = S(A_Matrix, circRNANum, cancerNum)
    cancerId = 0
    for i in range(0,cancerNum):
        if(cancerData[i][1] == cancerName):
            cancerId = int(cancerData[i][0])
            break
    if (cancerId == 0):
        return None
    resultList = []
    for i in range(circRNANum):
        resultList.append((circRNAData[i][1], np.around(SMatrix[i][cancerId - 1+circRNANum], decimals=9)))
    resultList.sort(key=lambda x:x[1],reverse=True)
    return resultList
def trainMatrix(cancerNum,circRNANum,circRNACancerData):
    AMatrix = getCircRNACancerAssociation(cancerNum, circRNANum, circRNACancerData)
    SCMatrix = SC(AMatrix, circRNANum, cancerNum)
    SDMatrix = SD(AMatrix.T, circRNANum, cancerNum)
    A_Matrix = A_(SCMatrix, SDMatrix, AMatrix)
    SMatrix = S(A_Matrix, circRNANum, cancerNum)
    return  SMatrix


if __name__ == "__main__":
    resultList1 = predictCancerToCircRNA(cancerNum, circRNANum, circRNACancerData, 'breast cancer')
    resultList2 = predictCircRNAToCancer(cancerNum, circRNANum, circRNACancerData, 'circ-Amotl1')
    print(resultList1)
    print(resultList2)