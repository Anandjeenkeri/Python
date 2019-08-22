def is_paliandrome(s):
	return s[::-1] == s
	

	
def get_nearest_pali(s):
	if is_paliandrome(s):
		return s
		
	if s[0] == s[-1]:
		return s[0]+get_nearest_pali(s[1:])+s[-1]
	else:
		pa1_1 = s[0] + get_nearest_pali(s[1:])+s[0]
		pa1_2 = s[-1] + get_nearest_pali(s[:-1])+s[-1]
		
		if len(pa1_1) > len(pa1_2):
			return pa1_2
		elif len(pa1_1) < len(pa1_2):
			return pa1_1
		return pa1_1 if pa1_1 < pa1_2 else pa1_2
		

		
print(get_nearest_pali("ananda"))



def get_max_sum_subarray(arr):
	if not arr or max(arr) < 0:
		return 0
	
	current_max_sum = arr[0]
	overall_max_sum = arr[0]
	
	for num in arr:
		current_max_sum = max(num, current_max_sum+num)
		overall_max_sum = max(current_max_sum, overall_max_sum)
	
	return overall_max_sum
	

	
print(get_max_sum_subarray([12,13,-1,4,5,6,7,8,9]))