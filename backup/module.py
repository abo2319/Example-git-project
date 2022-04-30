# 載入內建的 sys 模組並取得資訊
# import sys as system
# print(system.platform)
# print(system.maxsize)

# 建立geometry 模組, 載入使用
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# result=geometry.slope(1,2,5,6)
# print(result)

# 調整搜尋模組的路徑(模組必須要放在這些路徑之中 Python 才會找到)
import sys
sys.path.append("modules")
print(sys.path) # 印出模組的搜尋路徑列表
print("--------------------------------------------------------")
import geometry
print(geometry.distance(1,1,5,5))