def check(l):
    for ele in l:
        if ele>0:
            return True
    return False
t=int(input())
for _ in range(t):

    n=int(input())
    l=input().strip().split(' ')
    l=[int(ele) for ele in l]
    flag=0
    moves=0
    while(check(l)==True):
        c=l.index(min(l))
        for i in range(n):
            if i!=c:
                l[i]=l[i]-1
        moves+=1
    print(moves)
