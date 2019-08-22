def leader(arr):
	res = []
	leader = arr[0]
	i = 0
	print(len(arr))
	for i in range(0, len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i] <= arr[j]:
				break
		if j == len(arr)-1:
			print(arr[i])

if __name__ == "__main__":
	leader([6,7,15,1,3,4,5])