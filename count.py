#coding:utf-8
class A(object):
	"""docstring for A"""

	def add(self,a,b):
		return a+b

class B(A):
	"""docstring for B"""
	def sub(self,a,b):
		return a-b

b=B()

if __name__ == '__main__':
	print b.add(4,5)

# u'B继承了A的财产，所以可以用A的方法'


	# def __init__(self, arg):
	# 	super(B, self).__init__()
	# 	self.arg = arg
		
	# def __init__(self, arg):
	# 	super(A, self).__init__()
	# 	self.arg = arg
