#封装的线程池
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import requests

def get_data(url):
    print('开始下载',url)
    time.sleep(2)

    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0)'
    }
    response = requests.get(url,headers=header)
    print(response.status_code)
    if response.status_code ==200:
        return response.status_code,url
    #return url

def done(future):
    #线程池执行设定任务结束后结果参数
    print('下载完了')
    response = future.result()
    print(response)
#如何定义一个线程池(参数为线程量)
pool = ThreadPoolExecutor(1)
#如何提交任务给线程池
urls = {
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
}
# for url in urls:
#     #submit将我们执行的任务给这个线程池
#     a = pool.submit(fn=get_data,(url,))
#     #給线程池设置任务之后可以设置 一个回调函数，作用：当我们某个任务执行完毕之后，就会回调函数
#     a.add_done_callback(done)

for url in urls:
    # submit:表示将我们需要执行的任务给这个线程池，
    a = pool.submit(get_data,url)
    # 给线程池设置任务之后，可以设置一个回调偶数,
    # 作用是：当我们某个任务执行完毕之后，就会回调你设置的回调函数  
    a.add_done_callback(done)
   

pool.shutdown(True)
#如何让主线程等待子线程
print(threading.current_thread().name)

