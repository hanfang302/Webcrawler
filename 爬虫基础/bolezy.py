from urllib.request import Request,urlopen
import re
import requests
from lxml import etree
import pymysql

def get(url,start,end):
    for page in range(start,end + 1):
        furl = url + 'page/%s/'%page
        chuli(furl)
        print(furl)
def chuli(furl):
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

    url = 'http://top.jobbole.com/'
    response = requests.get(url,headers=header)

    # print(response.text)
    page_html = etree.HTML(response.text)
    list = page_html.xpath('//li[@class="media"]')
    for item in list:
        title = item.xpath('.//h3[@class="p-tit"]/a/text()')[0]
        link = item.xpath('.//h3[@class="p-tit"]/a/@href')[0]
        pub_data = item.xpath('.//p[@class="p-meta"]/span[1]/text()')[0]
        tag = item.xpath('.//p[@class="p-meat"]/span[@class="p-tags"]/a/text()')
        if len(tag) == 0:
            tag = '没有标签'
        #如果存在i[@class="fa fa-comments-o"]，说明有评论
        comment = item.xpath('.//i[@class="fa fa-comments-o"]')
        if len(comment) == 0:
            comment = '0'  #如果没找到i[@class="fa fa-comments-o"]，说明没有评论
        elif len(comment) > 0:
            if tag == '没有标签':   #有评论，没标签1               
                #没有标签的情况
                comment = item.xpath('.//p[@class="p-meta"]/span[2]/a/text()')[0]
            else:   #有评论  有标签
                comment = item.xpath('.//p[@class="p-meta"]/span[3]/a/text()')[0]
        print(title, link, pub_data,tag,comment)
        conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='bole', port=3306,charset='utf8')
        cur = conn.cursor()
        sql = 'INSERT INTO bole(title, link, pub_data,tag,comment) VALUES("%s","%s","%s","%s","%s")'
        cur.execute(sql,(title, link, pub_data,tag,comment))
        conn.commit()
        conn.close()
def fenye():
    fenye = int(input('请输入查询的页数：'))
    q = ( fenye - 1)*15
    conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='bole', port=3306,charset='utf8')
    cur = conn.cursor()
    sql = 'select * from bole limit %d,15'%int(q)
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
fenye()
if __name__ == '__main__':
    start = int(input("请输入开始的页数："))
    end = int(input("请输入截止的页数："))
    url = 'http://top.jobbole.com/'
    #http://top.jobbole.com/page/2/ 

    get(url,start,end)
