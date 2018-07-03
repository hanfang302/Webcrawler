from urllib.request import Request,urlopen
import urllib.parse as parse
import ssl
#import urllib.request as request
#urlopen（官方给我们封装一个简单的发起请求的方法）
#def __init__(self, url, data=None, headers={},
#                 origin_req_host=None, unverifiable=False,
#                 method=None):
#url:我们要请求的网址
#data:我们需要输入的相关参数，如果要传入的话必须是bytes类型
#(如果这个字段有值，它默认的是一个post请求)
#headers：请求头（cookies,user-Agent,Referer,Connection）
#origin_req_host：子域名者或则IP
#method：请求方式（Post/get）
#unverifiable:意思是用户没有足够的权限来访问资源
#默认是False，表示我们有权限获取，默认是True表示我们没有权限获取

#构建一个请求对象
url = 'http://www.1905.com/film/?fr=homepc_menu_news'
headers = {
    'User_Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
#构造一个get方式的请求对象，设置了url,headers,请求方式
req = Request(url,headers=headers,method='GET')
#发起请求
response = urlopen(req)
print(response.read())

#构造一个带参数的get请求
#https://www.baidu.com/s?ie=utf-8&wd=美女
#https://www.baidu.com/s?ie=utf-8&wd=%E7%BE%E5%A5%B3
# data = {
#     'wd':'美女',
#     'ie':'utf-8',
# }
# url = 'https://www.baidu.com/s?'
# data = parse.urlencode(data).encode('utf-8')
# print(data)
# context = ssl._create_unverified_context()
# #data是Post请求
# req = Request(url,data=data,headers=headers,method='GET')
# response = urlopen(req,context=context)
# print(response.read().decode('utf-8'))


# data = {
#     'wd':'美女',
#     'ie':'utf-8',
# }
# data = parse.urlencode(data).encode('utf-8')
