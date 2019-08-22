def dict_depth(dic, level=1):
	if not dic:
		return level
	return max(dict_depth(dic[key], level+1) for key in dic)
	
dict = {1:'a', 2: {3: {4: {}}}} 
print(dict_depth(dict))