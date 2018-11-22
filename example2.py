# 属性构造
import pymysql
import pandas as pda
import numpy as npy

conn = pymysql.connect(host="127.0.0.1", user="root",passwd="root", db="hexun")
sql = "select price, comment from muhexun"
data = pda.read_sql(sql, conn)
print(data)
ch = data["comment"]/data["hits"]
data["评论点击比"] = ch
file = "./hexun.xls"
data.to_excel(file, index=False)
