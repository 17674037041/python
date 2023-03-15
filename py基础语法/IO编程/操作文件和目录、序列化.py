# 程序创建@李宏宇
# 创建时间 ：2023/3/10

"""
1.操作文件和目录：CSDN  https://blog.csdn.net/m0_63794226/article/details/126435297?ops_request_misc=&request_id=&biz_id=102&utm_term=python%E6%93%8D%E4%BD%9C%E6%96%87%E4%BB%B6%E5%92%8C%E7%9B%AE%E5%BD%95&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-126435297.142^v73^insert_down3,201^v4^add_ask,239^v2^insert_chatgpt&spm=1018.2226.3001.4187
2.序列化：把对象转化为可传输的二进制流数据  反序列化：把二进制流数据转化为对象
    2.1.


"""
import json
import keyword
import pickle

# f = open('E:/IO编程/1.txt', 'r', encoding = 'utf-8')


# print(f.read())

import pickle

d = dict(name = 'Bob', age = 20, score = 88)
print(pickle.dumps(d))

f = open('E:/IO编程/1.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

obj = dict(name = '小明', age = 20)
s = json.dumps(obj, ensure_ascii = True)
print(s)
s = json.dumps(obj, ensure_ascii = False)
print(s)

print(keyword.kwlist)