import urllib.request as request
#导入ssl
import ssl
#对数据解析urllib.parse
import urllib.parse as parse
#构造一个请求
#设置这个参数表示我们可以忽略https的请求协议
context = ssl._create_unverified_context()
#get请求
response = request.urlopen('https://docs.python.org/3/library/urllib.html') 

#答应返回结果
#print(response.read().decode('utf-8'))
#查看返回的结果类型
#print(type(response))
#查看返回的状态码
#print(response.status)
#读取返回响应的响应头加s全部,不加s是单个
#print(response.getheaders())
#单独获取响应头里面其中的一个参数
#print(response.getheader('Content-Length'))
#如果有这个参数，默认post请求，如果这个要赋值
print(response.code)
#创建一个post请求
# datadict = {
#         "name":"zhangsan",
#         "sex":"1",
# }
# data = bytes(parse.urlencode(datadict),encoding='utf-8')
# #data = parse.urlencode(datadict).encode='utf-8'
# print(data)
# response = request.urlopen('http://httpbin.org/post',data=data,context=context)
# print(response.read())

# {
#     "args":{},
#     "data":"",
#     "files":{},
#     "form":{
#          'name':'liwenhao'
#          'sex':'1'
#     },
#     "headers":
#     {"Accept-Encoding":"identity",
#     "Connection":"close",
#     "Content-Length":"9",
#     "Content-Type":"application/x-www-form-urlencoded",
#     "Host":"httpbin.org ",
#     "User-Agent":"Python-urllib/3.6"
#     },
#     "json":null,
#     "origin":"114.242.248.195 ",
#     "url":"https://httpbin.org/post "
# }


# timeout：设置请求的超时时间，一旦超过设置的值，就会报错
#urllib.error.URLError: <urlopen error _ssl.c:817: The handshake operation timed out>

#cafile:制定CA证书
# context：设置CA证书的路径
# capath：可以忽略https的请求协议
