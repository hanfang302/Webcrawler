import urllib.request
import urllib.parse
import ssl
import pymysql
import re

url = 'http://maoyan.com/cinemas?'
#request = urllib.request.Request(url)
response = request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
with open('filename.html','w') as f:
    f.write(html)

pattern = re.compile('<a.*?cinema-name')
result = re.findall(pattern,html)
 #print(result)
 #将不完整的电影院地址拼接完整用到urllib.parse.urljoin()
for i in result:
    #print(i)
    full_url = urllib.parse.urljoin(url,i[0])
    print(full_url)
    name = i[1]
    address = i[2]
