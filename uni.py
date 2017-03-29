#coding:utf-8
def sub(c,d):
	return c-d

class A():
	def add(self,a,b):
		return a+b

a=A()

if __name__ == '__main__':
	print sub(8,3)
	print a.add(2,4)