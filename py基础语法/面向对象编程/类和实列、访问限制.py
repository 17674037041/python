# 程序创建@李宏宇
# 创建时间 ：2023/3/8

"""
1.类和实例：类是抽象的概念，实例是根据类创建出来的一个个具体的”对象“
    1.1.定义类是通过class关键字
2.访问限制：属性的名称前加上两个下划线__，内部属性不能被访问
    2.1.变量名类似__xxx__，双下划线开头，双下划线结尾的，是特殊变量，可以直接访问
    2.2.一个下划线开头的实例变量，外部可以访问，但是按照约定俗成的规定，不建议这样做
"""


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score


l = Student("李宏宇", 90)
ll = Student("黄子洁", 99)
print(l.get_name(), "   ", l.get_grade())
print(ll.get_name(), "   ", ll.get_grade())

# 练习
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
