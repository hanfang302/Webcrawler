# #import urllib.request as request
# from urllib.request import Request,urlopen
# from urllib import parse
# import ssl
# #url = 'https://bj.fang.anjuke.com/loupan/all/'
# #url = 'https://bj.fang.anjuke.com/loupan/all/p2/'
# def tieba(url,start,end):
#     for page in range(start,end+1):
#         pn = (page-1)* 50
#         filename = '第'+str(page)+'页.html'
#         fullurl = url+"&pn="+str(pn)
#         html = loadpage(fullurl, filename)
#         writefile(html, filename)

# def loadpage(url,filename):
#     print('正在下载'+filename)
#     requestContent = ssl._create_unverified_context()
#     headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
#     request = urllib.request.Request(url, headers = headers)
#     response = urllib.request.urlopen(request,context=requestContent)
#     return response.read()

# def writefile(html,filename):
#     print('正在存储'+filename)
#     with open('filename','wb') as f:
#         f.write(html)

# if __name__ == '__main__':
#     start = int(input('请输入起始页：'))
#     end = int(input('请输入终止页：'))
#     url = "http://tieba.baidu.com/f?"
#     key = parse.urlencode({"kw" : kw})
#     # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
#     url = url + key
#     tieba(url,start,end)

import urllib.request
from urllib import parse
import ssl
def tiebaSpider(url, beginPage, endPage):
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        # 组合为完整的 url，并且pn值每次增加50
        fullurl = url + "&pn=" + str(pn)
        #print fullurl
        # 调用loadPage()发送请求获取HTML页面
        html = loadPage(fullurl, filename)
        # 将获取到的HTML页面写入本地磁盘文件
        writeFile(html, filename)

def loadPage(url, filename):
    print ("正在下载" + filename)
    requestContent = ssl._create_unverified_context()
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request,context=requestContent)
    return response.read()

def writeFile(html, filename):
    print ("正在存储" + filename)
    with open(filename, 'wb') as f:
        f.write(html)
    print ("-" * 20)
 
if __name__ == "__main__":
    kw = input("请输入需要爬取的贴吧:")
    # 输入起始页和终止页，str转成int类型
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))
 
    url = "http://tieba.baidu.com/f?"
    key = parse.urlencode({"kw" : kw})
 
    # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
    url = url + key
    tiebaSpider(url, beginPage, endPage)
