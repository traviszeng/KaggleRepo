import numpy as np
import pandas as pd

pd.set_option('display.max_rows', 1024)   #设置最大显示行数
pd.set_option('display.max_columns', 1024) #设置最大显示列数

train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')

print(train.head())

print(train.shape,test.shape)

