# 程序创建@李宏宇
# 创建时间 ：2023/3/8

"""
1.匿名函数：匿名函数lambda x: x * x
    1.1.匿名函数有个限制，就是只能有一个表达式，不必担心函数名冲突
2.装饰器：定义一个函数，该函数是用来为其他函数添加额外功能的（拓展原来函数功能的一种函数）
    2.1.应用场景：插入日志、性能检测、事务处理、缓存、权限校验等
    2.2.把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
3.偏函数：可为原函数中的参数拟定一个初始值，并将带着初始值的原函数返回
"""

# 匿名函数
f = lambda n: n % 2 == 1

L = list(filter(f, range(1, 20)))
print(L)

# 为函数添加一个统计运行时长的功能
import time
import threading


def how_much_time(func):
    def inner():
        t_start = time.time()
        func()
        t_end = time.time()
        print("一共花费了{0}秒时间".format(t_end - t_start, ))

    return inner


@how_much_time
# @how_much_time等价于sleep_5s = how_much_time(sleep_5s)
def sleep_5s():
    time.sleep(5)
    print("%d秒结束了" % (5,))


@how_much_time
def sleep_6s():
    time.sleep(6)
    print("%d秒结束了" % (6,))


t1 = threading.Thread(target = sleep_5s)
t2 = threading.Thread(target = sleep_6s)
t1.start()
t2.start()


def mylog(type):
    def decorator(func):
        def infunc(*args, **kwargs):
            if type == "文件":
                print("文件中：日志记录")
            else:
                print("控制台：日志记录")
            return func(*args, **kwargs)

        return infunc

    return decorator


def fun2(a, b):
    print("使用功能2", a, b)


fun2 = mylog("文件")(fun2)
fun2(100, 200)


# 装饰器
def metric(fn):
    def ff(*args, **kwargs):
        start = time.time()  # 开始时间
        res = fn(*args, **kwargs)
        end = time.time()  # 结束时间
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return res

    return ff


# 测试
@metric    # fast=metric(fast)
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print("测试成功!")
