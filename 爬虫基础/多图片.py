import urllib.request as request
import re

# url = 'http://maoyan.com/films?'
# response = request.urlopen(url)
# result = response.read().decode('utf-8')

# a = re.compile('<img.*?src="(.*?)">',re.S)
# b = re.findall(a,result)
# print(b)

url = 'http://www.yggk.net/xiaohua/xiaohua/list1.html'
response = request.urlopen(url)
result = response.read().decode('gbk')

a = re.compile('<img.*?src="(.*?)">',re.S)
b = re.findall(a,result)
print(b)