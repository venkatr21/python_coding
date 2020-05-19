def checker(arr):
    counts=0
    for i in arr:
        if i>0:
            counts+=1
    return counts
n = int(input())
a=[]
b=[]
for i in range(n):
    st = input().strip().split()
    a.append(int(st[0]))
    b.append(int(st[1]))
if(n>1):
    mini = min(a)
    maxi = max(b)
    size = maxi-mini
    maxval = 0
    fin = [0 for i in range(size)]
    for i in range(n):
        for pos in range(a[i],b[i]):
            fin[pos-mini]+=1
    for i in range(n):
        fin1 = fin.copy()
        for pos in range(a[i],b[i]):
            fin1[pos-mini]-=1
        ele = checker(fin1)
        if maxval<ele:
            maxval= ele
    print(maxval)
else:
    print(b[0]-a[0])
        
