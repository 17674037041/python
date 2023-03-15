# 程序创建@李宏宇
# 创建时间 ：2023/3/10

"""
1.文件读写：CSDN  https://blog.csdn.net/qq_41340258/article/details/124148415?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167843012416782427447731%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=167843012416782427447731&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-124148415-null-null.142^v73^insert_down3,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=python%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99&spm=1018.2226.3001.4187
    1.1.读文件：open()函数，传入文件名和标识符  f = open('/Users/michael/test.txt', 'r') r表示读
    1.2.文件不存在，抛出IOError异常
    1.3.UnicodeDecodeError: ‘gbk’ codec can’t decode byte：
        python的open方法默认编码取决于平台，如果平台是windos，编码默认是gbk，
        如果文件时utf-8编码，就会报这个错误
    1.4.文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间打开
        的文件数量也是有限的
    1.5.f.read()：一次性读取文件全部内容
    1.6.f.readline()：每次读取一行
    1.7.f.readlines()：一次读取所有内容并按行返回list
    1.8.读取二进制文件像图片、视频等等，用“rb”
    1.9.with语句自动调用close()：
        with open('/path/to/file', 'r') as f:
            print(f.read())
2.StringIO和ByteslIO：
    2.1.BytesIO操作二进制数据，StringIO操作str
    2.2.文件标志位：
        写入、

"""
import pip
import requests as requests

# 文件读写
f = open('E:/IO编程/1.py', 'r', encoding = 'utf-8')  # 打开文件
ff = f.read()  # 读取文件
print(ff)  # 打印文件内容
f.close()  # 关闭文件

# 二进制文件
f = open("E:/IO编程/1.jpg", 'rb')
ff = f.read()
# print(ff)
f.close()

# stringIO和BytesIO
from io import StringIO, BytesIO

f = StringIO()
print(f.write('hello'))

response = requests.get('https://img.zcool.cn/community/0170cb554b9200000001bf723782e6.jpg@1280w_1l_2o_100sh.jpg')
type(response.content)
bytes
img = BytesIO(response.content)

from PIL import Image

pic = Image.open(img)

print(pic.format)
