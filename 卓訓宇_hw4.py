import numpy as np
import pandas as pd
# # Q1
# data = np.arange(2,25,2)

# # 1-1
# B = data
# print(B)

# # 1-2
# B = data.reshape(3,4)
# print(B)

# # 1-3
# C = B[2]
# print(C)
# print(C.shape)

# # 1-4
# D = C[:, np.newaxis]
# print(D)
# print(D.shape)


# # Q2
# import numpy as np
# x = np.array([[2,4],[6,8]], dtype=np.float64)
# y = np.array([[3,5],[7,9]], dtype=np.float64)

# # 2-1
# print(x[x > 4])

# # 2-2
# print(x + y)

# # 2-3
# print(np.dot(x, y))

# # 2-4
# print(x.sum(axis = 0)) # 行總和
# print(x.sum(axis = 1)) # 列總和


# # Q3
# train = pd.read_csv('train_feature.csv',encoding='big5', index_col='Index')

# # 3-1
# train_l = pd.read_csv('train_label.csv',encoding='big5', index_col='Index')
# print(train_l.shape)

# # 3-2
# df = pd.merge(train, train_l, on = 'Index', how ='outer')
# a = df.rename(columns={'price_per_ping': 'label'})  # 依提示
# print(a.columns)

# Q4
# 4-1 將 train_feature 內資料欄位'主要建材'、'鄉鎮市區'、'lat'、'lng'擷取到另一變數中，並打印出其前 10 列。
train = pd.read_csv('train_feature.csv',encoding='big5', index_col = 0, usecols = ['Index', '主要建材', '鄉鎮市區', 'lat', 'lng'])
a = train.iloc[ :11]
print(a)


# 4-2 篩選出 鄉鎮市區為大安區且鄰近的捷運站(nearest_tarin_station)為大安站的資料,並打印其location_type。
train = pd.read_csv('train_feature.csv',encoding='big5', index_col='Index', low_memory=False)
filter = (train['鄉鎮市區'] == '大安區') & (train['nearest_tarin_station'] == '大安站')
a = train.loc[filter, ['location_type']]
print(a)


# # 5
# # 5-1 計算出不同鄉鎮市區的平均經緯度(lat、lng)。
# train = pd.read_csv('train_feature.csv',encoding='big5', index_col = 0, usecols = ['Index', '鄉鎮市區', 'lat', 'lng'])
# a = train.groupby('鄉鎮市區').mean()
# print(a)

# #5-2 將上述鄉鎮市區使用經緯度的高低，從高到低排列，先排經度在排緯度。
# train = pd.read_csv('train_feature.csv',encoding='big5', index_col = 0, usecols = ['Index', '鄉鎮市區', 'lat', 'lng'])
# mean_lat_lng = train.groupby('鄉鎮市區').mean()
# a = mean_lat_lng.sort_values('lat', ascending=False)
# print(a)