import numpy as np
# def Normalized1(x):
#     u = np.mean(x)
#     o = np.std(x)
#     return np.round((x-u)/o)
# def Normalized2(x):
#     if(x >= 1):
#         return 1
#     else:
#         return 0
# A = np.array([[2,3],[3,4]],dtype=float)
# for j in range(2):
#     A[j] = Normalized1(A[j])
# print(A)
# function_Normalized2 = np.vectorize(Normalized2)
# A = function_Normalized2(A)
# print(A)
# B=np.array([[2,3]])
# print(np.std(B))
# a = [2,3,4]
# print(np.sum(a))

resultMatrix = np.array([[1,2],[3,4]])
print(resultMatrix[0])