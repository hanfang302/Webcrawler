# from urllib.request import Request,urlopen
# from urllib import parse
# import pymysql
import requests
from lxml import etree
#反爬虫
header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',

}
url = 'http://blog.jobbole.com/all-posts/'
#获取请求结果
response = requests.get(url,headers=header)
#print(response.text)

page_html = etree.HTML(response.text)
with open('data.html','w') as f:
    f.write(response.text)
list = page_html.xpath('//div[@class="post floated-thumb"]')
print(list)
for item in list:
    title = item.xpath('.//a[@class="archive-title"]/text()')
    #判断
    if len(title)==0:
        title = ['没有']
    print(item)

#def get_data(page):

