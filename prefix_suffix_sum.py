

def findElement(arr):
	n = len(arr)
	 
	prefix_sum = [0] * n
	prefix_sum[0] = arr[0]
	 
	for i in range(1, n):
		prefix_sum[i] = prefix_sum[i-1] + arr[i]
	print(prefix_sum)
	
	suffix_sum = [0] * n
	suffix_sum[n-1] = arr[n-1]
	for i in range(n-2, 0, -1):
		suffix_sum[i] =  suffix_sum[i+1] + arr[i]
		
	print(suffix_sum)
	
	for i in range(n):
		if prefix_sum[i] == suffix_sum[i]:
			print(arr[i])
			break
	

if __name__ == "__main__":
	findElement([1,4,5,3,10])