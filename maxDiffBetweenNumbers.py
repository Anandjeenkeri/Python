
def maxDiff(arr):
	maxDiff = 0
	for i in arr:
		for j in arr:
			maxDiff = max(maxDiff, i-j)
	return maxDiff
	
print(maxDiff([2,4,6,1]))


def reverse_string(str):
	return ' '.join([word[::-1]for word in str.split()])

print(reverse_string("I work at Thomson"))


		
		