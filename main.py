# 主程式
import geometry.point # 模組的完整名稱要包含所屬的封包
result=geometry.point.distance(3,4)   #用模組中的函示
print("距離",result)
import geometry.line as line #太長可改別名
result=line.slope(1,1,3,3)
print("斜率",result)
print('hello')