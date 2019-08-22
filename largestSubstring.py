
str1 = "([[({})]])"
list1 = list(str1)
for s in str1:
	if s == '(':
		if s == list1.pop():
		print(s)
	
	

