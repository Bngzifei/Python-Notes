"""
创建子进程的时候, Python 解释器会再次导入执行当前的py文件


不要把代码写成全局,否则在创建子进程的时候会再次将创建一次 即使用if __name__=='main':的形式

多进程的代码必须规范 对应好子进程自己执行的代码.

Process(target=test()),如果给test加了(),就是在主进程里面去执行test函数了,这样就不会有子进程的事情了,违背了创建子进程的初衷.
我们的目的就是让子进程去执行test()函数,实现多任务的目的.

模块sys:系统环境变量,临时的

为什么进程之间是独立的地址空间  --> 因为进程是os资源分配的单位.

要求稳定,不在意资源消耗:进程,否则就是线程

进程池:节约了进程的创建,销毁的资源开销

"""
