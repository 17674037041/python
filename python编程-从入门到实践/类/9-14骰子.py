# 程序创建@李宏宇
# 创建时间 ：2023/3/15

from random import randint


class Die():
    i = 1  # 类属性 属于类 所有实例对象都拥有

    def __init__(self, sides = 6):
        self.sides = sides
        self.i = 1  # 实例属性 属于实例对象
        return None

    def roll_die(self):
        num = randint(1, self.sides)  # 随机面数大小
        print(f"这是一个{self.sides}面的骰子，第{self.i}次随机到的面数大小为：{num}")
        self.i += 1
        return None


t1 = Die()
for i in range(randint(10, 10)):  # 6面骰子抛十次
    t1.roll_die()

t2 = Die(10)
for i in range(10):  # 10面骰子抛10次
    t2.roll_die()

t3 = Die(20)
for i in range(10):  # 20面骰子抛10次
    t3.roll_die()
