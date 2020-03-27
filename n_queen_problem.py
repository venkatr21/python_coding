def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
def checker(i,j,pos):
    i1=i
    j1=j
    if j not in pos:
        while i1>0 and j1>0:
            i1=i1-1
            if pos[i1]==j1-1:
                return False
            j1-=1
        else:
            while i>0 and j<n-1:
                i=i-1
                if pos[i]==j+1:
                    return False
                j+=1
            else:
                return True
    else:
        return False
    
n=int(input())
if n==2 or n==3:
    print("no soln")
    key=False
else:
    key=True
flag=False
check=0
i=0
tot=fact(n)
counter=0
pos=[[-1]*n]
while key:
    if counter==tot-1:
        break
    if (-1 not in pos[check]) and (check==0 or(pos[check] not in [pos[m] for m in range(check)])) and flag==False:
        pos.append([-1]*n)
        check+=1
        i=0
    if (-1 not in pos[check]) and (check==0 or(pos[check] in [pos[m] for m in range(check)])) and flag==False:
        flag=True
        i=n-1
    if flag:
        j=pos[check][i]
        for k in range(j+1,n):
            counter+=1
            if checker(i,k,pos[check]):
                flag=False
                pos[check][i]=k
                i+=1
                break
        else:
            pos[check][i]=-1
            i-=1
    else:
        for j in range(n):
            counter+=1
            if checker(i,j,pos[check]):
                pos[check][i]=j
                i+=1
                break
        else:
            flag=True
            pos[check][i]=-1
            i-=1
print(pos)
    
    
