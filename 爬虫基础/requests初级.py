import requests
import re

# r = requests.get('http://blog.jobbole.com/all-posts/')
# pattern = re.compile('<span.*?excerpt.*?>(.*?)</span>',re.S)
# content = re.findall(pattern,r.text)
# print(content)

# r = requests.get('https://github.com/favicon.ico')
# #print(r.content)
# with open('favicon.ico','wb') as f:
#     f.write(r.content)

date = {'address':'french','name':'xiaomeng'}
r = requests.post('http://httpbin.org/post',data=date)
print(r.text)