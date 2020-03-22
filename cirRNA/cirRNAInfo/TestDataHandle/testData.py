import numpy as np
import pymysql

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
def getCircRNACancerAssociation(cancerNum:int,circRNANum:int,circRNACancerData:tuple) -> np.ndarray:
    resultMatrix = np.zeros((cancerNum, circRNANum), dtype=np.int)
    for i in range(0, circRNACancerData.__len__()):
        circRNAIndex = int(circRNACancerData[i][0])
        cancerIndex = int(circRNACancerData[i][1])
        resultMatrix[cancerIndex - 1][circRNAIndex - 1] = 1

    return resultMatrix