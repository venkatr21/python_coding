[n,h,m]=input().split()
n=int(n)
h=int(h)
m=int(m)
li=[]
for i in range(n):
    li.append(-1)
for i in range(m):
    [l,r,x]=input().split()
    l=int(l)
    r=int(r)
    x=int(x)
    for j in range(l-1,r):
        if li[j]==-1 or li[j]>x:
            li[j]=x
for i in range(len(li)):
    if li[i]==-1:
        li[i]=h
    li[i]=li[i]**2
print(sum(li))
            


        
    
