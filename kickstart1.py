test=int(input())
for i in range(test):
    n,k=list(map(int,input().strip().split()))
    li=[]
    vals=[[] for i in range(26)]
    for j in range(n):
        li.append(input().strip())
        vals[(ord(li[j][0]))-65].append(li[j])
 
