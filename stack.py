class Stack:
	def __init__(self):
		self.stack = []
	
	def add(self, item):
		if item not in self.stack:
			self.stack.append(item)
			return True
		else:
			return False
	
	def peek(self):
		return self.stack[0]
	
	def display(self):
		if len(self.stack) <= 0:
			print("No elements to display in stack")
		else:
			print(self.stack)
	
	def pop(self):
		if len(self.stack) <= 0:
			return ("No elements in the stack")
		else:
			return self.stack.pop()

			
s = Stack()
s.add(1)
s.add(3)
s.display()
s.pop()
s.display()