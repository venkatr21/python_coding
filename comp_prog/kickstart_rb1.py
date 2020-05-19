testcase = int(input())
for i in range(testcase):
    c= int(input())
    counter=0
    l=[]
    l = list(map(int,input().strip().split()))
    for j in range(1,c-1):
        if(l[j-1]< l[j] and l[j+1]<l[j]):
            counter +=1
    print("Case #{} : {}".format(i+1,counter))
