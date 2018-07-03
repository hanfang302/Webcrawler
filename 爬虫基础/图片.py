from urllib.request import Request,urlopen
from urllib import parse
import ssl
import re
def tiebaSpider(url, beginPage, endPage):
    b = []
    for page in range(beginPage, endPage + 1):
        fullurl = url + str(page) + '.html'
        # print(fullurl)
        reqponse = urlopen(fullurl)
        resultcontent = reqponse.read().decode('utf-8')
        pattern = re.compile('<img.*?magazine_img.*?data-original="(.*?)".*?alt.*?>',re.S)
        result = re.findall(pattern,resultcontent)
        for i in result:
            b.append(i)
    # print(b)
    writes(b)
    
def writes(b):
    a = 1
    for i in b:
        print("正在保存")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        requestContent = ssl._create_unverified_context()
        request = Request(i, headers=headers)
        response = urlopen(request,context=requestContent)
        image = response.read()
        
        filename = str(a) + '.jpg'
        with open(filename, "wb") as f:
            f.write(image)
            print("已成功下载"+filename)
        a = a + 1

def main():
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))
    url = 'https://www.ugirls.com/Index/Search/Magazine-57-'
    tiebaSpider(url,beginPage,endPage)

if __name__ == '__main__':
    main()
