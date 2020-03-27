from collections import Counter
import random
def facto(n):
    if n==1:
        return 1
    else:
        return n*facto(n-1)
s=input()
ctr=Counter(s)
di=dict(ctr)
l=[]
for i in s:
    l.append(i)
newst=[]
for i in di.keys():
    di[i]=di[i]/2
for i in s[::-1]:
    countt=0
    while di[i]>0:
        newst.append(i)
        di[i]=di[i]-1
print(newst)
k=facto(len(newst))
print(k)
countt=0
fin=[]
while countt<k:
    random.shuffle(newst)
    if ''.join(newst) not in fin:
        fin.append(''.join(newst))
        countt+=1

    
    

