import requests
from lxml import etree

def main():
    url = 'http://www.u148.net/text/'
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text)
    list = etree.HTML(response.text)
    print(list)

    result = list.xpath('//div[@class="mainlist"]')

if __name__ == '__main__':
    main()