import math
def calculate(arr):
    counter=0
    for i in range(len(arr)):
        sume=0
        for j in range(i,len(arr)):
            sume+=arr[j]
            sr = math.sqrt(sume) 
            if (sr - math.floor(sr)) == 0:
                counter+=1
    return counter
                
test = int(input())
arr=[]
for i in range(test):
    n = input()
    arr.append(list(map(int,input().strip().split())))
st=[]
for i in range(test):
    st.append(calculate(arr[i]))
for i in range(test):
    print("Case #{}: {}".format(i+1,st[i]))

