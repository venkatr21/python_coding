#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the morganAndString function below.
def morganAndString(a, b):
    a=list(a)
    b=list(b)
    l=[]
    n=len(a)
    m=len(b)
    i,j=0,0
    while i!=n and j!=m:
        if a[i]>b[j]:
            l.append(b[j])
            j+=1
        else:
            l.append(a[i])
            i+=1
    if i==n:
        while j!=m:
            l.append(b[j])
            j+=1
    elif j==m:
        while i!=n:
            l.append(a[i])
            i+=1
    l="".join(l)
    return l

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        print(result)


