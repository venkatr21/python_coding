n=int(input())
cases = int(input())
x=[]
y=[]
t=[]
h=[]
for i in range(cases):
    st=input().strip().split()
    st = [int(i) for i in st]
    x.append(st[0])
    y.append(st[1])
    t.append(st[2])
    h.append(st[3])
result=[]
arr=[[0 for i in range(n//2+1)]for j in range(n//2+1)]
arr[0][0]=1
for times in range(max(t)):
    for i in range(min(n//2+1,times)):
        for j in range(min(n//2+1,times)):
            if arr[i][j]==1:
                if i==n//2+1 or j==n//2+1:
                    if i==n//2+1 and j==n//2+1:
                        arr[i][j-1]+=1
                        arr[i-1][j]+=1
                        arr[i][j]+=2
                    elif i==n//2+1:
                        arr[i][j]+=1
                        arr[i][j-1]+=1
                        arr[i][j+1]+=1
                    elif j==n//2+1:
                        arr[i-1][j]+=1
                        arr[i+1][j]+=1
                        arr[i][j]+=1
                elif i==0 or j==0:
                    if i==0 and j==0:
                        arr[i][j+1]+=1
                        arr[i+1][j]+=1
                    elif i==0:
                        arr[i][j-1]+=1
                        arr[i][j+1]+=1
                        arr[i+1][j]+=1
                    else:
                        arr[i-1][j]+=1
                        arr[i+1][j]+=1
                        arr[i][j+1]+=1
                elif i==j:
                    if i<times-1:
                        arr[i-1][j]+=1
                        arr[i+1][j]+=1
                        arr[i][j-1]+=1
                        arr[i][j+1]+=1
                else :
                    arr[i-1][j]+=1
                    arr[i+1][j]+=1
                    arr[i][j-1]+=1
                    arr[i][j+1]+=1
                
                    
                    
                
    
    
