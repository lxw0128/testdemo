# _*_ coding: utf-8 -*-
# @Author : lixinwei
# @Time   : 2021/1/21 2:45 上午
import argparse
import unittest
import argparse
from BeautifulReport import BeautifulReport
from test.testBaidu.LogUtils import Logger

testsuit = unittest.defaultTestLoader.discover('./test/testBaidu', pattern='*.py')
result = BeautifulReport(testsuit)
result.report(filename='testreport', description='testreport', log_path='./test/testBaidu/report/')

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--env', help='指定运行的环境,中文即可', type=str)
args = parser.parse_args()
param = vars(args)
v = {}
for key, value in param.items():
    v[key] = value
logger = Logger()
logger.info('testdemo入参：%s' % v)
print(v.get('env'))
