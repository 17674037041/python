# 程序创建@李宏宇
# 创建时间 ：2023/3/7

"""
1.range(key)函数生成序列从0开始小于key的整数
2.for循环
3.while循环
4.break
5.continue
6.python不支持do_while循环
"""


# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

# 条件判断
def is_obesity(key):
    if key < 18.5:
        return "BMI为:%.1f,过轻" % key
    elif 18.5 <= key < 25:
        return "BMI为:%.1f,正常" % key
    elif 25 <= key < 28:
        return "BMI为:%.1f,过重" % key
    elif 28 <= key < 32:
        return "BMI为:%.1f,肥胖" % key
    else:
        "BMI为:%.1f,严重肥胖" % key


height = 1.68
weight = 58
bmi = weight / height ** 2
print(is_obesity(bmi))


# 循环
# 计算1~10000数之间的累加
# 1.for循环
def accumulation(key):
    sum = 0
    for num in range(key + 1):
        sum += num
    return sum


print(accumulation(100))


# 2.while循环
def accumulation1(key):
    sum = 0
    while key > 0:
        sum += key
        key -= 1
    return sum


print(accumulation1(100))
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
# 1.for循环
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print("hello,%s" % x)

# 2.while循环
len = len(L)
i = 0
while i < len:
    print("hello,", L[i])
    i += 1
