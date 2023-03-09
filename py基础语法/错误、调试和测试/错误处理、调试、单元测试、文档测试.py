# 程序创建@李宏宇
# 创建时间 ：2023/3/9

"""
1.错误处理：try----except

2.调试：
    2.1.assert  断言
    2.2.logging

3.单元测试：

4.文档测试：doctest模块可以直接提取注释中的代码并执行测试

"""

from functools import reduce


def str2num(s):
    if s.find('.') == -1:
        return int(s)
    else:
        return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'  # 断言失败 会执行
    return 10 / n


def main():
    foo(1)


main()


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


d = Dict(a = 1, b = 2)
print(d['a'])
print(d.a)


# 文档测试
def fact(n):
    """
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    """
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
