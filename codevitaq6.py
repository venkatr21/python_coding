def facto(n):
    return 1 if n==1 else n*facto(n-1)
n=int(input())
arr=list(map(int,input().split()))
q=int(input())
query=[]
for i in range(q):
    query.append(list(map(int,input().split())))
for i in range(q):
    tot=1
    for j in range(query[i][0],query[i][1]+1):
        tot=tot*facto(arr[j-1])
    tot=tot%1000000007
    print(tot**(query[i][1]-query[i][0]))
        
