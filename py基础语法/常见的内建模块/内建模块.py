# 程序创建@李宏宇
# 创建时间 ：2023/3/14

"""
1.datetime：?????????
2.collections：Python内建的一个集合模块，提供了许多有用的集合类
    namedtuple、deque、defauldict(访问字典中的不存在的key的时候会抛出KeyError错误，
    此时可以用defaultdict返回一个默认值)、OrderedDict(保证dict是有序的)
3.argparse：??????????
4.base64：64位字符表示任意二进制数据的方法
5.struct：解决bytes和其他二进制数据的转换
6.hashlib：摘要算法
7.hmac：比hashlib更安全
8.itertools：操作迭代对象的函数
    8.1.itertools.count()：创建一个无限的迭代器，可根据第二个参数确定每次迭代的数值大小
    8.2.itertools.cycle()：序列无限重复下去
    8.3.itertools.repeat()：无限循环某个元素，可提供第二个参数限制重复的次数
    8.4.itertools.takewhile()：截取出一个有序的序列
    8.5.itertools.chain()：组合迭代对象，形成一个更大的迭代器
    8.6.itertools.groupby()：把迭代器中相邻的重复元素跳出来放在一起
9.contextlib：装饰器 with语句 上下文管理器
10.urlib： 提供一系列用于操作URL的功能
11.XML：
12.HTMLParse：
"""
import time
from functools import reduce

print("----hashlib----")
# # 第一题
# import hashlib
#
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
#
#
# def calc_md5(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     return md5.hexdigest()
#
#
# def login(user, password):
#     pwd = calc_md5(password)
#     if db[user] == pwd:
#         return True
#     return False
#
#
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')
#
#
# import hashlib, random
#
#
# def get_md5(s):
#     return hashlib.md5(s.encode('utf-8')).hexdigest()
#
#
# class User(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password = get_md5(password + self.salt)
#
#
# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
# }
#
#
# def login(username, password):
#     user = db[username]
#     return user.password == get_md5(password + user.salt)
#
#
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')


import itertools

# co = itertools.count(1) #无限迭代打印自然数
# for n in co:
#     print(n)

# cy=itertools.cycle('ABC') #无限重复打印ABC
# for c in cy:
#     print(c)

# re=itertools.repeat('A') #无限重复打印A，如有第二个参数则只打印制定的次数
# for r in re:
#     print(r)

# r=itertools.count(52,5)
# for i in r:
#     print(i)
#     time.sleep(1)


# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

x = filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5])  # filter()对序列中的每个元素筛选，获得新的序列
print(list(x))

print("----itertools----")


def pi(n):
    # 1.得到一个奇数序列并获取该序列的前N项
    oddn = itertools.takewhile(lambda x: x < 2 * n, itertools.count(1, 2))
    # 2.添加正负符号
    sym = itertools.cycle([1, -1])
    # 3.构造列表[4,-4/3,4/5,-4/7,……]
    oddn = map(lambda x: next(sym) * 4 / x, oddn)
    # 4.计算
    return reduce(lambda x, y: x + y, oddn)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

from contextlib import contextmanager

print("----contextlib----")


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()