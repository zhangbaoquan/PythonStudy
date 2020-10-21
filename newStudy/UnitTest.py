#coding=utf-8
"""
@project : python_work
@author  : zhangbaoquan
#@file   : UnitTest.py
#@ide    : PyCharm
#@time   : 2020-10-20 23:07:01
@desc    : 单元测试学习

"""

import unittest

class NameTest(unittest.TestCase):
    """ 测试单元 """
    def testName(self):
        self.assertEqual("hah","hah")



unittest.main()