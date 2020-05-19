def binaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal
g=int(input())
l=[]
ans=[-1]*g
for i in range(g):
    l.append(binaryToDecimal(int(input())))
print(l)
visited = []
ansr=[]
for i in range(len(l)):
    if i not in visited:
        for j in range(i,len(l)):
            if i&j>0:
                ansr.append(-1)
                break
            else:
                ansr.append(1)
                visited.append(i)
                visited.append(j)
                break
            
    else:
        ansr.append(1)
        
                
