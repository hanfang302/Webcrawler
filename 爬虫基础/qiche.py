#beatuifulsoup4 跟xpath一样，是用来帮助我们清洗数据的
from bs4 import BeautifulSoup
import requests
from lxml import etree
#import csv
url = 'https://www.autohome.com.cn/all/2/#liststart'
#url = 'https://hr.tencent.com/position.php?&start=0#a'
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
response = requests.get(url,headers=header)
print(response.status_code)
with open('qichezhijia.html','w') as f:
    f.write(response.text)
html = response.text
#构建一个beautifulsoup对象，他是一个tag对象
#soup = BeautifulSoup(html,'lxml')
#soup = BeautifulSoup(open('qichezhijia.html'),'lxml')
soup = BeautifulSoup(response.text,'lxml')
xpath = etree.HTML(response.text)
#print(soup.prettify)
#print(type(soup))
tr_result = soup.find_all('tr')
#find_all使用class属性为选择条件的时候，一定要注意class_
# tr_result1 = soup.find_all(class_='even')
tr_result2 = soup.find_all(class_='odd')
tr_result1 = soup.select('.event')
result = tr_result1 + tr_result2

#print(tr_result2)(一条数据)
#根据id查找，
#tr_result1 = soup.find_all(id='homeDep')
#find_all返回的是一个list

#css选择器基本语法：
# <td><h3 class='oppt' id='ncnk'><td><h3><h1></h1></h3></td>
# soup.select('td h3 h1')
# soup.select('.oppt')

for tr in tr_result:
    #print(tr)
    #css选择器select
    title = tr.select('td a')[0].get_text()
    job_type = tr.select('td')[1].get_text()
    need_pople = tr.select('td')[2].get_text()
    adress = tr.select('td')[3].get_text()
    publish = tr.select('td')[4].get_text()
    print(title,job_type,need_pople,adress,publish)
    dict = {
        'title':title,
        'job_type':job_type,
        'need_pople':need_pople,
        'adress':adress,
        'publish':publish,
    }
with open("zhiwei.csv","a") as csvfile:
    fielanames = ['title','job_type','need_pople','adress','publish']
    #句柄
    #writer = csv.DictWrite(csvfile,fieldnames=fieldnames)
    #writer.writerow(dict)
    #创建文件句柄
    #writer = csv.writer(csvfile) 

    #print(type(tr))

# xpath写法
# xtr_odd = xhtml.xpath('//tr[@class="odd"]')
# xtr_even = xhtml.xpath('//tr[@class="even"]')

# soup = BeautifulSoup(html,'lxml')
# #prettify帮助我们格式化输出转换的HTML
# #print(soup.prettify())
# print(soup.p)
# print(soup.head)
# print(type(soup.head))
# #获取标签的所有属性
# print(soup.p.attrs)
# #删除功能
# del soup.p['class']
# print(soup.p)

# # findall()
# result = soup.find_all('p')
# print(result)
# for i in result:
#     #获取名字
#     print(i.name)
#     #获取属性
#     print(i.attrs)
#     #获取文本1
#     print(i.string)
#     #获取文本2
#     print(i.get_text())
# # css语法来写(用法)
# #（.）表示class属性
# #（#）表示属性


