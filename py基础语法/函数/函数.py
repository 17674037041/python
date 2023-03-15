# 程序创建@李宏宇
# 创建时间 ：2023/3/7

"""
1.abs(a)  求绝对值
2.max(...)   返回最大值
3.函数名是指向一个函数对象的引用,可以把函数名赋给一个变量,相当于给这个变量起别名
a = abs
a(-1)  输出1
4.空函数体内可以用pass用来作为占位符
5.函数多返回值实际返回的是一个元组 多个变量可以同事接收一个tuple,按位置赋值对应的值
6.函数执行完毕也没有return语句时,自动return None
7.参数类型检查
if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
8.函数的默认参数
 8.1.必选参数在前 默认参数在后(避免产生歧义)
 8.2.多个参数时,变化大的参数放在前面,变化小的参数放后面
 8.3.不按顺序提供部分默认参数时,需要把参数名写上
 8.4.默认参数必须指向不可变对象
9.可变参数  * 参数接收到的是一个tuple 可以传入任意个参数
10.list和tuple前面加一个*号,可以把list或者tuple的元素变为可变参数
11.关键字参数 :
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
12.五种参数可以自由组合 定义的先后顺序为:必选参数、默认参数、可变参数、命名关键字参数、关键字参数


(1)必选参数:跟在函数名括号内的为参数名,参数在调用函数时必须给函数传递指定数量的参数
(2)默认参数:参数名后使用=号给参数赋值之后参数拥有了默认值,以后在调用该参数时,不给默认参数赋值程序也不会报错
(3)可变参数:可变参数的定义是在参数前添加一个*号,可变参数在函数内被视为一个tuple .「该参数可不传参」
(4)关键字参数:关键字的意思是以dict作为数据类型将参数传递给函数,key:value 「该参数可不传参」
(5)命名关键字参数:命名关键字参数就是将dict的key提前定义,调用函数时传参只能传入已定义key的参数
"""

import math

# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
a = 123
s = hex(a)
print(s, type(s), type(a))


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax2+bx+c=0的两个解
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("参数类型错误")
    if not isinstance(b, (int, float)):
        raise TypeError("参数类型错误")
    if not isinstance(c, (int, float)):
        raise TypeError("参数类型错误")
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "此方程无解"
    else:
        x1 = (-b + math.sqrt(d)) / 2 * a
        x2 = (-b - math.sqrt(d)) / 2 * a
    return x1, x2


x1, x2 = quadratic(-1, 5, 6)
print(x1, "\n", x2)


def add_end(L = []):
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())


# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def mul(*number):  # 可变参数
    m = 1
    for x in number:
        m *= x
    return m


print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))


# 递归函数
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(10))


# 汉诺塔 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
# 然后打印出把所有盘子从A借助B移动到C的方法
def move(n, a, b, c):
    if n == 1:
        print(a, "->", c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(6, 'A', 'B', 'C')


def make_car(manufacturer, model, **args):
    print(f"manufacturer is {manufacturer},model is {model},and {args}")


car = make_car('subaru', 'outback', color = 'blue', tow_package = True)