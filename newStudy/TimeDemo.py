#coding=utf-8
"""
@project : PythonStudy
@author  : zhangbaoquan
#@file   : TimeDemo.py
#@ide    : PyCharm
#@time   : 2020-12-19 15:22:02
@desc    : 定时任务


"""

import time
import datetime
import threading
import subprocess


def test():
    print("lala")
    # 让函数睡1秒
    time.sleep(5)
    print("haha")

# 创建一个定时任务，从当前开始，一直到12月25日0点，一直执行一个任务
def timer():
    endTime = datetime.datetime(2020,12,25,0,0,0)
    while datetime.datetime.now() < endTime:
        print("haha")
        time.sleep(3)
        print("lala")

# 创建一个子线程去执行一个定时任务
def useThread():
    # 这里使用threading.Thread 创建一个线程，target=timer 表示在新线程中调用的函数是timer ，这里的timer 是函数的参数
    thread = threading.Thread(target=timer)
    thread.start()

#     启动其他进程
def openOtherProcess():
    subprocess.Popen('/Applications/QQMusic.app/Contents/MacOS/QQMusic')


if __name__== '__main__':
    # 这里使用 time.time() 返回的是自1970年以来的秒数
    t1 = time.time();
    # test()
    # 使用round 函数将保留小数点后面两位
    print(round(t1,2))

    # 使用datetime 可以更加规范化显示时间
    # t2 = datetime.datetime.now()
    # print(t2)
    # print(t2.day)
    # print(t2.minute)

    # useThread()
    # time.sleep(5)
    # print("😝")

    openOtherProcess()


