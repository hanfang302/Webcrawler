import requests
import re
#http://dianying.2345.com/list/-------2.html

def dianying(page):
    url = 'http://dianying.2345.com/list/'+str(page)+'.html'
    response = requests.get(url)
    print(response.text)
    pattern = re.compile('>100</a>.*?<a.*?href="(.*?)">.*?下一页/</a>',re.S)
    next_page = re.findall(pattern,response.text)
    print(next_page)

    if next_page:
        dy(next_page[0])
    pattern = re.compile('<li.*?196116>(.*?)</li>',re.S)
    result = re.findall(pattern,response.text)
    for i in result:
        

    with open('filename','w') as f:
        f.write(html)

        