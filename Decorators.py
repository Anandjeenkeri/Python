#It allows the programmers to modify the behavior of the definition
#Decorators allow us to wrap one function with another function in order to extend the behavior of the wrapped function
#without permanently modifying it

#gfg_decorator # is a callable function will add some code on top of some other function 


#def hello_decorator():
#	print("Gfg")
#

def hello_decorator(func):
	def inner1(a, b):
		print("Before execution")
		
	
		returned_value = func(a,b) #Here we are calling the actual function 
		print("Some function called here")
		print("Total=", returned_value)
	
		print("after execution")
	
		return returned_value + 10
	return inner1
	
@hello_decorator
def sum_two_numbers(a,b):
	print("Inside the function")
	return a+b
	
a,b = 4,5
print("Sum=",sum_two_numbers(a,b))


print("Map function")
'''
Map function expects a function object and any number of iterables like list 
,dictionary, etc. It executes the function_object for each element in the iterables
and returns the list of elements modified by the function object
'''

def mult(x):
	return x*2

list1 = map(lambda x:x*2, [1,2,3,4,5])
print(list(list1))

import pprint
list2 = filter(lambda x: x%2 !=0, range(10))
pprint.pprint(list2)
print(list(list2))
