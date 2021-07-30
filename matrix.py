import numpy as np
import numpy.matlib #需要引入矩阵相关的库
#有关numpy的用法示例代码
#求矩阵的乘法
# m1=np.array([[1,2],[3,4]])
# m2=np.array([[5,6],[7,8]])
# m3=np.matmul(m1,m2)
# print(m3)

#求矩阵的逆
# m1=np.array([[1,2],[3,4]])
# m2=np.linalg.inv(m1)
# print(m2)

#求矩阵的转置矩阵
# m1=np.array([[1,2,3],[4,5,6]])
# m2=np.transpose(m1)
# print(m2)

#求行列式的值，存疑，为什么算的不准确
# m1=np.array([[1,2],[3,4]])
# Sum=np.linalg.det(m1)
# print(Sum)

#生成单位矩阵
# m1=np.matlib.identity(5,dtype=int)
# print(m1)