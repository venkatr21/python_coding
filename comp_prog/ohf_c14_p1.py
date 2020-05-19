fin = input().strip()
n = int(input())
counter =0
i =1
ipos=1
while ipos<n*len(fin)-1:
    if fin[i-1]==fin[i] and fin[i]==fin[(i+1)%len(fin)]:
        counter+=1
        print(ipos)
        i+=2
        ipos+=2
        i=i%len(fin)
    elif fin[i-1]==fin[i]:
        counter+=1
        print(ipos)
        i+=2
        ipos+=2
        i=i%len(fin)
    elif fin[i]==fin[(i+1)%len(fin)]:
        i=i+1
        ipos+=1
        i=i%len(fin)
    else:
        i+=2
        ipos+=2
        i=i%len(fin)
if ipos==n*len(fin)-1:
    if fin[i-1]==fin[i]:
        counter+=1
print(counter)
        
