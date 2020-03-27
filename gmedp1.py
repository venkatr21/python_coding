arr=[]
arr=list(map(int,input().rstrip().split()))
fin=[]
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if i!=j and i!=k and j!=k:
                if arr[i]+arr[j]+arr[k]==0:
                    if sorted([arr[i],arr[j],arr[k]]) not in fin:
                        fin.append(sorted([arr[i],arr[j],arr[k]]))
print(fin)
