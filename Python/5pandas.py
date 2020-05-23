#  数据读取-------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def print_sum(x,y):
  z = x + y
  return(z)

print_sum(10,10)   # !!! 哇，也是蛮好用的吗！

obj1 = np.arange(16).reshape(2,8)

obj1.dtype

obj1.shape = (4,4)

obj1

obj1.shape = (8,2)

obj1
df = pd.read_csv("D:/RBookLearning/Causal_Inference/Python/5data/ex1.csv")
df

pd.read_table("D:/RBookLearning/Causal_Inference/Python/5data/ex1.csv",
              sep = ",")

pd.read_csv("D:/RBookLearning/Causal_Inference/Python/5data/ex2.csv",header = None)

pd.read_csv("D:/RBookLearning/Causal_Inference/Python/5data/ex2.csv",
            header = None,
            names = ["a","b","c","d","message"])

names = ["a","b","c","d","message"]
names

pd.read_csv("Python/5data/ex2.csv",names = names,index_col = "message")

pd.read_csv("Python/5data/csv_mindex.csv")
  
parsed = pd.read_csv("Python/5data/csv_mindex.csv",index_col = ["key1","key2"])
parsed

list(open("Python/5data/ex3.txt"))

pd.read_table("Python/5data/ex3.txt",sep = "\s+")

pd.read_csv("Python/5data/ex4.csv")

pd.read_csv("Python/5data/ex4.csv",skiprows = [0,2,3])

result = pd.read_csv("Python/5data/ex5.csv")
result

pd.isnull(result)

# 逐行读取文本文件

pd.read_csv("Python/5data/ex6.csv")

pd.read_csv("Python/5data/ex6.csv",nrows = 5)

result = pd.read_csv("Python/5data/ex6.csv",chunksize = 1000)
result

# 文件写出

# 读取Excel数据

data = pd.read_excel("Python/5data/ex7.xlsx")
data
data.to_excel("Python/5data/data.xlsx")

# 读取JSON数据













































