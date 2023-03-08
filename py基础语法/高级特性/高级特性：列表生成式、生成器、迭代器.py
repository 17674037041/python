# 程序创建@李宏宇
# 创建时间 ：2023/3/7

"""
1.列表生成式：
    1.1.[x * x for x in range(1, 11)]
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        要生成的元素x*x放到前面，后面跟for循环
    1.2.x for x in range(1, 11) if x % 2 == 0 跟在for后面的if是一个筛选条件，不能带else
    1.3.x if x % 2 == 0 else -x for x in range(1, 11) 跟在for前面的部分是一个表达式，
        必须根据x计算出一个结果，所以必须带else
2.生成器：
    2.1.在Python中，这种一边循环一边计算的机制，称为生成器：generator
    2.2.generator保存的是算法，每次调用next(g),就计算g得下一个元素的值，直到计算到最后一个元素
    2.3.如果一个函数定义中包含yield关键字，那么这个函数就不在是一个普通函数，而是一个generator函数
    2.4.调用generator函数时，首先生成generator对象---->然后用next()函数不断获得下一个返回值
    2.5.调用generator函数会创建一个generator对象，多次调用会创建多个相互独立的generator
    2.6.把列表生成式中的[]改成()，就创建了一个generator
3.迭代器：
    3.1.可以直接作用于for循环的数据类型有:
        3.1.1.集合数据类型：list、tuple、dict、set、str等
        3.1.2.generator：包括生成器和带yield的generator function
        3.1.3.这些直接作用于for循环的对象统称为可迭代对象：Iterable
    3.2.可以直接作用于for循环的对象统称为可迭代对象：Iterable,
        可以使用isinstance()判断一个对象是否是Iterable对象
    3.3.可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator,
        可以使用isinstance()判断一个对象是否是Iterator对象
    3.4.生成器都是Iterator对象，但list、dict、str不是，可以使用iter()函数把他们变成Iterator
        >>> isinstance(iter([]), Iterator)
        True
        >>> isinstance(iter('abc'), Iterator)
        True
"""

# 通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L1 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L1)
if L1 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


# 斐波那契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# fib(6)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles():
    L = [1]
    while 1:
        yield L
        # 列表生成器
        L = [L[i] + L[i - 1] if i != 0 and i != len(L) else 1 for i in range(len(L) + 1)]
    return 'None'


n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')



def add(a,b):
    return a*b

print(add(5,6))