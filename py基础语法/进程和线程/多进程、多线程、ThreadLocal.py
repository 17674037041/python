# 程序创建@李宏宇
# 创建时间 ：2023/3/13

"""
多任务的实现有三种实现：
    1.多进程模式
    2.多线程模式
    3.多进程+多线程模式


1.多进程：

2.多线程：
    2.1.多任务可由多进程完成，也可以由一个进程内的多线程完成
    2.2.启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
    2.3.任何一个进程默认启动一个线程，称为主线程，其又可以开启新线程
    2.4.threading模块中的current_thread()函数，它永远返回当前线程的实例
    2.5.主线程实例名字叫MainThread，子线程创建时指定
    2.6.高级语言的一条语句在CPU执行时是若干条语句，
        balance = balance + n =》 x = balance + n; balance = x # 先存入临时变量，后赋值给目标值
    2.7.Pyhton解释器由于设计时有GIL全局锁，导致了多线程无法利用多核
3.ThreadLocal：

"""
# from multiprocessing import Process
# from multiprocessing import Pool
# import os, time, random
#
# import os
#
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':  # 此模块被导入时不会执行
#     print('Parent process %s.' % os.getpid())
#     p = Process(target = run_proc, args = ('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(5)
#     for i in range(5):
#         p.apply_async(long_time_task, args = (i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

import time, threading

# # 多线程
# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target = loop, name = "李宏宇")
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# 假定这是你的银行存款:

balance = 0


# 多线程共享同一变量balance
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(200000):
        change_it(n)


t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# ThreadLocal
# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target = process_thread, args = ('李宏宇',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('黄子洁',), name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
