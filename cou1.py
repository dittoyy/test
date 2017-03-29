#coding:utf-8
import count
class C(count.A):
	"""docstring for C"""
	pass
c=C()
if __name__ == '__main__':
	print c.add(1,2)
print __name__
print count.__name__
	# def __init__(self, arg):
	# 	super(C, self).__init__()
	# 	self.arg = arg
		