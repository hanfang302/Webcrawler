import urllib.request as request
import urllib.parse as parse
#import ssl
#目标网址
#get请求
url = 'http://www.1905.com/film/?fr=homepc_menu_news'
#构造请求，发起请求，获取响应。
response = request.urlopen(url)
#获取内容，用decode解码，赋值给resultcontent
r = response.read().decode('utf-8')
#直接打印结果
print(response.read().decode('utf-8'))

#写入本地文件
#打开一个文件，如果不纯在就创建，W表示写入，写入的必须是字符串
f = open('movie.html','w')
#往文件中写入内容
f.write(r)

# with open('movie.html','w') as f:
#     f.write(r)

#反爬虫最基本常识
#user-Agent:
#谷歌：