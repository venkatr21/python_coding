#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    res=0
    l=[]
    if k==len(contests):
        for i in contests:
            res=res+i[0]
        return res
    for i in contests:
        if i[1]==0:
            res=res+i[0]
        else:
            l.append(i[0])
    l.sort()
    l.reverse()
    for i in range(0,k):
        res=res+l[i]
    for i in range(k,len(l)):
        res=res-l[i]
    return res
        

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)
