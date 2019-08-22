

class Person:
	def __init__(self, age=0):
		self._age = 0
	
	@property
	def age(self):
		print("Getter method is called")
		return self._age
	
	@age.setter
	def age(self,a):
		if (a < 18):
			raise ValueError("Sorry")
		print("Setter method is called")
		self._age = a
		

andy = Person()
andy.age = 21
print(andy.age)
		
		