# _*_ coding: utf-8 -*-
# @Author : lixinwei
# @Time   : 2021/1/21 2:33 上午
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    testsuit =unittest.defaultTestLoader.discover('./testBaidu',pattern='*.py')
    result = BeautifulReport(testsuit)
    result.report(filename='测试报告', description='测试报告', log_path='./testBaidu/report/')

