import threading
import time
def download(url):
    print(url)
    #判断线程为前台线程还是后台线程
    print(threading.current_thread().name)
    time.sleep(2)

def main():
    starttime = time.time()
    
    task_list = ['url1','url2','url3','url4','url5']
    # for url in task_list:
    #     download(url)
    #存放当前的线程的对象
    thread_list = []
    for url in task_list:
        #创建一个线程(子线程) target当前线程要执行的任务,args传参数(固定写法)
        thread = threading.Thread(target=download,name='线程'+url,args=[url,])
        #False为前台线程，True为后台线程
        #thread.serDeamon(False)
        #启动线程
        thread.start()
        thread_list.append(thread)
        #方案一
        #thread.join()
    #子线程调用join(),子线程结束后主线程再结束
    #方案二
    for thread in thread_list:
        thread.join()

    print(threading.current_thread().name)

    endtime = time.time()
    print('耗时'+str(endtime-starttime))


if __name__ == '__main__':
    main()