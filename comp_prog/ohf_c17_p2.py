n = int(input())
st = input().strip()
di = {'R':[],'G':[],'B':[]}
for i in range(len(st)):
    if st[i]=='R':
        di['R'].append(i+1)
    elif st[i]=='G':
        di['G'].append(i+1)
    else:
        di['B'].append(i+1)
red = list(di['R'])
green = list(di['G'])
blue = list(di['B'])
fin=[]
for i in range(len(red)):
    for j in range(len(green)):
        for k in range(len(blue)):
                fin.append((max(red[i],green[j],blue[k])-min(red[i],green[j],blue[k])))
print(fin.count(min(fin)))
