import urllib.request
from urllib import parse
import ssl

def tiebaSpider(url, beginPage, endPage,key1,key2):
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 10
        filename = "第" + str(page) + "页.txt"
        # 组合为完整的 url，并且pn值每次增加50
        fullurl = url + key1+ "&pn=" + str(pn) + key2
        # 调用loadPage()发送请求获取HTML页面
        html = loadPage(fullurl, filename)
        # 将获取到的HTML页面写入本地磁盘文件
        writeFile(html, filename)
#(3)我们已经之前写出一个爬取一个网页的代码。现在，我们可以将它封装成一个小函数loadPage，供我们使用。
def loadPage(url, filename):
    print ("正在下载" + filename)
    requestContent = ssl._create_unverified_context()
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request,context=requestContent)
    return response.read()
#(4)最后如果我们希望将爬取到了每页的信息存储在本地磁盘上，我们可以简单写一个存储文件的接口。
def writeFile(html, filename):
    print ("正在存储" + filename)
    with open(filename, 'wb') as f: 
        f.write(html)
    print ("-" * 20)
#(1)模拟 main 函数
if __name__ == "__main__":
    kw = input("请输入需要爬取的贴吧:")
    # 输入起始页和终止页，str转成int类型
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))
    url = "http://www.baidu.com/s?"
    key1 = parse.urlencode({"wd" : kw})
    key2 = parse.urlencode({"op":kw})
    tiebaSpider(url, beginPage, endPage,key1,key2)
