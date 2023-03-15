# 程序创建@李宏宇
# 创建时间 ：2023/3/13

# https://www.liaoxuefeng.com/wiki/1016959663602400/1017639890281664  廖雪峰


"""
1.正则表示式是一种用来匹配字符串的，其设计思想是用一种描述的语言来给字符串定义一个规则，
    凡事符合规则的字符串，我们就认为它匹配了，否则，该字符串就是不合法的
2.csdn  https://blog.csdn.net/xuemoyao/article/details/8033138?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167875260816800211581437%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=167875260816800211581437&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-8033138-null-null.142^v73^insert_down3,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&spm=1018.2226.3001.4187
3.re模块提供正则表达式，常用的四个方法：match、search、findall
    3.1.re.match()：起始位置匹配一个模式，如果不是起始位置匹配成功的话，返回None    匹配单个字符
    3.2.re.search()：和re.match()类似  只不过是查找
    3.3.re.fandall()：寻找所有能匹配到的字符，并以泪飙的方式返回
        findall另一个属性re.S，把不同行看为一个整体，在整体中匹配
    3.4.python的数量词默认是贪婪的，总是尝试尽可能多的匹配更多的字符，使用？关闭贪婪模式



"""
import re

# re.match("匹配的正则",“要匹配的字符串”)
a = re.match('testas', 'testasdtest')
print(a)  # 返回一个匹配对象
print(a.group())  # 返回test，获取不到则报错
print(a.span())  # 返回匹配结果的位置，左闭右开区间
print(re.match('test', 'atestasdtest'))  # 返回None

print(re.match('\w', '23es 12testasdtest'))  # 返回none
print(re.match('\w\w\w', 'aA_3es 12testasdtest'))  # 返回none
print(re.match('\w\w\w', '\n12testasdtest'))  # 返回none

print(re.match('12[234]', '232s12testasdtest'))  # 因为开头的12没匹配上，所以直接返回none

print(re.match('.*d$', '2testaabcd'))  # 字符串必须以d结尾
print(re.match('.*c', '2testaabcd'))  # 字符串不是以c结尾，返回none

print(re.match('^2s', '2stoooabatestas'))  # 必须以2s开头

s = "this is number 234-235-22-423"
result = re.match(r"(.+)", s)
print(result.groups())

str="to=dddfdfa;kkk"
a=re.search(r'=(.*?);',str)
print(a.groups())
