

def sumoflistsubset(arr, sum):
	potentional_solution = set()
	for n in arr:
		if n in potentional_solution:
			return True
		potentional_solution.add(sum-n)
	return False
	
print(sumoflistsubset([10,13,5,7], 50))
	