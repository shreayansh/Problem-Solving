import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    x = [a+i for i in apples]
    y = [b+i for i in oranges]
    ca,co = 0,0
    for i in x:
        if(i>=s and i<=t):
            ca+=1
    for i in y:
        if(i>=s and i<=t):
            co+=1
    print(ca)
    print(co)


if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
