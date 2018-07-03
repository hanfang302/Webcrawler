#import urllib.request,urllib.parse
from urllib.request import Request,urlopen
import re

#构造请求
#req = urllib.request.Request(url,headers)
# response = urllib.request.urlopen(req)

req = Request(url,headers)

def get_page_data(startpage,endpage,url):
    for i in range(startpage,endpage+1):
        print(i)
        fullurl = url + 'list%s.html'%i
        #构建完完整的url
        #print(fullurl)
        #调用方法发起请求
        send_request(fullurl)

def send_request(fullurl):
    print(fullurl)
    #构造请求
    req = Request(fullurl)
    #response = urlopen(req)
    html = response.read().decode('gbk')
    #print(response.read().decode('gbk'))
    #图片地址
    #<img src=''
    #re.S可以匹配换行
    compile1 = re.compile('<img.*?src="(.*?).*?<p>(.*?)</p>">',re.S)
    result_images = re.findall(compile1,html)
    print(result_images)
    compile2 = re.compile('<img.*?class="lazy".*?data-original="(.*?)".*?<p>(.*?)</p>',re.S)
    result_images = re.findall(compile1,html)+re.findall(compile2,html)

    for info in result_images:
        inftext = ':'.join(info)
        print(infotext)
    with open('xiaohua.txt','w') as f:
        f.write(infotext+'\n')


def download_image(filename):


#def main():

    if __name__=='__main__':
        startpage = input('请输入起始页')
        endpage = input('请输入终止页')
        print(int(startpage),int(endpage))
        url('http://www.yggk.net/xiaohua/xiaohua/')