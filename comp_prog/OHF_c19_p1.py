n = int(input())
st = input().strip().split()
st = [int(i) for i in st]
l=[]
st.sort()
flag=True
if st[0]==1 and st.count(st[1])!=(n-1):
    flag = False
elif st[0]==1 and st.count(st[n-1])==(n-1):
    flag = True
elif st[n-1]==(n-1):
    if (st[0]==(n-1) or (st[0]==(n-2) and st.count(n-2)==(n-2))):
        flag = True
    else :
        flag= False
else:    
    for i in range(n):
        if i==0:
                l.append(st[i])
                l.append(st[i]+1)
        else:
            if (st[i] not in l) and (st[i]+1) not in l:
                flag = False
                break
if flag:
    print("Yes")
else:
    print("No")
            
        
