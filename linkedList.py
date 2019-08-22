class Node:
	def __init__(self,datavalue=None):
		self.datavalue = datavalue
		self.nextval = None
		
		
class SLinkedList:
	def __init__(self):
		self.headvalue = None
	
	'''
		Insert at the end of the list
	'''
	def atEnd(self, dataelem):
		#Create a new node
		NewNode = Node(dataelem)
		#list is empty and make new element as head value
		if self.headvalue == None:
			self.headvalue = NewNode
			return 
		lastele = self.headvalue
		#traverese till last node element
		while lastele.nextval is not None:
			lastele = lastele.nextval
		#point last element to the new element
		lastele.nextval = NewNode
			
	
	def listprint(self):
		printval = self.headvalue
		while printval is not None:
			print(printval.datavalue)
			printval = printval.nextval

list = SLinkedList()
list.headvalue = Node("Jan")
e2 = Node("Feb")
e3 = Node("Mar")
list.headvalue.nextval = e2
e2.nextval = e3
list.atEnd("Apr")
list.atEnd("May")

list.listprint()
