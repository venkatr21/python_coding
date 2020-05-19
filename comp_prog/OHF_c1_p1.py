# Enter your code here. Read input from STDIN. Print output to STDOUT
a= []
n, k = list(map(int,input().strip().split()))
a = list(map(int,input().strip().split()))
vis = [k]
ind = 0
while ind<len(vis):
    for i in range(len(a)):
        if a[i] not in vis:
            if(a[i]&vis[ind])!=0:
                vis.append(a[i])
    ind = ind+1
vis = set(vis)
a= set(a)
fin= a.difference(vis)
print(len(fin))
