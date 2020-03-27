n=int(input())
l=[['N' for i in range(n)] for j in range(n) ]
arr=[]
for i in range(n):
    arr.append(list(map(str,input().rstrip().split())))
for i in range(n):
    for j in range(n):
        if i!=j:
            l[i][j]=arr[i][j]
counter=0
for i in range(n):
    lis=[]
    for j in range(n):
        lis.append(l[j][i])
    if lis.count('T')>=lis.count('F'):
        counter=counter+1
    print(lis)
print(counter)
