# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set(font='SimHei') #设置画图中的中文为黑体
# plt.rcParams['axes.unicode_minus']=False  #如果X轴有负号，且显示不全的话，就加上以下语句

# from sklearn.model_selection import train_test_split
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression, SGDRegressor
# from sklearn.metrics import mean_squared_error

# from sklearn import datasets # 引入sklearn裏頭的資料集

# House = datasets.load_boston() # 取得波士頓房價的數據
# x = House.data
# y = House.target

# df = pd.DataFrame( x, columns = House.feature_names)
# df['Target'] = pd.DataFrame(y, columns = ['Target'])
# print(df.head())

# plt.figure(figsize = (15, 15))
# p = sns.heatmap(df.corr(), annot = True, square = True)
# plt.show()

import pandas as pd

groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
ironmen = [59, 9, 19, 14, 6, 77]

ironmen_dict = {
                "groups": groups,
                "ironmen": ironmen
}

# 建立 data frame
ironmen_df = pd.DataFrame(ironmen_dict)

# 刪除觀測值
ironmen_df_no_mw = ironmen_df.drop(0, axis = 0)
print(ironmen_df_no_mw)
print("---") # 分隔線

# 刪除欄位
ironmen_df_no_groups = ironmen_df.drop( 'group'=="Cloud")
print(ironmen_df_no_groups)