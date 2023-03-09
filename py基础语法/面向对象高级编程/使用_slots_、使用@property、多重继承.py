# 程序创建@李宏宇
# 创建时间 ：2023/3/8

"""
1.使用_slots_:
    1.1.创建一个class的实例后，我们可以给该实例绑定任何属性和方法
    1.2._slots_变量，用以限制class添加的属性：
        class Student(object):
            __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
    1.3._slots_定义的属性仅对当前类实例起作用，对继承的子类是不起作用
    1.4.当在子类中也定义_slots_时，子类就能定义本身及其父类身上允许的属性
2.使用@property：
    2.1.@property-》get   函数名.setter-》set

3.多重继承：
    3.1.Mixln：目的是给一个类增加多个功能，可以更好的看出继承关系
"""


class Student:
    pass


s = Student()


def set(self, score):
    self.score = score


Student.set = set

s.set(100)
print(s.score)


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60
print(s.score)


# 2.@property练习
class Screen(object):

    def __int__(self, width = 0, height = 0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
