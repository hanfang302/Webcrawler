import requests
from lxml import etree

url = 'http://top.jobbole.com/'
#反爬虫
header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
#获取请求的结果
response = requests.get(url,headers=header)
#用xpath中的etree方法自动补全HTML
bl = etree.HTML(response.text)
#运用xpath方法爬取标题
list = bl.xpath('.//div[@class="media-body"]')
print(list)
for item in list:
    title = item.xpath('.//h3[@class="p-tit"]/a/text()')#标题
    link = item.xpath('.//h3[@class="p-tit"]/a/@href')#链接
    time = item.xpath('.//p[@class="p-meta"]/span[1]/text()')#时间
    tag = item.xpath('.//p[@class="p-meta"]/span[@class="p-tags"]/a/text()')#标签
    comment = item.xpath('.//i[@class="fa fa-comments-o"]')#评论
    if len(tag) == 0:
        tag = '没有标签'
    if len(comment) == 0:
        comment = '没有评论'
    elif len(comment)>0:
        if tag == '未知标签'
            comment = item.xpath('.//p[@class="p-meta"]/span[2]/a/text()')
        else:
            comment = item.xpath('.//p[@class="p-meta"]/span[3]/a/text()')
           
    print(item)