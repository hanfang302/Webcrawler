import requests
from lxml import etree

url = 'http://www.u148.net/text/'
response = requests.get(url)
# print(response.status_code)
# print(response.text)
list = etree.HTML(response.text)
print(list)
#url_list = []
result = list.xpath('//div[@class="mainlist"]')
#print(result)
for item in result:
        title = item.xpath('//div[@class="list-content"]/h1/a/text()')[0]
        link = item.xpath('.//div[@class="list-content"]/h1/a/@href')[0]
        fullurl = 'http://www.u148.net/text/' + link
        print(title,fullurl)



