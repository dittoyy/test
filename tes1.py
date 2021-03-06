# coding:utf-8
import unittest
import HTMLTestRunner

# 测试case文件夹路径
test_dir = "D:\\test"

# 自定义格式时间戳
import time
c_time = time.strftime("%Y_%m_%d %H_%M_%S")
print c_time

# 测试报告的完成路径名称
report_name = "D:\\test"+c_time+"resut.html"

# 这个是定义加载套件的函数
def creatsuite(test_dir,pattern="test*.py"):
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern,
                                                   top_level_dir=None)
    #print discover
    testcase = unittest.TestSuite()
    for test_suite in discover:
        #print test_suite
        for test_case in test_suite:
            #print test_case
            testcase.addTests(test_case)
    print testcase
    return testcase

if __name__ == "__main__":
    fp = open(report_name, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'XXX项目测试报告',
                                           description=u'用例执行情况：')
    runner.run(creatsuite(test_dir,"test*.py"))
    fp.close()
    # r = unittest.TextTestRunner()
    # r.run(creatsuite(test_dir,"test*.py"))
