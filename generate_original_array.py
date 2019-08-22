
def generateOriginalArray(arr):
	n = len(arr)
	res = []
	count = 0
	for i in range(n):
		for j in range(n):
			if arr[j] >= arr[i]:
				count += 1
		res.append(count)
		count = 0
	
	return res

	
def printElementBetweenArray(arr, first, last):
	n = len(arr)
	
	res = []
	res.append(first)
	
	for i in range(n):
		if arr[i] == first:
			for j in arr[i:]:
				if arr[j] != last:
					res.append(arr[j])
				else:
					res.append(last)
					return res

def greaterElements(arr):
	n = len(arr)
	count = 0
	for i in range(n):
		count = 0
		for j in range(n):
			if arr[j] > arr[i]:
				count += 1
				if count == 2:
					print(arr[i])
					break

def nextGreaterElement(arr):
	for i in range(len(arr)):
		diff = 1000
		closest = -1
		for j in range(0, len(arr)):
			if arr[i] < arr[j] and arr[j] - arr[i] < diff:
				diff = arr[j] - arr[i]
				closest = j
		if closest == -1:
			print("_", end = " ")
		else:
			print("{}".format(arr[closest]), end=" ")

def average(arr, no_smallest, no_largest):
	res = arr[no_smallest:]
	res = res[:no_largest]
	sum = 0
	for n in res:
		sum += n
	try:
		print(sum/len(res))
	except ZeroDivisionError:
		print("0")


def pushAllZeros(a):
	k = [0 for i in range(a.count(0))]
	x = [i for i in a if a[i] != 0]
	print(x)
	x.extend(k)
	print(k)
	
def sequence_sum(arr):
	res = [0] * len(arr)
	
	for i in arr:
		for j in range(i,len(arr)):
			res[j] += 1
		print(res)
	
	print(res)

def replace_zero_five(arr):
	for i in range(len(arr)):
		if arr[i] == 0:
			arr[i] = 5
			
	print(arr)

def rotate_string(string,n):
	return string[n:]+string[:n]
					
if __name__ == "__main__":
	print(generateOriginalArray([6, 3, 2, 1, 0, 0, 0]))
	#print(printElementBetweenArray([1,3,3,9,10, 4],3,10))
	greaterElements([2, 8, 7, 1, 5])
	nextGreaterElement([2, 8, 7, 1, 5])
	print("\n")
	average([1, 2, 3],3,3)
	#secondRepeatedWord("anand basavaraj jeenkeri anand")
	pushAllZeros([1,2,0,0,0,4,5])
	sequence_sum([1,1,1,2])
	replace_zero_five([1,2,0,0,2,4])
	print(rotate_string("anand",4))