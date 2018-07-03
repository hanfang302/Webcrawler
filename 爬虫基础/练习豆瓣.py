
# #'ascii' codec can't encode characters in position 35-36: ordinal not in range(128)
import urllib.request
#对数据解析
from urllib import parse
#保证HTTP的通道安全
import ssl
#定义一个getajax函数
def getajax():
    url = 'https://movie.douban.com/j/search_subjects?'
    #https://movie.douban/j/search_subjects?page_limit=20&page_start=40&sort=recommend&tag=%E9%9F%A9%E5%89%A7&type=tv
    #变动参数
    data = {
        #页面限制
        'page_limit':'20',
        #页面开始
        'page_start':'40',
        'sort':'recommend',
        'tag':'韩剧',
        'type':'tv',
    }
    #转换成url编码格式（字符串，这里不是Post请求不用转换成字节，直接拼接在地址上）
    data = parse.urlencode(data)
    url = url+data
    print('urlencode转换后:'+data,'完整的get请求地址为：'+url)
    #设置这个参数表示我们可以忽略https的请求协议
    requestContext = ssl._create_unverified_context()
    #request对象作为urlopen()方法的参数，发送给服务器并接受响应
    response = urllib.request.urlopen(url,context=requestContext)
    #打印结果可以知道获取结果为一个字符串
    result = response.read()
    #查看返回的结果类型
    print(type(response))
    #返回结果
    print(result)
    print(response.url)
    print(type(dict))
    print(dict)

if __name__ == '__main__':
    getajax()