import sys

def find_prime(num):
    res_list = []
    for i in range(2,num+1):
        if res_list!=[] and any(i%l==0 for l in res_list):
            continue
        res_list.append(i)
    return res_list

if __name__=="__main__":
    if len(sys.argv)!=2: raise Exception("usage - $python find_prime.py <num:int>")
    try:num = int(sys.argv[1])
    except ValueError: raise Exception("Enter an integer as argument only.")
    l = find_prime(num)
    print(l)