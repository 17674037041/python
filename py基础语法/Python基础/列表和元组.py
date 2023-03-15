# 程序创建@李宏宇
# 创建时间 ：2023/3/7

from copy import deepcopy  # 深拷贝

s1 = 72
s2 = 85
r = (s2 - s1) / s2 * 100  # 百分比
print("{0}成绩提升了{1:.1f}%".format("小明", r))

'''
Python中的空值：None
1.元组tuple()不可变 列表list[]可变
2.python内置的有序集合
3.t = (1)，不是元组，这种情况默认为1  
注：只有一个元素的tuple定义时必须加一个逗号，来消除歧义

tuple中的操作方法
count() 

list中的操作方法 
1.append() 列表尾部添加元素
2.extend() 添加列表到另一个列表的尾部 //合并列表 *合并以及+号合并
3.pop() 默认移除最后一个元素，可移除指定元素（pop方法返回移除的元素）
4.remove() 移除列表中存在的元素 没有返回值
5.def关键字删除列表中的元素
6.in 判断元素是否在列表中 lst1 = [1,2] print(1 in lst1) # true
7.列表的操作符只支持+和*  +连接两个列表 *列表元素重复次数
8.count() 列表中某个元素的数量
9.reverse() 列表元素逆置
10.
'''

lst2 = [['hello', 'world'], [12, 'abc'], ['冰箱', '空调']]
lst3 = [1, 2, 3]
# for t1 in lst2:
#     print(t1)

lst2.remove([12, 'abc'])
print(lst2)

del lst2[0]
print(lst2)

# 深拷贝
lst = ['你好', ['hello', 'world'], [12, 'abc']]
# 列表的copy方法只能实现浅copy
copy1 = deepcopy(lst)
copy1[1][0] = 3
print(lst)  # ['你好', ['hello', 'world'], [12, 'abc']]
print(copy1)  # ['你好', [3, 'world'], [12, 'abc']]

a = list(range(1, 20, 3))
print(a)
print(a[:3])

