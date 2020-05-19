def querycalc(quer,points,a,b):
    if quer=='X':
        for i in range(a,min(len(points),b+1)):
            if points[i]==1:
                points[i]=4
            elif points[i]==2:
                points[i]=3
            elif points[i]==3:
                points[i]=2
            else :
                points[i]=1
    if quer=='Y':
        for i in range(a,min(len(points),b+1)):
            if points[i]==1:
                points[i]=2
            elif points[i]==2:
                points[i]=1
            elif points[i]==3:
                points[i]=4
            else :
                points[i]=3
    return points
from collections import Counter
n=int(input())
points=[]
for i in range(n):
    temp=input().strip().split(' ')
    temp=[int(ele) for ele in temp]
    x = temp[0]
    y = temp[1]
    if x>0 and y>0:
        points.append(1)
    elif x<0 and y>0:
        points.append(2)
    elif x>0 and y<0:
        points.append(4)
    elif x<0 and y<0:
        points.append(3)
    else:
        points.append([1,2,3,4])
queries=[]
q=int(input())
for i in range(q):
    queries.append(input().strip().split())
for i in queries:
    if i[0]!='C':
        points=querycalc(i[0],points,int(i[1])-1, int(i[2])-1)
    else:
        d1 =[]
        for j in range(int(i[1])-1, min(len(points),int(i[2]))):
            d1.append(points[j])
        dic = Counter(d1)
        for j in range(1,5):
            if j not in dic.keys():
                dic[j]=0
        strings = []
        for j in range(1,5):
            strings.append(str(dic[j]))
        print(" ".join(strings))
            
        
        
        
