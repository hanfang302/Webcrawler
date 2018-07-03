from selenium import webdriver
from lxml import etree
import re
import json
def shousuo():
    opt = webdriver.ChromeOptions()
    opt.set_headless()
    #创建浏览器对象
    browse = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver',options=opt)
    #模拟浏览器发起一个请求
    browse.get('https://www.zhaopin.com/')
    #获取信息
    browse.find_element_by_id('KeyWord_kw2').send_keys('python')
    browse.find_element_by_id('JobLocation').send_keys('北京')
    #搜索点击
    browse.find_element_by_class_name('doSearch').click()
    if browse.page_source:
        html = browse.page_source
        get_data(browse,html)

def get_data(browse,html):
    html_all = re.compile('<a\sstyle="font-weight:\sbold".*?>(.*?)</a>',re.S)
    all = re.findall(html_all,html)
    for i in all:
        a = i.replace('<b>','').replace('</b>','')
        print(a)
        dict = {            'title':a
        }
        with open('c.json','a') as f:
            f.write(json.dumps(dict)+'\n')
    if  browse.page_source.find('a.next-page'):
        browse.find_element_by_class_name('pagesnum').send_keys(1)
        browse.find_element_by_xpath('.//li[@class="pagesDown-pos"]/a[@class="next-page"]').click()
        # time.sleep(5)
        get_data(browse,browse.page_source)
    else:
        print('没有啦')

def main():
    shousuo()

if __name__ == '__main__':
    main()
