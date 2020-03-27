[n,m]=list(map(int,input().strip().split()))
l=[]
r=[]
c=[]
for i in range(m):
    [a,b,x]=list(map(int,input().strip().split()))
    l.append(a)
    r.append(b)
    c.append(x)
fin=[0]*(n)
for i in range(m):
    fin[l[i]-1]=c[i]
    fin[r[i]]=-1*c[i]
for i in range(1,n):
    fin[i]=fin[i-1]+fin[i]
print(max(fin))

    
    
    
