# -*- coding:UTF-8 -*-
import urllib.request as request
import ssl
#对数据解析urllib.parse
import urllib.parse as parse
#设置这个参数表示我们可以忽略http的请求协议
context = ssl._create_unverified_context()
#构造一个请求
#get请求
response = request.urlopen('https://docs.python.org/3/library/urllib.html') 

#答应返回结果
print(response.read().decode('utf-8'))
#查看返回的结果类型
print(type(response))
#查看返回的状态码
print(response.status)
#读取返回响应的响应头家s全部,不加s是单个
print(response.getheaders())
#单独获取响应头里面其中的一个参数
print(response.getheader('Content-Length'))
