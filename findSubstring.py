string = input("Enter string")
substring = input("Enter substring")

count = 0

print(len(string) - len(substring)+1)

#GEt the strin and substring
#we need to traverse over through the rest of the string 
#

for i in range(len(string)-len(substring)+1):
	print(string[i:i+len(substring)])
	if string[i:i+len(substring)] == substring:
		count += 1

print(count)