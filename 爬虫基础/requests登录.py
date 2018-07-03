import requests
import ssl
import re

context = ssl._create_unverified_context()
url = 'https://github.com/login'
user = 'user'
password = 'password'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.4793.400 QQBrowser/10.0.743.400'
}
response = requests.get(url,headers=header)
pattern = re.compile('<input name="authenticity_token" type="hidden" value="(.*)" />')
result = re.findall(pattern,response)
