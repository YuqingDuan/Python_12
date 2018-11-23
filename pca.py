# 属性规约与数值规约
# PCA主成分分析算法 https://blog.csdn.net/huangfei711/article/details/78663474
    # 1.计算每一列属性的平均值
    # 2.计算去平均值矩阵，即每一位特征减去各自的平均值
    # 3.计算协方差矩阵 Cov(X,Y)=[(X-E(X))*(Y-E(Y))]/(n-1)
    '''
    [[Cov(X1,X1), Cov(X1,X2), Cov(X1,X3) ... Cov(X1,Xn)]
     [Cov(X2,X1), Cov(X2,X2), Cov(X2,X3) ... Cov(X2,Xn)]
     [Cov(X3,X1), Cov(X3,X2), Cov(X3,X3) ... Cov(X3,Xn)]
     ...
     [Cov(Xn,X1), Cov(Xn,X2), Cov(Xn,X3) ... Cov(Xn,Xn)]]
     '''
    # 4.计算协方差矩阵的特征值和特征向量
    # 5.对特征值从大到小排序
    # 6.选择最大的特征值对应的特征向量
    # 7.将数据转换到这个特征向量构建的新空间中


from sklearn.decomposition import PCA
import pymysql
import pandas as pda
import numpy as npy

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "Devilhunter9527", db = "hexun")
sql = "select * from tmuhexun"
data = pda.read_sql(sql, conn)
ch = data["comment"]/data["hits"]
data["评论点击比"] = ch

# PCA
pca1 = PCA()
pca1.fit(data)
# 返回模型中的各个特征量：
characteristic = pca1.components_
print(characteristic)
# 返回各个成分中各自方差的百分比，贡献率：
rate = pca1.explained_variance_ratio_
print(rate)
# 降维操作：
# pca中的参数为希望的维数：
pca2 = PCA(2)
pca2.fit(data)
reduction = pca2.transform(data)
characteristic2 = pca2.components_
print(characteristic2)
print(reduction)

# 对降维数据进行恢复：
recovery = pca2.inverse_transform(reduction)
print(recovery)











