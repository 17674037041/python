# 程序创建@李宏宇
# 创建时间 ：2023/3/14

"""
1.使用场景：数据库链接、Socket(套接字)
2.

"""
from random import randint

def Singleton(cls):
    instance = {}

    def _singleton_wrapper(*args, **kargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        return instance[cls]

    return _singleton_wrapper


@Singleton
class SingletonTest(object):
    def __init__(self, name):
        self.name = name


slt_1 = SingletonTest('第1次创建')
print(slt_1.name)
slt_2 = SingletonTest('第2次创建')
print(slt_1.name, slt_2.name)

print(slt_1 is slt_2)

from threading import RLock


class Singleton(object):
    single_lock = RLock()  # 上锁

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        with Singleton.single_lock:
            if not hasattr(Singleton, "_instance"):
                Singleton._instance = object.__new__(cls)

        return Singleton._instance


single_1 = Singleton('第1次创建')
single_2 = Singleton('第2次创建')

print(single_1.name, single_2.name)  # 第2次

