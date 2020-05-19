def calculate(arr,n,k):
    if min(arr)>=k:
        return 0
    else :
        counte = 0
        temp = k
        for i in range(n):
            if arr[i]==temp:
                if temp == 1:
                    counte+=1
                    temp= k
                else:
                    temp-=1
        return counte
                
            
test  = int(input())
n=[]
k=[]
arr=[]
for i in range(test):
    n1,k1 = list(map(int,input().strip().split()))
    arr1 = list(map(int, input().strip().split()))
    n.append(n1)
    k.append(k1)
    arr.append(arr1)
st=[]
for i in range(test):
    st.append(calculate(arr[i],n[i],k[i]))
for i in range(test):
    print("Case #{}: {}".format(i+1,st[i]))
