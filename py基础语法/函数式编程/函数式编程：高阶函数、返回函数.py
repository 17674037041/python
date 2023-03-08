# 程序创建@李宏宇
# 创建时间 ：2023/3/8
"""
1.高阶函数：函数的参数为另一个函数，这种函数称为高阶函数
    1.1.编写高阶函数，就是让函数的参数可以接收别的函数
    1.2.map/reduce：map的函数定义：map(函数, list)
        1.2.1.map()方法会将一个函数f(x)映射到序列的每一个元素上，生成新序列，包含所有函数返回值
        1.2.2.Reduce()函数在迭代序列的过程中，首先把前两个元素（只能两个元素）传给函数，函数加工后，然后把得到的
            结果和第三个元素作为两个元个参数传给函数参数，依此类推
    1.3.filter：filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
        然后根据返回值是True还是False决定保留还是丢弃该元素。
    1.4.sorted：排序算法
        1.4.1.用sorted()排序的关键在于实现一个映射函数
2.返回函数：函数作为返回值
    2.1.返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
    2.2.使用闭包就是内层函数引用了外层函数的局部变量
    2.3.使用闭包时，对外层变量赋值前，需要先使用nonlocal声明变量不是当前函数的局部变量



"""
from functools import reduce
from operator import itemgetter


# 高阶函数
def add(x, y, f):
    return f(x) + f(y)


print(add(5, 9, abs))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# 第一题
def normalize(name):
    result = ''
    n = 0
    for st in name:
        if n == 0:
            result += st.upper()
            n = 1
        else:
            result += st.lower()
    return result


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# 第二题
def prod(L):
    def mul(x, y):
        return x * y

    return reduce(lambda x, y: x * y, L)  # lambda表达式


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 第三题
def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    n = s.index('.')
    print("n=", n)
    s1 = list(map(char2num, s[:n]))
    s2 = list(map(char2num, s[n + 1:]))
    return reduce(fn, s1) + reduce(fn, s2) / 10 ** len(s2)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# filter
def is_palindrome(n):
    n = str(n)
    boo = True
    p1 = 0
    p2 = len(n) - 1
    while p1 <= p2:
        if n[p1] == n[p2]:
            p1 += 1
            p2 -= 1
            boo = True
        else:
            boo = False
            return boo
    return boo


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print(sorted([36, 5, -12, 9, -21], key = abs))
[5, 9, -12, -21, 36]


# sorted
# 第一题
def by_name(t):
    return t[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key = by_name, reverse = True)
print(L2)


def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x

    return fn


f = inc()
print(f())  # 1
print(f())  # 2


# 返回函数
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x = 0

    def counter():
        nonlocal x
        x += 1
        return x

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
