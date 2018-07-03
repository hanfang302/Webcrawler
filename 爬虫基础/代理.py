#urllib使用代理
#服务器把自己的ip封掉（请求的次数过于频繁，超过服务器设置的值）
#有付费代理和免费代理
import urllib.request

proxy = [
    '代理1',
    '代理2',
]
for i in proxy:
    #构建一个代理proxyhandler对象
    handler = urllib.request.ProxyHandler({'协议':'IP+端口号'})
    #需要用户名和密码的代理(需要验证)
    #urllib.request.ProxyHandler({'协议':'用户名:密码@IP+端口号'})
    #创建一个opener对象
    opener = urllib.request.bulid_opener(handler)
    #使用opener.open方法发起请求
    opener.open('http://www.baidu.com')
    html = response.read()
if html:
    #查看响应的结果code
    print(response.code)
    print('当前代理可用')
else:
    print('不可用')

# #查看响应的结果
# print(response.code)
