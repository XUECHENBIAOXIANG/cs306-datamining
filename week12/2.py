#Freely explore the following datasets and present meaningful outcomes.#有个数据集cereal。csv.
#name,mfr,type,calories,protein,fat,sodium,fiber,carbo,sugars,potass,vitamins,shelf,weight,cups,rating
#100% Bran,N,C,70,4,1,130,10,5,6,280,25,3,1,0.33,68.402973
#请尝试各种可视化结果
#Bar/Column or line or Scatter or Stacked Bar/Column or Dual-Axis

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
# Step 1: Load data from csv files
data = pd.read_csv("cereal.csv")
# Step 2: Data cleaning
# Step 3: Get features
X = data[['potass']]
Y = data[['rating']]
# 绘图
plt.scatter(X, Y)
plt.xlabel('potass')
plt.ylabel('rating')
plt.show()
# Stacked Bar/Column
#data 先根据rating排序
data = data.sort_values('rating')
data[['potass', 'sodium','calories']].plot(kind='bar', stacked=True)
plt.show()
