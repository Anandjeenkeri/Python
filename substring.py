string = input("Enter string")
substring = input("Enter substring")

count = 0

print(len(string) - len(substring)+1)

for i in range(len(string) - len(substring)+1):
	if string[i:i+len(substring)] == substring:
		count += 1

print(count)