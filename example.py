import pymysql
import pandas as pda
import numpy as npy

conn = pymysql.connect(host="127.0.0.1", user="root",passwd="root", db="csdn")
sql = "select price, comment from taob"
data = pda.read_sql(sql, conn)
print(data)
# 离差标准化
data2 = (data-data.min())/(data.max()-data.min())
print(data2)
# 标准差标准化
data3 = (data-data.mean())/data.std()
print(data3)
# 小数定标规范化
k = npy.ceil(npy.log10(data.abs().max())) 
data4 = data/10**k
print(data4)
# 等宽离散化
data5 = data["price"].copy()
data6 = data5.T
data7 = data6.values
k = [0, 50, 100, 300, 500, 2000, data7.max()]
c = pda.cut(data7, k, labels=["1cheap","2cheap","intermediate","1expensive","2expensive","3expensive"])
print(c)













 
















