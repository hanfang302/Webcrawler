#https://www.qiushibaike.com/8hr/page/2/
#多线程
import threading
#请求模块
import requests
#数据存储
import json
#数据解析
from lxml import etree
#队列
import queue

class THreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        # 继承父类方法
        #多继承方法
        super(THreadCrawl,self).__init__()
        #单继承一下方法
        #super().__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        #print(self.threadName)
    #重写父类方法（run方法）是为了发起请求，拿到响应结果
    def run(self):
        BOOL = self.pageQueue.empty()
        #while not self.pageQueue.empty()
        while BOOL:
            print('开启'+self.threadName)
            #从任务队列里那页码(爬取一个队列)
            page = self.pageQueue.get()
            fullur = 'https://www.qiushibaike.com/8hr/page/'+str(page)+'/'
            #拼接发起请求
            response = requests.get(fullur,headers=self.headers)
            #打印结果状态码
            print(response.status_code)
            if response.status_code == 200:
                self.dataQueue.put(response.text)
            #print(self.dataQueue.type(self.dataQueue))
            print('run起来')

class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue):
        super(ThreadParse,self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue

    def run(self):
        #解析获取的数据
        #队列
        while not self.dataQueue.empty():
            html = self.dataQueue.get()
            print('获取到数据')
            self.parse(html)

    def parse(self.html):
        #解析数据
        parse_data = etree.HTML(html)
        content = parse_data.xpath('//div[@id="content-left"]/div')
        for sub_div in contentList:
            title = sub_div.xpath('.//h2/text()')[0]
            content = sub_div.xpath('.//div[@class="content"]/span/text()')
            #print(title)
            dict = {
                'title':title,
                'content':content,
            }

            peint(dict)
            with open('duanzi.json','a') as f:
                #ensure_ascii这里默认是Ture,是ascil编码
                f.write(json.dumps(dict,ensure_ascii=False) + '\n')

#主线程
def main():
    #首先创建一个任务列队
    pageQueue = queue.Queue(30)
    #构造数据的队列
    dataQueue = queue.Queue()
    #把页码放进去
    for i in range(1,14):
    #往任务列队中存要请求的代码
        pageQueue.put(i)

    #创建线程来获取网页的内容
    crawlTheradNames = ['crawlone','crawltwo','crawlthree']
    threadcreaws = []
    for threadName in crawlTheradNames:
        thread = THreadCrawl(threadName=threadName,pageQueue=pageQueue,dataQueue=dataQueue)
        thread.start()
        threadcreaws.append(thread)
        #thread.join()
   
    for thread in threadcreaws:
        thread.join()

    #创建一个锁，为同一个资源，某一时刻只被一个线程执行
    lock = threading.Lock()
    #创建解析线程
    parseThreadNames = ['Korean','French','German']
    threadParse = []
    for threadName in parseThreadNames:
        parsethread = ThreadParse(threadName,dataQueue)
        parsethread.start()
        threadParse.append(parsethread)

    for thread in threadParse:
        thread.join()



print(threading.current_thread().name)
if __name__ == "__main__":
    main()