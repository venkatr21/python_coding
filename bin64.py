import math
a=0
while a<64:
    b=bin(a)[2:]
    print('0'*(6-len(b))+b)
    a+=1
