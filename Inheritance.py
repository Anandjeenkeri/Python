
class Person(object):
	nationality = 'Indian'
	#Constructor method for the person class and is called during when object is being instantiated
	def __init__(self, name):
		self.name = name
	
	def __repr__(self):
		return "The name of the class%s"%(self.name)
	
	def __str__(self):
		return "The str format %s"%(self.name)
	def func(self):
		print("This is person class method")
	
	#method returns the person name which is set during object instantiate
	def getName(self):
		print("Return name")
		return self.name
	def setName(self, name):
		print("Set new name")
		self.name = name
		
p = Person("Anand")
p.func()
print(p.getName())
p.setName("Advika")
print(p.getName())
print(p.nationality)
print(Person.nationality)

#Python example show multiple inheritance

class Base1():
	def __init__(self):
		print("Calling Base1 constructor")
	def base_fun(self):
		print("I am from Base1 class")
	def __del__(self):
		print("Base1 destructor called")
	
class Base2():
	def __init__(self):
		print("Calling Base2 constructor")
	
	def base_fun(self):
		print("I am from Base2 class")
	
	def __del__(self):
		print("Base2 destructor called")
		
class Derived(Base1, Base2):
	def __init__(self):
		Base2.__init__(self)
		Base1.__init__(self)
		print("Derived")
	
	def __del__(self):
		print("Destructor called")

d = Derived()
d.base_fun()

b2 = Base2()
b2.base_fun()


		


