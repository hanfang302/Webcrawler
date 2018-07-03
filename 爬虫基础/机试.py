import requests
from lxml import etree
import os

def main():

    url = 'https://www.jianshu.com/c/7b2be866f564?utm_medium=index-collections&utm_source=desktop'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.4793.400 QQBrowser/10.0.743.400'
    }
    response = requests.get(url, headers=header)
    #print(response.text)
    list = etree.HTML(response.text)
    url_list = []
    #result = list.xpath('.//ul[@class="note-list"]')
    result = list.xpath('.//li[@class="have-img"]')  
    #print(result)
    for item in result:
        title = item.xpath('.//div[@class="content"]/a[@class="title"]/text()')[0]
        link = item.xpath('.//div[@class="content"]/a/[@class="title"]/@href')[0]
        author = item.xpath('.//a[@class="nickname"]/text()')[0]
        #content = item.xpath('.//div[@class="content"]/p[@class="abstract"]/text()')
        #img = item.xpath('.//img[@class=" img-blur-done"]')
        fullurl = 'https://www.jianshu.com/' + link
        print(title,author,fullurl)
        url_list.append(fullurl)
        if not os.path.exists(title):
            os.mkdir(title)


if __name__ == '__main__':
    main()
      

    

