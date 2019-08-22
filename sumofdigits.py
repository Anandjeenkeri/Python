

def totalsum(Number):
	Sum = 0
	while(Number > 0):
		Reminder = Number % 10
		Sum = Sum + Reminder
		Number = Number //10
	return Sum
n = 8904491421

def leastSum(n):
	sum = totalsum(n)
	while(len(str(sum)) > 1):
		print(sum)
		sum = totalsum(sum)
	return sum

print(leastSum(n))
		
		
		
	
	


		
		