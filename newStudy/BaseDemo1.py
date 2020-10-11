# coding=utf-8
"""
@project : python_work
@author  : zhangbaoquan
#@file   : BaseDemo1.py
#@ide    : PyCharm
#@time   : 2020-10-11 15:51:52
@desc    : 基础练习1

包含一些基础的语法
"""

message = " hello python"
msg = "good ! "
age = 27
# print(message)

# title 方法让字符串首字母大写,lower 让首字母小写
# print(message.title())
# print(message.lower())

# 和Java一样
# print(message + "\n"+msg)

# 删除前面的空格
# print(message.lstrip())
# 将数字转成字符串
# print(str(27))

# 列表 相当于数组
arry = ['haha', 'kaka', 'lala']
# print(arry[0])
# print(arry[-1])
# arry[1] = 'hehe'
# arry.append('zaza')
# # 插入指定位置
# arry.insert(1,'nana')
# print(arry)

# str = arry[0]
# print(str)
# pop 是取出，相当于直接删除列表里的值
# str = arry.pop(0)
# print(arry)
# remove 也是删除
# arry.remove('haha')
arry.insert(0, 'zaza')
# 按首字母排序sort，也支持倒序reverse
# arry.sort()
# print(arry)
# arry.reverse()
# print(arry)
# sorted 相当于临时排序，没有改变原始列表的顺序
# print(sorted(arry))
# print(arry)
# 计算列表长度 len()
# print(len(arry))

# 遍历列表
# for str in arry:
#     print(str)

# 使用list 创建一个数字列表，在使用range（）方法创建一个数据范围
number = list(range(1, 6))
# print(number)

# for nub in range(1, 3):
#     print(nub)
# 最大值，最小值的方法
# print(min(number))
# print(max(number))

# 切片，将列表的一部分输出
# print(arry)
# print(arry[0:2])
# str1 = arry[0:2]
# print(str1)
# 遍历切片
# for a1 in arry[0:2]:
#     print(a1)

# 复制列表
# nubers = arry

# 列表是可以动态修改的，元组不行！！！
dim = (100, 200, 300)
# print(dim)
# print(dim[1])
#
# for aw in dim:
#     print(aw)
#
# print(len(dim))

# for a in arry:
#     if a == 'haha':
#         print(a.upper())
#     else:
#         print(a)
# for b in range(0,10):
#     if b > 2 and b < 5:
#         print("haha")
#     else:
#         if b< 2 or b > 8:
#             print("kaka")
#         else:
#             print(b)

# if 'jiji' in arry:
#     print('在')
# elif 'haha' in arry:
#     print('我在')
# else:
#     print("不在")

# 字典 相当于Java的 map，但和Java 又不一样，结构和json 一样
color = {"white": "ffffff", 'black': '000000'}
# print(color)
# print(color['white'])
# 一个字典中可以存在多种，字典也是动态的,不关心顺序
ko = {'wight': 100, 'name': 'lili'}
# print(ko)
ko['age'] = 10
# print(ko)
# ko['name']='haha'
# print(ko)
# del ko['name']
# print(ko)

# 遍历字典 输出键值对
# for key,value in ko.items():
#     print(key)
#     print(value)

# 输出字典的 key
# for key in ko.keys():
#     print(key)
# 输出字典的 value
# for value in ko.values():
#     print(value)
ko['height'] = 100
# print(ko)
# # 使用set() 方法将字典里的value值重复的去除
# for value in set(ko.values()):
#     print(value)
# 将列表嵌套在字典中
ko['pp'] = [1, 2, 3]
# 字典嵌套在列表中
wo = [color, ko]
# print(wo)
# 在字典中嵌套字典
color['expend'] = {'blue': '333333', 'yellow': '900909'}
# 遍历列表里的字典
# for o in wo:
#     print(o)

# 输入函数input
nsg = ""
# print(nsg)

# 用户默认输出的是字符串，使用int() 可将字符串转换成数字，使用str（） 是将数字转成字符串
# age1 = int(nsg)
# if age1 > 27:
#     print('haha')
# else:
#     print('lala')
# while nsg != 'close':
#     nsg = input("please input name : ")
#     print(nsg)

while True:
    nsg = input("please input name : ")
    if nsg == 'haha':
        print(nsg)
        break
    else:
        print(nsg)
