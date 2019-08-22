

def count(s, dictionary):
	for i in s:
		if i not in dictionary:
			dictionary[i] = 1
		else:
			dictionary[i] += 1
			
	max_element = 0
	max_val = 0
	
	for i in dictionary:
		if dictionary[i] > max_val:
			max_val = dictionary[i]
			max_element = i
	
	return max_element

s = "aaaaaaaabbcccccddghkkkkkkk"
dict = {}
print(count(s, dict))