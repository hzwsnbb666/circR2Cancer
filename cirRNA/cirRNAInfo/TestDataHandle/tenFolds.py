import KATZHCDA as kz
import random
import matplotlib.pyplot as plt
import LeastSquare as ls
import RWR as rwr
import numpy as np
import testData as td
import NCPCDA as ncp
def AnalyseAlgrithom(methodName:str):
    circRNACancerData = list(td.circRNACancerData)
    random.shuffle(circRNACancerData)
    circRNACancerData = tuple(circRNACancerData)

    AMatrix = td.getCircRNACancerAssociation(td.cancerNum, td.circRNANum, circRNACancerData).T

    All_Sample_List = []
    One_Sample_List = []
    Zero_Sample_List = []
    for i in range(AMatrix.__len__()):
        for j in range(AMatrix[0].__len__()):
            All_Sample_List.append((i + 1, j + 1, AMatrix[i][j]))
    random.shuffle(All_Sample_List)
    for item in All_Sample_List:
        if (item[2] == 1):
            One_Sample_List.append(item)
        else:
            Zero_Sample_List.append(item)
    folds = 10
    one_split = int(One_Sample_List.__len__() / folds)
    zero_split = int(Zero_Sample_List.__len__() / folds)
    # 存放所有的TPR和所有的FPR
    All_TPR_List = []
    All_FPR_List = []

    for k in range(1, folds + 1):
        trainZeroList = Zero_Sample_List[:(k - 1) * zero_split] + Zero_Sample_List[k * zero_split:folds * zero_split]
        trainOneList = One_Sample_List[:(k - 1) * one_split] + One_Sample_List[k * one_split:folds * one_split]
        testZeroList = Zero_Sample_List[(k - 1) * zero_split:k * zero_split]
        testOneList = One_Sample_List[(k - 1) * one_split:k * one_split]

        # trainList = circRNACancerData[:(k-1)*split] + circRNACancerData[k*split:]
        # testList = circRNACancerData[(k-1)*split:k*split]
        ###依次计算出训练集的测试结果和测试集的相似性举证
        testAllList = testZeroList + testOneList
        if(methodName == 'Random Walk with Restart'):
            trainAllMatrix = rwr.trainMatrix(td.circRNANum, td.cancerNum, tuple(trainOneList), 0.7, 0.7, 0.5)
        elif(methodName == 'Least Square'):
            trainAllMatrix = ls.trainMatrix(td.cancerNum,td.circRNANum,tuple(trainOneList),0.5)
        elif(methodName == 'KATZHCDA'):
            trainAllMatrix = kz.trainMatrix(td.cancerNum,td.circRNANum,tuple(trainOneList))
        elif(methodName == 'NCPCDA'):
            trainAllMatrix = ncp.trainMatrix(td.cancerNum,td.circRNANum,tuple(trainOneList))
        else:
            trainAllMatrix = None
            return None

        TPRList = []
        FPRList = []
        ThresholdList =[] #存放阈值
        # 对每个阈值下的TP,FP,FN,TN进行计算
        # 依次设置阈值
        for tempItem in testAllList:
            ThresholdList.append(trainAllMatrix[tempItem[0] - 1, tempItem[1] - 1])
        ThresholdList.sort()
        for t in range(ThresholdList.__len__()):
            TP = 0
            FP = 0
            FN = 0
            TN = 0
            Threshold = ThresholdList[t]
            for item2 in testAllList:
                if (item2[2] == 1 and trainAllMatrix[item2[0] - 1, item2[1] - 1] >= Threshold):
                    TP += 1
                elif (item2[2] == 0 and trainAllMatrix[item2[0] - 1, item2[1] - 1] >= Threshold):
                    FP += 1
                elif (item2[2] == 1 and trainAllMatrix[item2[0] - 1, item2[1] - 1] < Threshold):
                    FN += 1
                else:
                    TN += 1
            TPR = TP / (TP + FN)
            FPR = FP / (TN + FP)
            TPRList.append(TPR)
            FPRList.append(FPR)
        All_TPR_List.append(TPRList)
        All_FPR_List.append(FPRList)
    #平均TPR，FPR，先将每次TPR和FPR排序，然后依次按列取平均值，得到Mean_TPR,Mean_FPR,ROC_AUC
    Mean_TPR = np.mean(np.array(All_TPR_List), axis=0)
    Mean_FPR = np.mean(np.array(All_FPR_List), axis=0)

    ROC_AUC = np.trapz(Mean_TPR, Mean_FPR)

    return ROC_AUC,Mean_TPR,Mean_FPR

def drawAllConfigure(ROC_AUC_List:list,Mean_TPR_List:list,Mean_FPR_List:list):
    x_major_locator = plt.MultipleLocator(0.1)

    # 把x轴的刻度间隔设置为0.1，并存在变量里

    y_major_locator = plt.MultipleLocator(0.1)

    # 把y轴的刻度间隔设置为0.1，并存在变量里

    ax = plt.gca()

    # ax为两条坐标轴的实例

    ax.xaxis.set_major_locator(x_major_locator)

    # 把x轴的主刻度设置为0.1的倍数

    ax.yaxis.set_major_locator(y_major_locator)

    # 把y轴的主刻度设置为0.1的倍数

    plt.xlim(0.0, 1.0)

    plt.ylim(0.0, 1.0)

    plt.plot(Mean_FPR_List[0], Mean_TPR_List[0], 'g', label='RWR ROC=%0.4f' % ROC_AUC_List[0])
    plt.plot(Mean_FPR_List[1], Mean_TPR_List[1], 'r', label='Least Square ROC=%0.4f' % ROC_AUC_List[1])
    plt.plot(Mean_FPR_List[2], Mean_TPR_List[2], 'b', label='KATZHCDA ROC=%0.4f' % ROC_AUC_List[2])
    plt.plot(Mean_FPR_List[3], Mean_TPR_List[3], 'y', label='NCPCDA ROC=%0.4f' % ROC_AUC_List[3])

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc=0)
    plt.show()
def drawConfigure(ROC_AUC:float,TPR:np.ndarray,FPR:np.ndarray):
    x_major_locator = plt.MultipleLocator(0.1)

    # 把x轴的刻度间隔设置为0.1，并存在变量里

    y_major_locator = plt.MultipleLocator(0.1)

    # 把y轴的刻度间隔设置为0.1，并存在变量里

    ax = plt.gca()

    # ax为两条坐标轴的实例

    ax.xaxis.set_major_locator(x_major_locator)

    # 把x轴的主刻度设置为0.1的倍数

    ax.yaxis.set_major_locator(y_major_locator)

    # 把y轴的主刻度设置为0.1的倍数

    plt.xlim(0.0, 1.0)

    plt.ylim(0.0, 1.0)

    plt.plot(FPR, TPR, 'g', label='mean ROC=%0.4f' % ROC_AUC)

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc=0)
    plt.show()
    plt.savefig('Algrithom Mean ROC.jpg')

def bestThresholds(trainList:list,testList:list):
    tempList = trainList.copy()
    tempList.sort(reverse=True)
    TPRList = []
    FPRList = []
    for item in tempList:
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        Threshold = item
        for i in range(trainList.__len__()):
            if (testList == 1 and trainList[i] >= Threshold):
                TP += 1
            elif (testList == 0 and trainList[i] >= Threshold):
                FP += 1
            elif (testList == 1 and trainList[i] < Threshold):
                FN += 1
            else:
                TN += 1
        TPR = TP / (TP + FN) #计算真正例率
        FPR = FP / (TN + FP) #计算假正例率
        TPRList.append(TPR)
        FPRList.append(FPR)
    ROC_AUC = np.trapz(TPRList,FPRList)
    drawConfigure(ROC_AUC,np.array(TPRList),np.array(FPRList))


if __name__ == "__main__":
    # ROC_AUC_List = []
    # TPR_List = []
    # FPR_List = []
    # ROC_AUC1, TPR1, FPR1 = AnalyseAlgrithom('Random Walk with Restart')
    # ROC_AUC2, TPR2, FPR2 = AnalyseAlgrithom('Least Square')
    # ROC_AUC3, TPR3, FPR3 = AnalyseAlgrithom('KATZHCDA')
    ROC_AUC4, TPR4, FPR4 = AnalyseAlgrithom('NCPCDA')
    drawConfigure(ROC_AUC4,TPR4,FPR4)
    # ROC_AUC_List.append(ROC_AUC1)
    # ROC_AUC_List.append(ROC_AUC2)
    # ROC_AUC_List.append(ROC_AUC3)
    # ROC_AUC_List.append(ROC_AUC4)
    # TPR_List.append(TPR1)
    # TPR_List.append(TPR2)
    # TPR_List.append(TPR3)
    # TPR_List.append(TPR4)
    # FPR_List.append(FPR1)
    # FPR_List.append(FPR2)
    # FPR_List.append(FPR3)
    # FPR_List.append(FPR4)
    # drawAllConfigure(ROC_AUC_List,TPR_List,FPR_List)



    

