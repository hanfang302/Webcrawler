#多线程
import threading
#target=执行函数；name=线程名称；args=执行函数的参数，是元组(元组只有一个元素的时候为1，)
sub_thread = threading.Thread(target=done,name='1')
#启动线程
sub_thread.start()
#True后台线程，无论子线程是否结束，主线程一旦结束，所有子线程全部结束
#False一般回合join配合使用，前台线程，主线程必须等待子线程结束才能结束
sub_thread.setDaemon(False)
sub_thread.join()

#打印线程名称
print(threading.current_thread().name)

#重写线程，为了重写run方法，添加自己需要的功能
class ThreadCustom(threading.Thread):
    def __init__(self,参数1，参数2...)
        super(ThreadCustom,self).__init__
        self.参数1 = 参数1
        self.参数2 = 参数2

    def run(seelf):
        #写自己需要实现的功能