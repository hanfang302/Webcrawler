import requests
#使用requests发起一个get请求
response = requests.get('http://docs.python-requests.org/zh_CN/latest/')
#发起一个带参数的get请求
dict = {
    'wd':'图片'
}
# response = requests.get('http://www.baidu.com/s',params=dict)
# print(response.url)
#默认是会验证SSL证书，这里的verify设置为False是忽略SSL验证
#response = requests.get('https://www.12306.cn',verify=False)

#设置代理
#https://125.120.10.240:6666
proxies = {
    'http':'https://121.231.155.160:6666',
}
response = requests.get('https://www.baidu.com/s',params=dict,proxies=proxies)

#响应的状态码
print(response.status_code)
response.encoding = 'utf-8'
#响应的结果，字符串
#print(response.text)
#字节类型b'xxxxxx'
#print(response.content)
#查看我们请求的网址
#print(response.url)
#获取响应的头
#print(response.headers)
#可以直接读取cookie(request.cookiejar的一个对象)
# cookie = response.cookies
# print(type(cookie))
# print(type(cookie.items()))
# print(cookie.items())
# #浏览器的cookie 格式
# for item in cookie.items():
#     print(item)
#     print(item[0])
#     print(item[1])

#
