def absolutePermutation(n, k):
    if k==0:
        return [i for i in range(1,n+1)]
    elif n%2==1:
        return [-1]
    elif k>n/2 or (n%k)%2!=0:
        return [-1]
    else: 
        l=[i for i in range(1,n+1)]
        ks=[]
        index=n//k
        for i in range(0,index-1,k):
            for m in range(k*(i+1),k*(i+2)):
                ks.append(l[m])
            for m in range(k*i,k*(i+1)):
                ks.append(l[m])
        return ks
