def rotator(ch,l):
  if l[0]=='L':
    while l[1]>0:
      ch=ch[1:]+ch[0:1]
      l[1]-=1
  else :
    while l[1]>0:
      ch=ch[-1:]+ch[0:len(ch)-1]
      l[1]-=1
  return ch
ch=input()
di1={}
for i in ch:
  if i not in di1.keys():
    di1[i]=1
  else :
    di1[i]+=1
trial=int(input())
test=''
while trial>0:
  l=input().split()
  l[1]=int(l[1])
  ch=rotator(ch,l)
  test=test+ch[0]
  trial-=1
di2={}
for i in test:
  if i not in di2.keys():
    di2[i]=1
  else :
    di2[i]+=1
if di1==di2:
  print('YES')
else :
  print('NO')
