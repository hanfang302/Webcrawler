#import requests
#http://www.1905.com/list-p-catid-220.html
import urllib.request as request
import urllib.parse as parse
url = 'http://www.1905.com/film/?fr=homepc_menu_news'
#response = requests.get(url)
response = request.urlopen(url)
r = response.read().decode('utf-8')
print(response.read().decode('utf-8'))
with open('movie.html','w') as f:
     f.write(r)