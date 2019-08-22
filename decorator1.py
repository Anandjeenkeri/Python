#callable decorator function and it takes function as argument
def hello_decorator(func): 
	def inner1(*args, **kwargs): #wrapper function
		print("Before function") #do some operation before calling the actual function
		returned_value = func(*args, **kwargs)  #calling the actual function
		print("After function ") #after calling the actual function
		return returned_value #return the actual function value
	return inner1 #return the wrapper function 

	
@hello_decorator #call the decorator function
def sum_two_number(a,b,c):
	print("Inside actual function")
	return a+b+c

print("Sum of number:{}".format(sum_two_number(2,4,5)))

def myFunc(arg, **kwargs):
	print(arg)
	for key, value in kwargs.items():
		print("%s==%s"%(key,value))
	
myFunc("Hi", first='Anand', last='jeenkeri')


class MyClass:
	#hidden varaible 
	__hiddenVariable = 0
	
	#A member method that changes the hidden variable
	
	def add(self, increment):
		self.__hiddenVariable += increment
		print(self.__hiddenVariable)
		
myObject = MyClass()
print(dir(myObject))
myObject.add(10)
print(myObject._MyClass__hiddenVariable)

print(myObject.__class__)
print(myObject.__doc__)

class Test:
	def __init__(self, a,b):
		self.a = a
		self.b = b
		
	def __repr__(self):
		return "Test a:%s b:%s" % (self.a, self.b)
	
	def __str__(self):
		 return "From str method of Test: a is %s b is %s" % (self.a, self.b)
	
#Driver code

t = Test(10,20)
print(t)
print([t])

class Base(object):
	def __init__(self, x):
		print("Calling base constructor")
		self.x = x
		
	
class Derived(Base):
	def __init__(self, x, y):
		print("Calling derived constructor")
		Base.x = x
		self.y = y
		
	def printStr(self):
		print("Printing derived method")
		print(Base.x, self.y)

d = Derived(10,23)
print(d.printStr())

import pprint
nums = [1,-3,5,6,-7]

print(max(nums))

positives = filter(lambda num: num>0, nums)

pprint.pprint(list(positives))



#two great benifits of generators
'''
A generator looks lot like a function, but uses the keyword 'yield' instead of 'return'
'''

def gen_num():
	n = 0
	while n < 4:
		yield n
		n += 1

num = gen_num() # when we call it returns a generator object
print(next(num))
print(next(num))

'''
Each time the generator is called it pauses at that moment in the function
'''