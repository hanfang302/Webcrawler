import urllib.request
import http.cookiejar

#创建一个cookiejar对象使用存储cookie
cookie = http.cookiejar.CookieJar()
#构建一个cookie的处理器对象handler
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
#作用构建opener
opener = urllib.request.build_opener(cookie_handler)
#使用open方法向服务器发送请求
response = opener.open('http://www.baidu.com')
#获取响应的状态
print(response.code)
print(cookie)
for item in cookie:
    print(item.name)
    print(item.value)
    cookie_str = cookie_str + item.name+'='item.value+';'
print(cookie_str)


#mozillaCookieJar():可以一节制定保存文件，使用save方法保存
cookie_file = 'cookie.txt'
#构建一个mozillaCookieJar对象来保存cookie
mz_cookie = http.cookiejar.MozillaCookieJar(cookie_file)
#构建一个cookie的处理对象
handler = urllib.requestHTTPCookieProcessor(mz_cookie)
#构建一个opener对象
opener = urllib.request.build_opener(handler)
#发送请求(打开URL)
response = opener.open('http://www.baidu.com')
#设置为全局的opener,调用urlopen方法是指上是使用自定义的opener
urliib.request.install_opener(opener)
urllib.request.urlopen('http://www.baidu.com')
#保存
mz_cookie.save()
print(response.code)
#读取本地的cookie
mz_cookie.loads(cookie_file)
print(mz_cookie)

