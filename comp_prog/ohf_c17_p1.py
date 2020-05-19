fin1=[]
def retlist(inp):
    l = []
    while inp>0:
        ele1 = inp%10
        if ele1>0 and ele1 not in l:
            l.append(ele1)
        inp=inp//10
    return l
def satanic(numb):
    l=[1**1,2**2,3**3,4**4,5**5,6**6,7**7]
    if numb in l:
        return True
    return False
def check(numb):
    if numb>0 and numb not in fin1:
        l = retlist(numb)
        l.sort()
        for i in range(len(l)):
            l[i] = numb - l[i]**2
        for i in l:
            if satanic(i):
                return i
            else:
                check(i)
                fin1.append(i)               
        else:
            return(-1)
            
        
n = int(input())
l=[]
for i in range(n):
    l.append(int(input()))
for i in range(1,1700):
    ele = i
    if satanic(ele) or check(ele)>0:
        print(i,"Yes")
    else :
        print(i,"No")
        
