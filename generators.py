def square_num(nums):
    for i in nums:
        yield(i*i)

my_nums = square_num([1,2,3,4,5,6])

for num in my_nums:
    print(num)

def fibonacci(num):
    a,b = 0,1
    for i in range(0,num):
        print(a)
        a,b = b,a+b

fibonacci(10)