def eval(arr,dire,l,t):
    timec = 0
    while timec<t:
        dircopy=dire.copy()
        arrcopy=arr.copy()
        for i in range(len(arr)):
            flag=1
            j=0
            while j<len(arr):
                if j!=i and arr[i]==arr[j] and dire[i]==(dire[j]%2+1):
                    dire[i]=dire[i]%2+1
                    dire[j]=dire[j]%2+1
                    break
                elif j!=i and arr[i]==(arr[j]+1)%l and dire[i]==2 and dire[j]==1:
                    dircopy[i]=dircopy[i]%2+1
                    flag=0
                    break
                elif j!=i and arr[i]==(arr[j]-1 if arr[j]!=0 else l-1)%l and dire[i]==1 and dire[j]==2:
                    dircopy[i]=dircopy[i]%2+1
                    flag=0
                    break
                else:
                    j+=1
            if flag==1:                        
                if dire[i]==1:           
                    arrcopy[i]=(arrcopy[i]+1)%l
                else:
                    arrcopy[i]=(l-1) if (arrcopy[i]==0) else arrcopy[i]-1
        arr = arrcopy.copy()
        dire = dircopy.copy()
        print(arr,dire)
        timec+=1
    return arr
st = input().strip().split()
n,l,t  = [int(i) for i in st]
arr=[]
dire=[]
for i in range(n):
    st = input().strip().split()
    a,b  = [int(i) for i in st]
    arr.append(a)
    dire.append(b)
carr = arr.copy()
arr = eval(arr,dire,l,t)
for i in arr:
    print(i)
    
