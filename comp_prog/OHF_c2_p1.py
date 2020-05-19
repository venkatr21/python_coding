def knapsack(m,weights,profits,n):
    if n==0 or m==0:
        return 0
    if weights[n-1]>m:
        return knapsack(m,weights,profits,n-1)
    
    else:
        return max(profits[n-1]+knapsack(m-weights[n-1],weights,profits,n-1),
                    knapsack(m,weights,profits,n-1))



n,m=map(int,input().split(' '))
p=input()
p=p.split(' ')
p=[int(ele) for ele in p]

value=input()
value=value.split(' ')
value=[int(ele) for ele in value]

num=input()
num=num.split(' ')
num=[int(ele) for ele in num]

profits=[]
weights=[]
k = sum(num)
for i in range(0,n):
    for j in range(0,num[i]):
        profits.append(value[i])

for i in range(0,n):
    for j in range(0,num[i]):
        weights.append(p[i])

ch=knapsack(m,weights,profits,n)
print(ch)
