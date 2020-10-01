import math
import os
import random
import re
import sys
import collections

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dict = collections.Counter(ar)
    count=0
    for x in dict:
        if(dict[x]%2==0):
            count+=dict[x]//2
        elif(((dict[x]-1)%2)==0):
            count+=dict[x]//2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
