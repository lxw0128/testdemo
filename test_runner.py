# _*_ coding: utf-8 -*-
# @Author : lixinwei
# @Time   : 2021/1/21 2:45 上午
import unittest
from BeautifulReport import BeautifulReport

testsuit =unittest.defaultTestLoader.discover('./test/testBaidu',pattern='*.py')
result = BeautifulReport(testsuit)
result.report(filename='testreport', description='testreport', log_path='./test/testBaidu/report/')
