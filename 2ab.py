#coding:utf-8
# def add(a,b):
# 	c=a+b
# 	return c
# 	pass
# if __name__ == '__main__':
# 	print add(2,3)

from selenium import webdriver
import unittest
import time

class Baidu(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get("https://www.baidu.com")
		print '111'
	def test_001(self):
		'''search selenium'''
		driver=self.driver
		se=driver.find_element_by_css_selector('#kw')
		se.send_keys('selenium')
		driver.find_element_by_css_selector('#su').click()
		print '222'
	def test__002(self):
		'''search python'''
		driver=self.driver
		se=driver.find_element_by_css_selector('#kw')
		se.send_keys('python')
		driver.find_element_by_css_selector('#su').click()
		print '333'
	def tearDown(self):
		self.driver.quit()
		print '444'
if __name__ == '__main__':
	unittest.main()