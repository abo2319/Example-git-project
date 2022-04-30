import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.style as style

train = pd.read_csv('train_feature.csv',encoding='big5', index_col='Index', low_memory=False)
label = pd.read_csv('train_label.csv',index_col='Index')
train['label'] = label

## Q1

# data = label.head(100)
# fig1, ax1 = plt.subplots()
# ax1.set_title('Box Plot')
# ax1.boxplot(data)
# plt.show()


## Q2

# a = train[train['label'] > 300000]
# group = a.groupby('建物現況格局-廳')['label'].mean()
# group.plot( x ='建物現況格局-廳', y = 'label', kind = 'bar' )
# plt.xlabel('num_of_rooms')
# plt.ylabel('dollar')
# plt.xticks(rotation = 'horizontal')
# plt.title('bar plot of buildings')
# plt.show()


## Q3

# Da_an = train[train["鄉鎮市區"] == "大安區"]
# sns.countplot(data =  Da_an, x = '主要用途')
# plt.title('大安區房屋用途')
# plt.show()


## Q4
# sns.scatterplot(data = train, x = 'nearest_tarin_station_distance', y = 'income_avg', hue = '鄉鎮市區')
# plt.show()