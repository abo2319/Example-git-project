# 抓取 PTT 電影版的網頁原始碼 (HTML)
import urllib.request as req
def getData(url):
    # url="https://www.ptt.cc/bbs/Gossiping/index.html"
    # 建立一個 Request 物件, 附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)
    # 解析原始碼, 取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")  # 讓 BeautifulSoup 協助我們解析 HTML 格式文件
    # titles=root.find("div", class_="title") # 尋找隨機一個 class="title" 的 div 標籤
    titles=root.find_all("div", class_="title")
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤 (沒有被刪文), 印出來
            print(title.a.string)
    # 抓取下一頁的連結
    nextLink=root.find("a", string="‹ 上頁") # 找到內文是 ‹ 上頁 的 a 標籤
    return nextLink["href"]
    # print(nextLink["href"])
    # print(titles)
    # print(titles.a.string)
    # print(root.title.string)
# 主程序: 抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
# print(pageURL)