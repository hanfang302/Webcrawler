import requests
from lxml import etree
import os

def main():

    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&kw=技术&sm=0&p=1'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.4793.400 QQBrowser/10.0.743.400'
    }
    response = requests.get(url, header=header)
    #print(response.text)
    list = etree.HTML(response.text)
    lists = []
    result = list.xpath('.//table[@class="newlist"]')  
    #print(result)
    for item in result:
        title = item.xpath('.//td[@class="zwmc"]/div[@class="title"]/text()')[0]
        link = item.xpath('.//td[@class="zwmc"]/div/[@class="title"]/@href')[0]
        fullurl = 'https://www.jianshu.com/' + link
        print(title,link,fullurl)
        lists.append(fullurl)
        if not os.path.exists(title):
            os.mkdir(title)

if __name__ == '__main__':
    main()
      

    

