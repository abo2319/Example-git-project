# 抓取 PTT 電影版的網頁原始碼 (HTML)
import urllib.request as req
url="https://medium.com/_/graphql"
# 建立一個 Request 物件, 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 根據觀察, 取得的資料是 JSON 格式
# print(data)
# 解析 JSON 格式的資料, 取得每篇文章的標題
import json
data=json.loads(data) # 把原始的資料解析成字典/列表的表示形式
print(data)
# 取得 JSON 資料中的文章標題
