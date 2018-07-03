import urllib.request as request
import urllib.parse
import ssl

def tieBa(beginPage,endPage,):
    for page in range(beginPage,endPage+1):
        #每一页的网址pn+50，它是从零开始的
        pn = (page-1)*10
        #给获取到的文件起名称
        filename = "第" + str(page) + "页.html"
        fullurl = url + '&pn=' + str(pn)
        html = loadPage(fullurl,filename)
        writeFile(html,filename)

def loadPage(url,filenname):
    print('正在下载'+filenname)
    requestContent = ssl._create_unverified_context()
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request,context=requestContent)
    return response.read()

def writeFile(html,filename):
    print('正在存储'+filename)
    with open(filename,'wb') as f:
        f.write(html)
    print('-'*15)


if __name__ == "__main__":
    beginPage = int(input('请输入起始页:'))
    endPage = int(input('请输入终止页:'))
    url = 'http://tieba.baidu.com/f?'
    tieBa(url,beginPage,endPage)



