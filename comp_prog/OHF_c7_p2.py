test = int(input())
for i in range(test):
    n =int(input())
    arr=[]
    for s in range(n):
        st = input().strip().split(' ')
        st = [int(j) for j in st]
        arr.append(st)
    val=0
    for s in range(len(arr[0])):
        pro=1
        for k in range(1,n):
            if arr[0][s] in arr[k]:
                if len(arr[k])==1:
                    pro = 0
                    break
                pro = pro*(len(arr[k])-1)
            else :
                pro = pro*len(arr[k])
            print(pro,val)
        val = val+pro
    print(val)
            
        
    
