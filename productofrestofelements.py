def factor(arr):
	cumulative_prod = 1
	right_prod_arr = list()
	for num in arr:
		cumulative_prod *= num
		right_prod_arr.append(cumulative_prod)
	
	cumulative_prod = 1
	left_prod_arr = list()
	for num in arr[::-1]:
		cumulative_prod *= num
		left_prod_arr.append(cumulative_prod)
	left_prod_arr = left_prod_arr[::-1]
	
	print(left_prod_arr)
	print(right_prod_arr)
	out_put_arr = list()
	for i in range(len(arr)):
		num = None
		if i == 0:
			num = left_prod_arr[i+1]
		elif i== len(arr)-1:
			num = right_prod_arr[i-1]
		else:
			num = right_prod_arr[i-1] * left_prod_arr[i+1]
		out_put_arr.append(num)
	return out_put_arr
	

print(factor([2,2,3,4,5]))
