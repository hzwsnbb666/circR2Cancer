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
def getCircRNACancerAssociation(cancerNum: int, circRNANum: int, circRNACancerData: tuple) -> np.ndarray:
    resultMatrix = np.zeros((cancerNum, circRNANum), dtype=np.float)
    for i in range(0, circRNACancerData.__len__()):
        circRNAIndex = int(circRNACancerData[i][0])
        cancerIndex = int(circRNACancerData[i][1])
        resultMatrix[cancerIndex - 1][circRNAIndex - 1] = 1

    return resultMatrix.T


def KC(AMatrix: np.ndarray, circRNANum: int, cancerNum: int) -> np.ndarray:
    IP: np.ndarray
    IP_2: float = 0.0
    IPi_2: float = 0.0
    Nc: float = circRNANum
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
def KD(AMatrix: np.ndarray, circRNANum: int, cancerNum: int) -> np.ndarray:
    IP: np.ndarray
    IP_2: float = 0.0
    IPi_2: float = 0.0
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

def SC(KCMatrix: np.ndarray, circRNANum: int) -> np.ndarray:
    resultMatrix = np.zeros((circRNANum, circRNANum), dtype=float)
    for i in range(circRNANum):
        for j in range(circRNANum):
            resultMatrix[i][j] = 1.0 / (1.0 + np.exp(-15 * KCMatrix[i][j] + np.log(9999)))
    # print(resultMatrix)
    return resultMatrix

def SD(KDMatrix: np.ndarray, cancerNum: int) -> np.ndarray:
    resultMatrix = np.zeros((cancerNum, cancerNum), dtype=float)
    for i in range(cancerNum):
        for j in range(cancerNum):
            resultMatrix[i][j] = 1.0 / (1.0 + np.exp(-15 * KDMatrix[i][j] + np.log(9999)))
    return resultMatrix

def LC(SCMatrix: np.ndarray,circRNANum:int) -> np.ndarray:
    DCMatrix = np.zeros((circRNANum,circRNANum),dtype=float)
    for i in range(circRNANum):
        DCMatrix[i][i] = np.sum(SCMatrix[i])

    v , Q = np.linalg.eig(DCMatrix)
    V = np.diag(v**(-0.5))
    DCMatrix_1_2 = Q*V*np.linalg.inv(Q)



    resultMatrix = np.matmul(np.matmul(DCMatrix_1_2,DCMatrix-SCMatrix),DCMatrix_1_2)
    return resultMatrix

def LD(SDMatrix: np.ndarray,cancerNum:int) -> np.ndarray:
    DDMatrix = np.zeros((cancerNum,cancerNum),dtype=float)
    for i in range(cancerNum):
        DDMatrix[i][i] = np.sum(SDMatrix[i])
    v , Q = np.linalg.eig(DDMatrix)
    V = np.diag(v**(-0.5))
    DDMatrix_1_2 = np.matmul(np.matmul(Q,V),np.linalg.inv(Q))



    resultMatrix = np.matmul(np.matmul(DDMatrix_1_2,DDMatrix-SDMatrix),DDMatrix_1_2)
    return resultMatrix

def FC(SCMatrix:np.ndarray,LCMatrix:np.ndarray,AMatrix:np.ndarray)->np.ndarray:
    resultMatrix = np.matmul(np.matmul(SCMatrix,SCMatrix+np.matmul(LCMatrix,SCMatrix)),AMatrix)
    return resultMatrix

def FD(SDMatrix:np.ndarray,LDMatrix:np.ndarray,AMatrix:np.ndarray)->np.ndarray:
    resultMatrix = np.matmul(np.matmul(SDMatrix,SDMatrix+np.matmul(LDMatrix,SDMatrix)),AMatrix.T)
    return resultMatrix
def trainMatrix(cancerNum:int,circRNANum:int,circRNACancerData:tuple,parameter:float)->np.ndarray:
    AMatrix = getCircRNACancerAssociation(cancerNum, circRNANum, circRNACancerData)
    KCMatrix = KC(AMatrix, circRNANum, cancerNum)
    SCMatrix = SC(KCMatrix, circRNANum)


    KDMatrix = KD(AMatrix.T, circRNANum, cancerNum)
    SDMatrix = SD(KDMatrix, cancerNum)

    LCMatrix = LC(SCMatrix, circRNANum)

    LDMatrix = LD(SDMatrix, cancerNum)

    FCMatrix = FC(SCMatrix, LCMatrix, AMatrix)

    FDMatrix = FD(SDMatrix, LDMatrix, AMatrix)

    resultMatrix = parameter*FCMatrix+(1-parameter)*FDMatrix.T
    return  resultMatrix
def predictCircRNAToCancer(cancerNum:int,circRNANum:int,circRNACancerData:tuple,parameter:float,circRNAName:str):
    circRNAId = 0
    resultMatrix = trainMatrix(cancerNum,circRNANum,circRNACancerData,parameter)
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



def predictCancerToCircRNA(cancerNum:int,circRNANum:int,circRNACancerData:tuple,parameter:float,cancerName:str):
    cancerId = 0
    resultMatrix = trainMatrix(cancerNum, circRNANum, circRNACancerData, parameter).T
    for i in range(cancerNum):
        if (cancerData[i][1] == cancerName):
            cancerId = int(circRNACancerData[i][0])
            break
    if (cancerId == 0):
        return None
    resultList = []
    for i in range(circRNANum):
        resultList.append((circRNAData[i][1], np.around(resultMatrix[cancerId - 1][i], decimals=7)))
    resultList.sort(key=lambda x: x[1], reverse=True)
    return resultList

if __name__ == "__main__":
    resultList1 = predictCancerToCircRNA(cancerNum,circRNANum,circRNACancerData,0.2,'breast cancer')
    resultList2 = predictCircRNAToCancer(cancerNum,circRNANum,circRNACancerData,0.2,'circ-Amotl1')
    print(resultList1)
    print(resultList2)


