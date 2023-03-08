# 程序创建@李宏宇
# 创建时间 ：2023/3/7

"""
1.切片：
切片操作的基本表达式:object[start:end:step] 开始位置 结束位置 步长
开始位置：没有值得话从头开始
结束位置：没有给定值得话表示切割到结束为止
步长：默认取1 步长决定切得方向 为正则从左到右 为负则从右往左
2.判断是否可迭代？：通过collections.abc模块的Iterable类型判断
引入模块 from collections.abc import Iterable
  2.1.isinstance('abc', Iterable) # str是否可迭代
  2.2.isinstance([1,2,3], Iterable) # list是否可迭代
  2.3.isinstance(123, Iterable) # 整数是否可迭代

"""


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    if s == '':
        return None
    while len(s) != 0 and s[0] == ' ':  # 处理首部
        s = s[1:]
    if len(s) == 0:
        return None
    while s[-1] == ' ':
        s = s[:-1]
    return s


# for x in range(10):
#     st = input("请输入一个字符串：")
#     print(st)
#     print(trim(st))


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L) == 0:
        return None, None

    max = L[0]  # 最大值
    min = L[0]  # 最小值
    for x in L:
        if max < x:
            max = x
        if min > x:
            min = x
    return min, max


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
