#import pyquery.PyQuery as PyQuery
from pyquery import PyQuery
import lxml
import requests

#目标url
url = 'http://blog.jobbole.com/all-posts/'
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
response = requests.get(url,headers=headers)
#状态码
print(response.status_code)
with open('jobble.html','w') as f:
    f.write(response.rext)

pq_html = PyQuery(response.text)
#pq_html = PyQuery(filename='jobble.html')
#pq_html = PyQuery(url)
print(type(pq_html))
print(pq_html())

#取值
result_articles = pq_html('.post.floated-thumb')

for sub_div in result_articles.items():
    print('---Korean----')
    print(type(sub_div))
    title = sub_div('.archive-title').text()
    link = sub_div('.archive-title').arrt('href')
    print(title.link)
    #获取子元素
    print(sub_div.children())
    print(sub_div.addClass('German'))