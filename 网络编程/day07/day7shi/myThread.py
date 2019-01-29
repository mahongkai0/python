from threading import Thread
from time import sleep,ctime

##自定义线程

class MyThread(Thread):
    def __init__(self,target,args= (),kwargs={},name = 'pedu'):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.name = name
 
    
    def run(self):
        self.target(*self.args,**self.kwargs)

 
#测试函数
def player(sec,song):
    for i in range(2):
        print("playing %s:%s" % (song,ctime()))
        sleep(sec)

t = MyThread(target=player,args=(3,),kwargs={'song':'凉凉'},name='Tedu') 
t.start()
t.join()

# 步骤：   1.继承Thread
#         2.编写__init__添加属性 加载父类init
#         3.重写run方法

#         使用：使用自己的类创建线程对象 调用start启动线程 则自动执行run方法

