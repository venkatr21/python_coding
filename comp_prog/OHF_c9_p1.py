n = int(input())
st = input().strip().split(' ')
st = [int(i) for i in st]
counter=0
fin=[]
for i in range(len(st)):
    new = st.copy()
    new.remove(new[i])
    sume = sum(new)
    for j in range(len(new)):
        newsum = sume-new[j]
        if new[j]==newsum:
            counter+=1
            fin.append(str(i+1))
            break
print(counter)
x=" ".join(fin)
print(x)
        
