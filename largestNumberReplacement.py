items = [1,5,3,2,3,7,10,8,7,11]

for i in range(len(items)):
	for j in items[i+1:]:
		if j > items[i]:
			items[i] = j
			break

print(items)


str = "abcaaabbdfgheeeeiiikkkkkookjkkppppppp"

elements = list(str)
flag = 0
seen = 0
res = []
i = 0

for i in range(len(elements)-1):
	if elements[i] == elements[i+1]:
		seen = 1
	else:
		if seen == 1:
			seen = 0
		else:
			res.append(elements[i])

if seen == 0:
	res.append(elements[-1])

print(res)

largestSub = []
tempSub = []


print(elements)
for i in range(len(elements)-1):
	#Verify whether curent element and next elements are equal
	if elements[i] == elements[i+1]:
		#we are in a substring having the same elements
		flag = 1  
		tempSub.append(elements[i])
	else:
		if flag == 1:
			tempSub.append(elements[i])
			flag = 0
			if len(tempSub) > len(largestSub):
				del largestSub[:]
				largestSub = tempSub[:]
				del tempSub[:]
				#print (largestSub)
			else:
				del tempSub[:] 
		
				
print(largestSub)


'''
Bubble sort
'''
list1 = [10,4,5,2,6,7,12]

def bubbleSort(arr):
	#Decrement the value everytime when a value pushed to its position
	for n in range(len(arr)-1,0,-1):
		#print(n)
		for k in range(n):
			if arr[k] > arr[k+1]:
				tmp = arr[k]
				arr[k] = arr[k+1]
				arr[k+1] = tmp	
	return arr
	
print(bubbleSort(list1))

	
'''
Insertion sort
'''

'''
You've been given a list of historical stock prices for a single day for Amazon stock. The index of the list represents the timestamp, so the element at index of 0 is the initial price of the stock, the element at index 1 is the next recorded price of the stock for that day, etc. Your task is to write a function that will return the maximum profit possible from the purchase and sale of a single share of Amazon stock on that day. Keep in mind to try to make this as efficient as possible.
'''
def profit(stock_prices):
	print("Maximum profit possible from the stock market")
	min_stock_price = stock_prices[0]
	max_profit = 0
	
	for price in stock_prices[1:]:
		min_stock_price = min(price, min_stock_price)
		comparison_price = price - min_stock_price
		max_profit = max(max_profit, comparison_price)
		
	return max_profit
	
	
#Largest count sum

def largest_cnt_sum(arr):
	print("Largest count of sum")
	if len(arr) == 0:
		return 0
	
	max_sum  = sum = arr[0]
	
	for n in arr[1:]:
		sum = max(sum, sum+n)
		max_sum = max(sum, max_sum)
	
	return max_sum
	pass
	
l = [1,2,-1,3,4,10,10,-10,-1]

print(largest_cnt_sum(l))


def anagram(s, t):
	print("Check two given strings are anagrams")
	s = s.replace(' ', '').lower()
	t = t.replace(' ', '').lower()
	
	if (len(s) != len(t)):
		return False
	
	counter = {}
	
	for letter in s:
		if letter in counter:
			counter[letter] += 1
		else:
			counter[letter] = 1
		
	for letter in t:
		if letter in counter:
			counter[letter] -= 1
		else:
			return False
		
	for k in counter:
		if counter[k] != 0:
			return False
	
	return True
	
print(anagram('dog', 'god'))

	
			
#Given two arrays, find the missin element in first arrays

def finder(arr1, arr2):
	print("Finding the missing number from the given two arrays")
	sum = 0
	for n in arr1:
		sum += n
	
	for n in arr2:
		sum -= n
	
	return sum

print(finder([1,2,3,4,5,6,7], [3,7,2,1,4,5]))

def findmissingNumber(arr1, arr2):
	result = 0
	for num in arr1+arr2:
		result ^= num
	
	return result
	
print(findmissingNumber([1,2,3,4,5,6,7], [3,7,2,1,4,5]))


def compress(s):
	l = len(s)
	r = ""
	
	if l == 0:
		return ""
	
	if l == 1:
		return s+"1"
	cnt = 1
	i = 1
	while i < l:
		if s[i] == s[i-1]:
			cnt += 1
		else:
			r=r+s[i-1]
			cnt = 1
		i += 1
	
	r = r + s[i-1]
	return r
	
print(compress("AAABBCCC"))


'''
Given a string, determine if it is comprised of all unique characters
'''

def uniq_char(s):
	return len(set(s)) == len(s)
	
print(uniq_char("abcd"))


#aLCdPoX642Kp2ZwW

'''
import subprocess
import re
result = []

win_cmd = 'ipconfig'
process = subprocess.Popen(win_cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for line in process.stdout:
	if 'IPv4' in line:
		match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
		if match:
			print(match.group(0))
'''

'''String subsequence'''

s = 'abc'
t = 'ahbvfc'

def isSubsequence(str1, str2):
	m = len(str1)
	n = len(str2)
	
	i = 0
	j = 0
	while j < m and i < n:
		if str1[j] == str2[i]:
			j = j+1
		i = i+1
	return j==m
print('Print the string subsequence')
print(isSubsequence('abc', 'anbfghjcvg'))
			