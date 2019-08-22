#code
def maxSum(l,s):
    start_index = l[0]
    end_index = l[0]
    for i in range(len(l)):
        sum = l[i]
        start_index = l[i]
        for j in l[i+1:]:
            sum =sum+j
            if sum == s:
               '''sdf'''
               return start_index,j
    else:
        return -1
        
if __name__ == "__main__":
    list1 = [1,2,3,4,5,6,7]
    print(maxSum(list1,28))