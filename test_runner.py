# _*_ coding: utf-8 -*-
# @Author : lixinwei
# @Time   : 2021/1/21 2:45 上午
import unittest
from BeautifulReport import BeautifulReport

testsuit =unittest.defaultTestLoader.discover('./test/testBaidu',pattern='*.py')
result = BeautifulReport(testsuit)
result.report(filename='测试报告', description='测试报告', log_path='./test/testBaidu/report/')
