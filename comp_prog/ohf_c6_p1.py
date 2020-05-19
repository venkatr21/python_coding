def func(l,counter,i):
    if l==[0]*len(l):
        return counter
    else:
        if l[i]==1:
            counter = counter+1
            m = l
            m.pop(i)
        else :
            counter = counter+2
            m = l
            m[i] = m[i]-1
        for j in range(len(m)):
            if m[j]!=0:
                for k in range(m[j]):
                    return(func(m,counter,j))
    return(counter-1)

s= input().strip().split(' ')
m , l = [int(i) for i in s]
s = input().strip().split(' ')
s = [int(i) for i in s]
l = []
for i in range(len(s)-1):
    if(s[i+1]-s[i])!=1:
        l.append(s[i+1]-s[i]-1)
counts=0
for i in range(len(l)):
    counts += func(l,0,i)
print(counts%1000000007)

