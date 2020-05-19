n,m=map(int,input().split(' '))
l=[]
sports=[[] for i in range(m)]
for i in range(n):
    temp=input().split(' ')
    temp=[int(ele) for ele in temp]
    l.append(temp)
for i in range(m):
    for j in range(n):
        sports[i].append(l[j][i])
        sports[i] = list(set(sports[i]))
    
    
