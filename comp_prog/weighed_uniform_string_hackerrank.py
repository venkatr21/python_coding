#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    fin = []
    for i in queries:
        var = i
        ct = 1
        while ct<=int(math.sqrt(var)):
            if(var%ct==0) and (var//ct+96)<122:
                ele = str(chr((var//ct)+96))
                pos = ele*ct
                print(var,ct,ele)
                if(re.search(pos,s)):
                    fin.append("Yes")
                    break
            ct = ct+1
        else:
            fin.append("No")
    return fin



if __name__ == '__main__':

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)
    print(result)
