# coding=utf-8
"""
@project : python_work
@author  : zhangbaoquan
#@file   : BAdvDemo1.py
#@ide    : PyCharm
#@time   : 2020-10-11 22:11:18
@desc    : 进阶语法练习：函数、类、文件和异常

"""
# 导入整个模块，这个还需要模块名 . 方法
import demoUtil

# 导入模块里的摸个方法（可以直接使用）
from demoUtil import make_printDiv

# * 导入该模块下的所有方法，更爽
from demoUtil import *


def greet(name):
    print("hello python" + ' : ' + name)


def plus(a, b):
    return a + b


# name3 设置有默认值，因此可以不传，这个语法kotlin也有
def printName(name1, name2, name3=''):
    print(name1 + '、' + name2 + '、' + name3)


# greet('haha')
# # print(plus(1, 2))
# printName('haha', 'lala')
# printName('haha', 'lala', 'kaka')

# 传递任意数量的实参，使用* 将接收到的所有值全部封装到一个元组中,Java也支持这个特性
def make_print(*tips):
    print(tips)


# 使用** 可以传递任意数量的键值对，但我个人觉得这个功能很鸡肋
def make_print_list(*tips, **tips2):
    print(tips)
    print(tips2)


# make_print(1)
# make_print(1, 2)

# 注意，这里的key 不要加''
# make_print_list(1, kaka='aoa', lala='jiji')

# demoUtil.make_printPlus(1, 2)
#
# make_printDiv(4, 2)
#
# make_printMinus(5, 3)


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """ 模拟小狗坐下"""
        print(self.name.title() + " now sit")


# 类的继承
class BlackDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def go(self):
        print("go")


# my_dog = Dog('lala', 2)
# print(my_dog.age)
# my_dog.sit()

# hd = BlackDog('lala', 2)
# hd.sit()
# hd.go()

# 导入car的Python文件，引入里面的Car类
# from car import Car
# mCar = Car()
# mCar.stop()

# 这个是导入整个car 文件下的所有类，只是需要文件名.类
# import car
#
#
# mCar = car.Car()
# mCar.stop()

from collections import OrderedDict

# 使用OrderedDict 可以保证字典添加的顺序性（默认是无序的） OrderedDict 是python 标准库里的
# lanage = OrderedDict()
#
# lanage['lala'] = 'hehe'
# lanage['hah'] = 'lili'
#
# for a,b in lanage.items():
#     print(a + ":" + b)

# 不使用标准库
# lanage = {}
# lanage['lala'] = 'hehe'
# lanage['hah'] = 'lili'
#
# for a,b in lanage.items():
#     print(a + ":" + b)

# from random import randint
#
# # 产生随机数
# x = randint(1,6)
# print(x)

# 读文件, open 是打开文件，with 是将文件内容存储在 声明的txt  对象中
# file_path = '/Users/zhangbaoquan/work/MyProject/python_work/PythonStudy/file/bug.txt'
# with open(file_path) as txt:
#     contents = txt.read()
#     print(contents)

# 也可以逐行读取,python 默认使用将内容解读为字符串
# with open(file_path) as txt:
#     for line in txt:
#         print(line.strip())

# 字符串截取：
# str = "jjijijllllll"
# print(str[:5]+'...')

# file_path2 = '/Users/zhangbaoquan/work/MyProject/python_work/PythonStudy/file/bug2.txt'
file_path = '/Users/zhangbaoquan/work/MyProject/python_work/PythonStudy/file/novel.txt'
json_path = '/Users/zhangbaoquan/work/MyProject/python_work/PythonStudy/file/data.json'
json_path2 = '/Users/zhangbaoquan/work/MyProject/python_work/PythonStudy/file/data2.json'
# 写文件，w 会将之前的文件里的内容清空
# with open(file_path2, 'w') as text:
#     text.write('haha')

# 写文件， a 是在原文件里的内容追加
# with open(file_path2, 'a') as txt:
#     txt.write('\n' + "huhu")

# 处理异常
# try:
#     print(6)
#     print(5 / 0)
# except ZeroDivisionError:
#     print('error')
# else:
#     """仅在try 里执行成功后，才会执行，有一句异常都不行"""
#     print('haha')
# print('success')

# 分析文本

# try:
#     with open(file_path) as txt:
#         content = txt.read()
# except FileNotFoundError:
#     print('error')
# else:
#     """计算文件中有多少单词"""
#     """这里是将文件里的字符串拆成一个个单词，存储在一个列表中words"""
#     words = content.split()
#     # print(words)
#     print("单词数："+str(len(words)))

# line = "row,roo,row"
# # 表示输出当前字符串里某一个字符出现了几次
# print(str(line.count('row')))

# 使用json 存储数据
import json

# 打开json 文件，然后将列表写入文件中
# nub = [1, 2, 3]
# with open(json_path2, 'w') as js:
#     """ 调用json库，写json数据"""
#     json.dump(nub, js)

# 输出json文件的内容
# with open(json_path) as js:
#     txt = json.load(js)
#     print(txt)

# print(txt)

import os

# 判断一个目录是否存在
# status = os.path.exists(json_path2)
# print(status)

focus_path = '/Users/zhangbaoquan/work/MyProject/python_work/PythonStudy/file2/'
status = os.path.exists(focus_path)
print(status)
# 创建文件夹
if status != True:
   os.mkdir(focus_path)
   print("创建文件夹")
else:
    print("文件夹已经存在")

# 在文件夹下创建任意一个文件
txt_path = focus_path + "haha2.html"
# 直接打开一个文件，如果文件不存在则创建文件
open(txt_path,'w')

# 获取文件大小
size = os.path.getsize(json_path)
print(size)