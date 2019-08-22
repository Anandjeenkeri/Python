import unittest

def string_compression(string):
	comprresed_string = []
	len = 0
	counter = 0
	print(string)
	for i in range(len(string)):
		if i != 0 and string[i] != string[i-1]:
			comprresed_string.append(string[i-1] + str(counter))
			counter = 0
		counter += 1
	
	comprresed_string.append(string[-1] + str(counter))
	return min(string, ''.join(comprresed_string), key=len)
	

s = 'aaabbvvfrkkkk'

print(string_compression(s))
	
	