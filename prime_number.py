def is_prime(num):
	if num > 1:
		for i in range(2, num-1):
			if num%i == 0:
				return False
		else:
			return True

print(is_prime(5))

def all_prime(upto):
	prime = []
	if upto == 1:
		return 1
	elif upto == 2:
		return (1,2)
	else:	
		for i in range(upto+1):
			if i == 1:
				prime.append(1)
			elif i == 2:
				prime.append(2)
			else:
				if(is_prime(i)):
					prime.append(i)
	return prime

print(all_prime(3))

'''
for arg in sys.argv[1:]:
	try:
		f = open("file.txt")
	except OSError:
		print("cannot open", arg)
	else:
		print(arg, 'has', len(f.readlines()), 'lines')
		f.close()
'''

'''
A thread is a lightweight process except it exists entirely inside a process and shares the resources.
A single process may have multiple threads of exection
Useful when an application wants to perform multiple tasks on shared data
'''