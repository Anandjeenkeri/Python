
def find_first(elem, arr):
	for i in range(len(arr)):
		if a[i] == elem:
			return i
			
	return -1
	
def find_last(elem, arr):
	index = -1
	for i in range(len(arr)):
		if arr[i] == elem: #we found the element first time and let us see if the same element exist susequently 
			if i < len(arr) and a[i+1] == elem: #ele exist next to it and increment the index 
				index = i + 1
			else:
				index = i   #same elem is not continued hence return the last element
				break
				
	return index

arr = [1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 7, 7]
print(find_first(arr, 3))
print(find_last(arr, 7))

