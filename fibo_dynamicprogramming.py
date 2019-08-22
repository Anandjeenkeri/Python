
def fib(n, memoize):
	if memoize[n] is not None:
		return memoize[n]
	if n==1 or n==2:
		return 1
	else:
		result = fib(n-1, memoize[n-1]) + fib(n-2, memoize[n-2])
		memoize[n] = result

		
n=5
memoize = [None for _ in range(0,n+1)]
print(len(memoize))
print(memoize[5])

res = fib(n, memoize)
print(res)