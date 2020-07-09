import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    b = 0
    arr = [x for x in range(i,j+1)]
    for n in arr: 
        rev = int(str(n)[::-1])
        
        if(abs(n-rev)%k==0):
            b+=1
    return b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ijk = input().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])
    result = beautifulDays(i, j, k)
    fptr.write(str(result) + '\n')
    fptr.close()
