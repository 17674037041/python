# 程序创建@李宏宇
# 创建时间 ：2023/3/8

"""
1.继承和多态：
    1.1.Python不支持多态，其本身就是一种多态语言，崇尚鸭子类型
    1.2.面向对象的各种方法：
        1.2.1.静态方法（@staticmethod）
        1.2.2.类方法是（@classmethod）：类方法只能访问类变量，不能访问实例变量
        1.2.3.属性方法（@property）：方法变成静态属性后调用不用加括号了
2.获取对象信息：
    2.1.总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”
    2.2.dir()：获得一个对象的所有属性和方法，其返回包含字符串的list
    2.3.getattr()：获取对象中的属性 可以给定default参数 当属性不存在时 返回默认参数
    2.4.setattr()：设置一个属性
    2.5.hasattr()：判断对象中有无某个属性
    2.6.只有在不知道对象信息的时候，我们才会去获取对象信息
3.实例属性和类属性：
    3.1.class中定义属性，这种属性就是类属性，归类所有，但是其所有实例都可以访问到
    3.2.实例属性和类属性具有相同名字时，实例属性会屏蔽掉类属性
    3.3.总结：
        3.3.1.实例属性属于各个实例所有，互不干扰
        3.3.2.类属性属于类所有，所有实例共享一个属性
"""


class Person(object):
    name = "李宏宇"

    def __init__(self, name):
        self.name = name

    @classmethod  # 把eat方法变为类方法
    def eat(self):
        print("%s is eating" % self.name)


d = Person("xiaoming")
d.eat()


# 练习
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1 # 类属性用类名访问 self访问的是实例属性


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
