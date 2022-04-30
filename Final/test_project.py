import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn.distributions import ecdfplot
# sns.set(font='SimHei') #设置画图中的中文为黑体
# plt.rcParams['axes.unicode_minus']=False  #如果X轴有负号，且显示不全的话，就加上以下语句

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error

x_train = pd.read_csv("Final\\train_feature.csv",encoding='big5')
x_test = pd.read_csv("Final\\test_feature.csv",encoding='big5')
label = pd.read_csv("Final\\train_label.csv",index_col='Index')
# x_train['price_per_ping'] = label




# print("The train data size before dropping Index feature is : {} ".format(x_train.shape))
# print("The test data size before dropping Index feature is : {} ".format(x_test.shape))

#Save the 'Index' column
train_Index = x_train['Index']
test_Index = x_test['Index']

#Now drop the  'Index' colum since it's unnecessary for  the prediction process.
x_train.drop("Index", axis = 1, inplace = True)
x_test.drop("Index", axis = 1, inplace = True)
x_train.drop(labels = ['非都市土地使用分區', '非都市土地使用編定'], axis = 1, inplace = True)


x_train['house_ping'] = x_train['建物移轉總面積(平方公尺)'] - x_train['車位移轉總面積(平方公尺)']
# print(x_train['house_ping'])
# print(x_train.head())














# #check again the data size after dropping the 'Index' variable
# print("\nThe train data size after dropping Index feature is : {} ".format(x_train.shape)) 
# print("The test data size after dropping Id feature is : {} ".format(x_test.shape))



# x_train = x_train.drop(x_train[(x_train['土地移轉總面積(平方公尺)']>50000 ) & (x_train['price_per_ping']>6000000)].index)

# fig, ax = plt.subplots()
# ax.scatter(x = x_train['土地移轉總面積(平方公尺)'], y = x_train['price_per_ping'])
# plt.ylabel('土地移轉總面積(平方公尺)', fontsize=13)
# plt.xlabel('price_per_pin', fontsize=13)
# plt.show()


# print(x_train.head())

# print(x_train.columns)
# print(x_train.dtypes)
# print(x_train.select_dtypes(include=["object"]).apply(pd.Series.nunique, axis = 0))
# print(x_train.dtypes.value_counts())
# print(x_train.isnull().sum())
# print(x_test.head())


# print(x_train['nearest_tarin_station'].value_counts())
# print(str(set(x_train['鄉鎮市區'])))
# print(list(x_train))

# int_features = []
# float_features = []
# object_features = []

# for dtype, feature in zip(x_train.dtypes, x_train.columns):
#     if dtype == 'float64':
#         float_features.append(feature)
#     elif dtype == 'int64':
#         int_features.append(feature)
#     else:
#         object_features.append(feature)

# print(f'{len(int_features)} Integer Features : {int_features}\n')
# print(f'{len(float_features)} Float Features : {float_features}\n')
# print(f'{len(object_features)} Object Features : {object_features}')


# cat_features = ['主要建材', '主要用途','交易標的','土地區段位置/建物區段門牌','建物型態', '建物現況格局-隔間', '有無管理組織','車位類別', '都市土地使用分區', '鄉鎮市區','num_of_bus_stations_in_100m','location_type','nearest_tarin_station' ]
# num_features = ['交易年月日','交易筆棟數','土地移轉總面積(平方公尺)','建物現況格局-廳', '建物現況格局-房', '建物現況格局-衛',  '建物移轉總面積(平方公尺)', '建築完成年月', '移轉層次', '總樓層數', '車位移轉總面積(平方公尺)','income_avg', 'income_var', 'nearest_tarin_station_distance', 'lat', 'lng']
# dtype_dict = {c: 'category' for c in cat_features}
# num_dict = {c: np.float32 for c in num_features}
# dtype_dict.update(num_dict)
# print(dtype_dict)

# x_train = x_train.drop(labels = ['非都市土地使用分區', '非都市土地使用編定'], axis = 1, inplace = True)
# print(x_train.head())



# print(x_train['price_per_ping'].describe())
# plt.subplots(figsize=(8, 6))
# sns.distplot(x_train['price_per_ping'])
# sns.boxplot(x_train['price_per_ping'])
# plt.show()
# print("Skewness: %f" % x_train['price_per_ping'].skew())
# print("Kurtosis: %f" % x_train['price_per_ping'].kurt())

