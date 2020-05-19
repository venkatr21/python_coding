def pathfinder(A): 

    paths = [[0]*len(A[0]) for i in A]
    if A[0][0] == 0: 
        paths[0][0] = 1
    for i in range(1, len(A)):
        if A[i][0] == 0: 
            paths[i][0] = paths[i-1][0]
    for j in range(1, len(A[0])): 
        if A[0][j] == 0: 
            paths[0][j] = paths[0][j-1]          
    for i in range(1, len(A)): 
        for j in range(1, len(A[0])): 
            if A[i][j] == 0: 
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
    return paths[-1][-1] 

def nCr(n, r): 
    return (fact(n) / (fact(r)  
                * fact(n - r)))  
def fact(n): 
    res = 1
    for i in range(2, n+1): 
        res = res * i    
    return res 

test = int(input())
for i in range(test):
    w,h,l,u,r,d = list(map(int,input().strip().split()))
    a=[[0 for i in range(w)]for i in range(h)]
    for i in range(u-1,d):
        for j in range(l-1,r):
            a[i][j]=1

    event = pathfinder(a)
    total = nCr(w+h-2,w)
    print(event,total)
    
    
    
