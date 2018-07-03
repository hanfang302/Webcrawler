import urllib.request
import http.cookiejar as cookiejar
from urllib import parse
cookie = cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_handler)
opener.addheaders = [
    ('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'),
]
data = {
    'email':'hanfang123@aliyun.com',
    'password':'hf123456',
}
postdata = parse.urlencode(data).encode('utf-8')
request = urllib.request.Request("http://www.renren.com/PLogin.do", data = postdata)
opener.open(request)
response = opener.open("http://www.renren.com/965722397/profile")
print(response.code)
html = response.read() 
with open('renren.html','wb') as f:
    f.write(html)
