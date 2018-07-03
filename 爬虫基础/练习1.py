import urllib.request as request
#ssl对网络连接进行加密
import ssl
import urllib.parse as parse

#设置这个参数表示我们可以忽略http的请求协议
context = ssl._create_unverified_context()
#get请求
# response = request.urlopen('https://docs.python.org/3/library/urllib.html')
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.getheaders())
# print(response.getheader('Content-Length'))

#Post请求
datas = {
    'name':'zhangsan',
    'address':'French',
}
data = bytes(parse.urlencode(datas),encoding='utf-8')
print(data)
response = request.urlopen('http://www.baidu.com',data=data,context=context)
print(response.read())
