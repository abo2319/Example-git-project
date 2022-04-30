#Point 實體物件的設計: 平面座標的點
# class Point:
#     def __init__(self):  # self固定
#         self.x=3
#         self.y=4
# 建立第一個實體物件, 並取得實體屬性的資料 
# p1=Point() 
# print(p1.x, p1.y) # 使用實體物件
# 建立第二個實體物件
# p2=Point()
# print(p2.x, p2.y)
# 這樣 x,y 限制為3,4
# class Point:
#     def __init__(self, x, y):  # 實體屬性: 封裝在實體物件中的變數
#         self.x=x
#         self.y=y
# p1=Point(3,4) 
# print(p1.x, p1.y) # 使用實體物件
# # 建立第二個實體物件
# p2=Point(5,6)
# print(p2.x, p2.y)

# FullName 實體物件的設計: 分開紀錄姓, 名資料的全名
class FullName:
    def __init__(self, first, last):
        self.first=first
        self.last=last
name1=FullName("S.Y", "Cho")
print(name1.first, name1.last)
name2=FullName("Z.N", "Liu")
print(name2.first, name2.last)