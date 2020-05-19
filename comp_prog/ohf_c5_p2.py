n = int(input())
x=[]
y=[]
for i in range(n):
    a= input().strip().split(' ')
    x,y =[int(i) for i in a]
    ele = x+1
    val = y-1
    print(".......")
    while True:
        if ele*val <x*y:
            break
        elif (ele+1)*val <x*y and (ele+1)*val > ele*val:
            ele = ele+1
        val = val-1
    counter=0
    ele1 = y+1
    val1 = x-1
    while True:
        if ele1*val1 <x*y:
            break
        elif (ele1+1)*val1 <x*y and (ele1+1)*val1 > ele1*val1:
            ele1 = ele+1
        val1 = val1-1
    while val>0:
        if(val*ele<x*y):
            counter +=1
        else:
            print(ele,val)
        val = val-1
        ele = ele+1
    while val1>0:
        if(val1*ele1<x*y):
            counter +=1
        else:
            print(ele1,val1)
        val1 = val1-1
        ele1 = ele1+1
    print(counter)
