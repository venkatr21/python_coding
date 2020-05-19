def eval(arr,c,k):
    counter = 0
    while len(arr)>0:
        pos = arr[0]+k
        popcount=1
        while len(arr)>0 and popcount<=c and arr[0]<=pos:
            arr.pop(0)
            popcount+=1
        if popcount>1:
            counter +=1
    return counter

st = input().strip().split()
n,c,k  = [int(i) for i in st]
arr=[]
for i in range(n):
    arr.append(int(input()))
result = eval(arr,c,k)
print(result)
