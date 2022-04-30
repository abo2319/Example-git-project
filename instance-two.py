# Point 實體物件的設計: 平面座標的點
# class Point:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
#     # 定義實體方法
#     def show(self):
#         print(self.x, self.y)
#     def distance(self, targetX, targetY):
#         return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5 
# p=Point(3,4)
# p.show() # 呼叫實體方法/ 函式
# result=p.distance(0,0) # 計算座標(3,4)和座標(0,0)之間的距離
# print(result)

# File 實體物件的設計: 包裝檔案讀取的程式
class File:
    # 定義初始化函式
    def __init__(self, name): # 初始化函式建立兩個實體屬性 name, file (file 初期是None)
        self.name=name
        self.file=None # 尚未開啟檔案: 初期是 None(Python 裡特殊資料 代表空)
    # 定義實體方法 open, read
    def open(self): # 調用 python 檔案開啟功能, 得到一個檔案物件放入實體屬性file裡
        self.file=open(self.name, mode="r", encoding="utf-8") # Python 內建檔案開啟功能
    def read(self):
        return self.file.read()
# 讀取第一個檔案
f1=File("data1.txt") # 建立實體物件,放在變數f1
f1.open() # 利用 f1代表實體物件呼叫實體方法 open
data=f1.read() # 再呼叫另一個實體方法 read 回傳資料 放入 data
print(data)
# 讀取第二個檔案
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)