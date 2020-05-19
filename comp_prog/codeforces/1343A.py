   
n= int(input())
for i in range(n):
    tot = int(input())
    for j in range(2,tot+1):
        if tot%(2**j-1)==0:
            print(tot//(2**j-1))
            break
        
