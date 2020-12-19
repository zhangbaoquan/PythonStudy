# coding=utf-8
"""
@project : python_work
@author  : zhangbaoquan
#@file   : xlsTest.py
#@ide    : PyCharm
#@time   : 2020-10-24 11:16:30
@desc    : 崩溃日志分析

"""
from xlrd import open_workbook
import os
from xlwt import Workbook
import pandas as pd


file_crash = '/Users/zhangbaoquan/work/MyProject/python_work/PythonStudy/file/crash.xls'

# """ 打开xls 文件"""
# work_book = open_workbook(file_crash)
# """ 输出显示当前xls 有几张表 """
# print('number of worksheets:', work_book.nsheets)
#
# for worksheet in work_book.sheets():
#     """ 输出每张表的表名、行数、列数"""
#     print('workSheet name: ', worksheet.name)
#     print('Rows: ', worksheet.nrows)
#     print('Columns: ', worksheet.ncols)


""" 将Crash.xls 文件的内容复制到testCrash.xls"""
# 创建一个testCrash.xls 文件，并将文件保存在file2文件夹下
root_path = '/Users/zhangbaoquan/work/MyProject/python_work/PythonStudy/file2/'
file_status = os.path.exists(root_path)
# 判断当前文件夹是否已经创建
if file_status != True:
    print("当前文件夹没有创建")
    os.makedirs(file_status)
else:
    print("当前文件夹已经创建")

output_file = root_path + "testCrash.xls"
# 创建文件
# open(output_file, 'w')

# testCrash.xls 创建一个工作簿和工作表，表名是 " haha " 并将创建的表添加到工作簿中
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet("haha")
#
# # 将xls 数据存在一个json 中
# jsonData = {}
# # 读取Crash.xls 文件，读xls 用的是open_workbook，其他普通文件用open
# with open_workbook(file_crash) as workbook:
#     # 获取 haha 列中的数据
#     worksheet = workbook.sheet_by_name('haha')
#     # 读取第一行，第三列的数据
#     for row in range(worksheet.nrows):
#         data = []
#         jsonData[row] = data
#         for col in range(worksheet.ncols):
#             data.append(worksheet.cell_value(row, col))
#
# print(jsonData)
# # 结果 ： {0: ['haha', 'lala', 'huhu', 'hehe '], 1: ['n1', 'n2', 'n3', 'n4']}

""" 使用pandas 库分析数据"""
data_frame = pd.read_excel(file_crash,sheet_name='haha')
