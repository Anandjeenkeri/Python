
def isDivisible(n):
	for i in str(n):
		if n%int(i)==0:
			return "Yes"
	else:
		return "No"
	

print(isDivisible(3000000007))