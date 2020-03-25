import numpy as np
import pymysql
import math
import tenFolds as tf
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

# 获取Human circRNA–Disease Associations矩阵
def getCircRNACancerAssociation(cancerNum,circRNANum,circRNACancerData) :
    resultMatrix = np.zeros((cancerNum, circRNANum), dtype=np.int)
    for i in range(0, circRNACancerData.__len__()):
        circRNAIndex = int(circRNACancerData[i][0])

        cancerIndex = int(circRNACancerData[i][1])
        resultMatrix[cancerIndex - 1][circRNAIndex - 1] = 1

    return resultMatrix


# Gaussian interaction profile kernel similarity for circRNAs
def CC(AMatrix,circRNANum,cancerNum) :
    IP_2 = 0.0
    IPi_2 = 0.0
    ym_ = circRNANum
    CCMatrix = np.zeros((circRNANum, circRNANum), dtype=np.float)
    for i in range(circRNANum):
        for j in range(cancerNum):
            if(AMatrix[i][j]==1):
                IPi_2 += pow(AMatrix[i][j],2)
    for i in range(circRNANum):
        for j in range(circRNANum):
            IP = AMatrix[i] - AMatrix[j]
            for k in range(cancerNum):
                IP_2 += math.pow(IP[k], 2)
            CCMatrix[i][j] = math.exp(- ym_ / IPi_2 * IP_2)
            IP_2 = 0.0
    return np.around(CCMatrix, decimals=7)


def DD(AMatrix,circRNANum,cancerNum) :
    IP_2 = 0.0
    IPi_2 = 0.0
    yd_ = cancerNum
    DDMatrix = np.zeros((cancerNum, cancerNum), dtype=np.float)

    for i in range(cancerNum):
        for j in range(circRNANum):
            if(AMatrix[i][j]==1.0):
                IPi_2 += pow(AMatrix[i][j],2)
    for i in range(cancerNum):
        for j in range(cancerNum):
            IP = AMatrix[i] - AMatrix[j]
            for k in range(circRNANum):
                IP_2 += math.pow(IP[k], 2)
            DDMatrix[i][j] = math.exp(- yd_ / IPi_2 * IP_2)
            IP_2 = 0.0
    return np.around(DDMatrix, decimals=7)


def WDD(AMatrix, DMatrix,cancerNum,parameter = 0.5) :
    WDDMatrix = np.zeros((cancerNum, cancerNum), dtype=np.float)
    Asum = 0
    Dsum = 0
    for i in range(cancerNum):
        Asum = np.sum(AMatrix[i])
        Dsum = np.sum(DMatrix[i])
        for j in range(cancerNum):
            if (Asum == 0):
                WDDMatrix[i][j] = DMatrix[i][j] / Dsum
            else:
                WDDMatrix[i][j] = (1 - parameter) * DMatrix[i][j] / Dsum
    return np.around(WDDMatrix, decimals=7)


def WCC(AMatrix, CMatrix, circRNANum,parameter = 0.5) :
    WCCMatrix = np.zeros((circRNANum, circRNANum), dtype=np.float)
    Asum = 0
    Csum = 0
    for i in range(circRNANum):
        Asum = np.sum(AMatrix[i])
        Csum = np.sum(CMatrix[i])
        for j in range(circRNANum):
            if (Asum == 0):
                WCCMatrix[i][j] = CMatrix[i][j] / Csum
            else:
                WCCMatrix[i][j] = (1 - parameter) * CMatrix[i][j] / Csum
    return np.around(WCCMatrix, decimals=7)


def WTD(AMatrix,circRNANum,cancerNum, parameter = 0.5) :
    WTDMatrix = np.zeros((cancerNum, circRNANum), np.float)
    Asum = 0
    for i in range(cancerNum):
        Asum = np.sum(AMatrix[i])
        for j in range(circRNANum):
            if (Asum == 0):
                WTDMatrix[i][j] = 0
            else:
                WTDMatrix[i][j] = parameter * AMatrix[i][j] / Asum
    return np.around(WTDMatrix, decimals=7)



def WTC(AMatrix, circRNANum,cancerNum,parameter = 0.5) :
    WTCMatrix = np.zeros((circRNANum, cancerNum), np.float)
    Asum = 0
    for i in range(circRNANum):
        Asum = np.sum(AMatrix[i])
        for j in range(cancerNum):
            if (Asum == 0):
                WTCMatrix[i][j] = 0
            else:
                WTCMatrix[i][j] = parameter * AMatrix[i][j] / Asum

    return np.around(WTCMatrix, decimals=7)




def trainMatrix(circRNANum,cancerNum,circRNACancerData,parameter1,parameter2,r):
    AMatrix = getCircRNACancerAssociation(cancerNum, circRNANum, circRNACancerData)
    CMatrix = CC(AMatrix.T, circRNANum, cancerNum)
    DMatrix = DD(AMatrix, circRNANum, cancerNum)

    WDDMatrix = WDD(AMatrix, DMatrix, cancerNum, parameter1)
    WTDMatrix = WTD(AMatrix, circRNANum, cancerNum, parameter1)

    WTCMatrix = WTC(AMatrix.T, circRNANum, cancerNum, parameter2)
    WCCMatrix = WCC(AMatrix.T, CMatrix, circRNANum, parameter2)

    WMatrix = np.vstack((np.hstack((WDDMatrix, WTDMatrix)), np.hstack((WTCMatrix, WCCMatrix))))
    p0Matrix = np.zeros((circRNANum+cancerNum,cancerNum),dtype=float)
    for i in range(cancerNum):
        itemCircRNANum = np.sum(AMatrix[i])
        for j in range(circRNANum):
            if(AMatrix[i][j] == 1):
                p0Matrix[cancerNum+j][i] = 1.0 / itemCircRNANum
    t = 1
    pt = p0Matrix
    circRNACancerNum = circRNANum*cancerNum
    # 接下来开始随机游走，需要注意的是这里结束标志为p(t+1)和p(t)的差值的平均值小于10^-6
    while(True):
        ptAdd1 = p(WMatrix,t,r,p0Matrix)
        Delta = abs(ptAdd1 - pt)
        if(np.sum(Delta) / circRNACancerNum < 1e-6):
            break
        pt = ptAdd1
        t += 1
    return ptAdd1[cancerNum: ,:]




def p(WMatrix,t,r,p0):
    if (t == 0 ):
        return p0
    else:
        return (1-r) * np.matmul(WMatrix,p(WMatrix,t-1,r,p0)) + r*p0


def predictCancerToCircRNA(circRNANum,cancerNum,circRNACancerData,parameter1,parameter2,r,cancerName):
    cancerId = 0
    for i in range(0,cancerNum):
        if(cancerData[i][1] == cancerName):
            cancerId = int(cancerData[i][0])
            break
    if (cancerId == 0):
        return None

    resultMatrix, ROC_AUC, Mean_TPR, Mean_FPR = tf.AnalyseAlgrithom('RWR')
    resultList = []

    for i in range(circRNANum):
        resultList.append((circRNAData[i][1], np.around(resultMatrix[i][cancerId - 1], decimals=7)))
    resultList.sort(key=lambda x: x[1], reverse=True)
    return resultList

#预测指定circRNA的Cancer
def predictCircRNAToCancer(circRNANum,cancerNum,circRNACancerData,parameter1,parameter2,r,circRNAName):
    circRNAId = 0
    for i in range(0,circRNANum):
        if(circRNAData[i][1] == circRNAName):
            circRNAId = int(circRNAData[i][0])
            break
    if (circRNAId == 0):
        return None
    resultMatrix = trainMatrix(circRNANum, cancerNum, circRNACancerData, parameter1, parameter2, r)
    resultList = []
    for i in range(cancerNum):
        resultList.append((cancerData[i][1], np.around(resultMatrix[circRNAId - 1][i], decimals=7)))
    resultList.sort(key=lambda x: x[1], reverse=True)
    return resultList


#由于做算法对比时，circRNA和Cancer的ID是从0开始的，因此需要重写一个类似的getCircRNACancerAssociation2方法
def getCircRNACancerAssociation2(cancerNum,circRNANum,circRNACancerData) :
    resultMatrix = np.zeros((cancerNum, circRNANum), dtype=np.int)
    for i in range(0, circRNACancerData.__len__()):
        circRNAIndex = int(circRNACancerData[i][0])

        cancerIndex = int(circRNACancerData[i][1])
        resultMatrix[cancerIndex][circRNAIndex] = 1

    return resultMatrix



if __name__ == '__main__':
    resultList1 = predictCancerToCircRNA(circRNANum,cancerNum,circRNACancerData,0.5,0.5,0.5,'breast cancer')
    resultList2 = predictCircRNAToCancer(circRNANum,cancerNum,circRNACancerData,0.5,0.5,0.5,'circ-Amotl1')

    print(resultList1)
    print(resultList2)