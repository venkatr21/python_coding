n=int(input())
l=[]
for i in range(n):
    l.append(input())
di={}
for i in l:
    k=''.join(sorted(i))
    if k not in di.keys():
        di[k]=[i]
    else :
        di[k].append(i)
for i in di.keys():
    print(di[i])
