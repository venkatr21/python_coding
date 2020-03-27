n=int(input())
amt=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
lis=[]
lis.append(0)
for i in range(0,d+1):
  for j in range(0,c+1):
    for k in range(0,b+1):
      for l in range(0,a+1):
        if (l*100+k*200+j*500+i*1000)==amt and (i+j+k+l)<=n:
          lis.append(i+j+k+l)
print(max(lis))
