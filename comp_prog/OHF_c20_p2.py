def minimumpush(arr, n):
    counter=0
    itematpos = n
    i=n-1
    while i>=0:
        if (arr[i] == itematpos): 
            itematpos -= 1
            i-=1
        else :
            temp = itematpos
            ind = arr.index(itematpos)
            arr2 = arr[ind+1:temp].copy()
            while arr[ind-1]==temp-1:
                ind-=1
                temp-=1
            while arr[i]!=itematpos:
                ele=max(arr2)
                if ele>temp:
                    arr2.remove(ele)
                    arr=[ele]+arr[0:arr.index(itematpos)+1]+arr2+arr[arr.index(itematpos)+1:len(arr)]
            counter+=1
        print(arr)
    return counter
n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input().strip()))
print(minimumpush(arr, n))
