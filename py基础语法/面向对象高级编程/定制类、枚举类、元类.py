# 程序创建@李宏宇
# 创建时间 ：2023/3/9

"""
1.定制类：
    1.1._str_返回用户看到的字符串
    1.2._repr_返回程序开发者看到的字符串  为调试服务的
    1.3.当直接敲变量的时候 可以让_str_等于_repr_  这样就和print()打印等同了
    1.4._iter_：返回一个迭代对象，for循环不断调用该迭代对象的_next_方法拿到循环的下一个值,
        直到遇到StopIteration错误时推出循环(raise StopIteration)
    1.5._getitem_：实现此方法，可以像list那样按照下标去除元素
    1.6._getattr_：调用不存在的方法时，会在此方法中寻找
        def __getattr__(self, attr):  # 返回一个属性
            if attr=='score':
                return 99

        def __getattr__(self, attr):  #返回一个函数
            if attr=='age':
                return lambda: 25
    1.7._call_：对实例进行调用就好比对一个函数进行调用，所以对象可以看成函数，函数可以看成对象，两者区别不大
        1.7.1.通过callable()函数，能判断一个对象是都是“可调用”对象
        1.7.2.类中定义_call_方法，可以调用实例对象

2.使用枚举类：可以用成员名车引用枚举常量，也可以直接根据value的值获得枚举常量


3.使用元类：???????不是很懂

"""



class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print(n)

a, b = 1, 1
for x in range(100):
    a, b = b, a + b
print(a)


class Stu:
    def __init__(self):
        self.name = "李宏宇"

    def __getattr__(self, item):
        if item == "age":
            return 23
        elif item == "address":
            return "广州天河棠下"

    def __call__(self, *args, **kwargs):
        print("正在对实例进行调用！{0}    {1}".format(args, kwargs))


st = Stu()
print(st.name)
print(st.age)
print(st.address)
print(st.k)
st("fds", 1, 2, 3, d = 'd')

# 枚举类
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 枚举练习
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
