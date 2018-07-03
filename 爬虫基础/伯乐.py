#import requests
from urllib.request import Request,urlopen
from urllib import parse
import pymysql
import re

def boLe(url,beginPage,endPage):
    a = []
    for pages in range(beginPage,endPage+1):
        page = (pages-1)+1
        fullurl = url + '/page/' + str(page)
        req = urlopen(fullurl)
        result = req.read().decode('utf-8')
        a = re.compile('<div.*?media-body">(.*?)</div>',re.S)
        b = re.findall(a,result)
        for i in b:
            a.append(i)


def main():
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))
    url = 'http://top.jobbole.com/'
    boLe(url,beginPage,endPage)

if __name__ == '__main__':
    main()

