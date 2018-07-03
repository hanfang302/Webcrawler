import requests

def main():

    url = 'https://www.jianshu.com/c/7b2be866f564?utm_medium=index-collections&utm_source=desktop'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.4793.400 QQBrowser/10.0.743.400'
    }
    response = requests.get(url, headers=header)