arr=input().rstrip()
flag=0
ansr=""
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        brr=arr[i:j+1]
        if brr==brr[::-1] and len(brr)>len(ansr):
            flag=1
            ansr=brr
if flag==0:
    print("error")
else:
    print(ansr)
    
    
    
