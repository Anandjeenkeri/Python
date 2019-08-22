import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    res = []
    for ch in s.lower():
        if ch not in res and ch != " ":
            res.append(ch) 
    if len(alphabet) == len(res):
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
