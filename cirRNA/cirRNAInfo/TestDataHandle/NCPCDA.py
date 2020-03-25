import numpy as np
import pymysql
import math
from sklearn.metrics import roc_curve, auc

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
def getCircRNACancerAssociation(cancerNum, circRNANum, circRNACancerData) :
    resultMatrix = np.zeros((cancerNum, circRNANum), dtype=np.float)
    for i in range(0, circRNACancerData.__len__()):
        circRNAIndex = int(circRNACancerData[i][0])
        cancerIndex = int(circRNACancerData[i][1])
        resultMatrix[cancerIndex - 1][circRNAIndex - 1] = 1

    return resultMatrix.T

# circRNA与circRNA的相似性矩阵
def CS(AMatrix, circRNANum, cancerNum) :

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

# Cancer与Cancer的相似性矩阵
def DS(AMatrix, circRNANum, cancerNum) :
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

def CSP(circRNANum,cancerNum,CSMatrix,AMatrix):
    resultMatrix = np.zeros((circRNANum,cancerNum),dtype=float)
    for i in range(circRNANum):
        for j in range(cancerNum):
            if(np.sum(AMatrix[:,j])==0):
                resultMatrix[i][j] = np.matmul(CSMatrix[i:i+1,:],AMatrix[:,j:j+1])
            else:
                resultMatrix[i][j] = np.matmul(CSMatrix[i:i+1,:],AMatrix[:,j:j+1])/np.sum(AMatrix[:,j])
    return resultMatrix
def DSP(circRNANum,cancerNum,DSMatrix,AMatrix):
    resultMatrix = np.zeros((circRNANum, cancerNum), dtype=float)
    for i in range(circRNANum):
        for j in range(cancerNum):
            if(np.sum(AMatrix[i,:])==0):
                resultMatrix[i][j] = np.matmul(AMatrix[i:i + 1, :], DSMatrix[:, j:j + 1])
            else:
                resultMatrix[i][j] = np.matmul(AMatrix[i:i+1,:],DSMatrix[:,j:j+1])/np.sum(AMatrix[i,:])
    return resultMatrix

def trainMatrix(cancerNum,circRNANum,circRNACancerData):
    AMatrix = getCircRNACancerAssociation(cancerNum,circRNANum,circRNACancerData)
    CSMatrix = CS(AMatrix,circRNANum,cancerNum)
    DSMatrix = DS(AMatrix.T,circRNANum,cancerNum)
    CSPMatrix = CSP(circRNANum,cancerNum,CSMatrix,AMatrix)
    DSPMatrix = DSP(circRNANum,cancerNum,DSMatrix,AMatrix)
    resultMatrix = np.zeros((circRNANum,cancerNum))
    for i in range(circRNANum):
        for j in range(cancerNum):
            resultMatrix[i][j] = (CSPMatrix[i][j] + DSPMatrix[i][j])/(np.sum(CSPMatrix[i,:])+np.sum(DSMatrix[:,j]))
    return resultMatrix

def predictCircRNAToCancer(cancerNum,circRNANum,circRNACancerData,circRNAName):
    circRNAId = 0
    resultMatrix = trainMatrix(cancerNum,circRNANum,circRNACancerData)
    for i in range(0,circRNANum):
        if(circRNAData[i][1] == circRNAName):
            circRNAId = int(circRNAData[i][0])
            break
    if (circRNAId == 0):
        return None
    resultList = []
    for i in range(cancerNum):
        resultList.append((cancerData[i][1],np.around(resultMatrix[circRNAId-1][i],decimals=7)))
    resultList.sort(key=lambda x: x[1], reverse=True)
    return resultList



def predictCancerToCircRNA(cancerNum,circRNANum,circRNACancerData,cancerName):
    cancerId = 0
    resultMatrix = trainMatrix(cancerNum, circRNANum, circRNACancerData).T
    AMatrix = getCircRNACancerAssociation(cancerNum,circRNANum,circRNACancerData).T
    for i in range(cancerNum):
        if (cancerData[i][1] == cancerName):
            cancerId = int(circRNACancerData[i][0])
            break
    if (cancerId == 0):
        return None
    trainList = resultMatrix[cancerId - 1]
    testList = AMatrix[cancerId - 1]

    resultList = []
    for i in range(circRNANum):
        resultList.append((circRNAData[i][1], np.around(resultMatrix[cancerId - 1][i], decimals=7)))
    resultList.sort(key=lambda x: x[1], reverse=True)
    return resultList
if __name__ == "__main__":
    # resultList1 = predictCancerToCircRNA(cancerNum,circRNANum,circRNACancerData,'breast cancer')
    # resultList2 = predictCircRNAToCancer(cancerNum,circRNANum,circRNACancerData,'circ-Amotl1')
    # print(resultList1)
    # print(resultList2)
    train_Matrix = trainMatrix(cancerNum,circRNANum,circRNACancerData)[0]
    AMatrix = getCircRNACancerAssociation(cancerNum,circRNANum,circRNACancerData)[0]
    fpr,tpr,thresholds = roc_curve(AMatrix,train_Matrix)
    print(thresholds)