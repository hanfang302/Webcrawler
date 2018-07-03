#1获取网址
#2构建对象
#3查找
import requests
from bs4 import BeautifulSoup
import re
#import vsc
#反爬虫
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Mobile Safari/537.36'
}
#获取网址
url = 'https://www.autohome.com.cn/all/1/#liststart'
response = requests.get(url,headers=header)
response.encoding='gbk'
#打印响应的状态
print(response.status_code)
# with open('qichezhijia.html','w') as f:
#     f.
#获取文本
#print(response.text)
#先构建一个bs对象
soup_html = BeautifulSoup(response.text,features='html.parser')
#输出规范的HTML文档
print(soup_html.prettify)
#select是css的语法
article_list = soup_html.select('.article li')
print(article_list)

objids = []

for item in article_list:
    #print(item)
    if len(item.select('a')) !=0:
        title = item.select('h3')[0].get_text()
        href = item.select('a')[0].attrs('href')
        #href1 = item.select('a')[0].attrs('href')
        image_url = item.select('.article-pic img')[0].attrs('src')
        publish_time = item.select('.fn-left')[0].get_text()
        content = item.select('.p')[0].get_text()
        visit_num = item.select('.fn-right em')[0].get_text()
        comment_num = item.select('.fn-right em')[1].get_text()
        #从文章详情URL中获取文章id
        #a = re.compile('//www.autohome.com.cn/\w*?/\d*?/(\d*?)-*\*.html#pvareaid=\d*?')
        a = re.compile('.*?cn.*?/\d*/(.*?)[-,.].*?html')
        objid = re.findall(a,href)[0]
        objids.append(objid)
        dict ={
            'title':title,
            'href':href,
            'image_url':image_url,
            'publish_time':publish_time,
            'content':content,
            'visit_num':visit_num,
            'comment_num':comment_num,
        }
        #article_dict.append(dict)
        #print(title,href,image_url,publish_time,content,visit_num,comment_num)
    #print(type(item))
print(len(objids))
objids_str = '.'.join(objids)
print(objids_str)
url = ''
params = {
    'appid':'1',
    'dataTyepe':'jsonp',
    'objids':'objids_str',
}
com_response = requests.get(url,params=params,headers=header)
print(com_response.status_code)
print(com_response.text)
com_data = com_response.text.replace('()')
#获取评论列表数据
#url路径
#https://reply.autohome.com.cn/api/getData_ReplyCounts.ashx?appid=1&dateType=jsonp&objids=918394.918391.918393.917966.918351.918385.918383.918348.918371.918379.918369.918374.918370.918360.918357.918359.918347.912740.918337.918350.918349.918341.918338.918343.918345.918342.918340.917871.918339.918333.918244.918334.918336.918105.917978.916111.915188.918335.918332.918288.918312.918325.918327.918330.918311.918320.918316.918318.918317.918256.918310.918313.918308.918307.918304.918305.918299.918283.918284.918204&callback=jQuery1720846400777151542_1528424651879&_=1528424654983
# with open('qichezhijia.csv','a') as csvfile:
#     filename
