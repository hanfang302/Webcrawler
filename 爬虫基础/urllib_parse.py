#urllib.parse:解析url,拼接，编码
import urllib.parse
import ssl
#urlparse拆分一个url，分解出各个组成部分
url = 'https://www.baidu.com'
result = urllib.parse.urlparse(url)
print(result)
#query=':
#scheme:协议
#netloc:域名
#path:路径
#params:参数
#query:查询条件，一般用于get请求
#fragment:锚点

#urlunparse 拼接
uels = ('https','www.baidu.com','s','','ie=utf-8','a')
fullurl = urllib.parse.urlunparse(uels)
print(fullurl)

#urlencode 一般用于将字典序列化为url编码格式
dict = {
    'name':'lisi',
    'password':'123456',
}
#data = urllib.parse.urlencode(dict).encode('utf-8')
data = bytes(urllib.parse.urlencode(dict),encode='utf-8') 
print(data)

#parse_qs:将URL的编码格式反序列化字典
result = urllib.parse.parse_qs(data)
print(result)
for k,v in result.items():
    print(k.decode('utf-8'))
    print(v[0].decode('utf-8'))

#urljoin:url的拼接
base_url = 'http://maoyan.com/cinemas'
son_url = 'cinema/15280?poi=99389254'
fullurl = urllib.parse.urljoin(base_url,son_url)
print(fullurl)
