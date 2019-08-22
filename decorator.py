def dec(x):
	return x - 1

def inc(x):
	return x + 1
	
def operator(func, x):
	result = func(x)
	return result
	
print(operator(dec, 4))


def is_called():
	def is_returned():
		print("Hellow")
	return is_returned
	
new = is_called()
new()

def make_pretty(func):
	def inner():
		print("I got decorated")
		func()
	return inner
	
@make_pretty
def ordinary():
	print("I am ordinary")
	
	
ordinary()


def print_iterator(it):
	for x in it:
		print(x, end='')
	print('')
	
list = [1,2,3,4]

map_iterator = map(lambda x: x*2, list)
print_iterator(map_iterator)

name = 'eg-filer'
str = name.split('-')
print(str)
excludedFilers = ['eg','hy']

if not name.startswith('eg-'|'hy-'):
	print("Excluded")
else:
	print("Includede")
	
