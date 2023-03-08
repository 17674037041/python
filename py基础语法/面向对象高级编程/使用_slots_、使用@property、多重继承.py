# 程序创建@李宏宇
# 创建时间 ：2023/3/8

"""
1.使用_slots_:
    1.1.创建一个class的实例后，我们可以给该实例绑定任何属性和方法

2.使用@property

3.多重继承
"""


class Student:
    pass


s = Student()


def set(self, score):
    self.score = score


Student.set = set

s.set(100)
print(s.score)



