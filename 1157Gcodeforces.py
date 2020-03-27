def invert(no,mo,*li):
    if mo==0:
        for i in range(m):
            if li[no][i]==0:
                li[no][i]=1
            else:
                li[no][i]=0
        rowd[no]=1 if rowd[no]==0 else 0
    else:
        for i in range(n):
            if li[i][mo]==0:
                li[i][mo]=1
            else:
                li[i][mo]=0
        cold[mo]=1 if cold[mo]==0 else 0
    return li
            
[n,m]=input().split()
n=int(n)
m=int(m)
rowd=[0 for i in range(n)]
cold=[0 for i in range(m)]
li=[]
for i in range(n):
    li.append(input().split())
for i in range(n):
    for j in range(m):
        li[i][j]=int(li[i][j])
li=invert(int(input()),int(input()),li)
print(li)
print(rowd)
print(cold)
