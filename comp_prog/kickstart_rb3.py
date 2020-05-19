def parserst(st):
    his=[]
    i=0
    while i<len(st):
        le = len(st)
        if(st[i] == '('):
            his.append(i)
            i=i+1
        elif(st[i] == ')'):
            p=his.pop()
            st = st[0:p-1]+st[p+1:i]*int(st[p-1])+st[i+1:le]
            i=len(st[0:p]+st[p+1:i]*int(st[p-1]))-1
        else:
            i=i+1
    return(st)
testcase = int(input())
for i in range(testcase):
    st = input().strip()
    h=1
    w=1
    for i1 in parserst(st):
        if(i1=='N'):
            if(h==1):
                h=10**9
            else:
                h=h-1
        elif(i1=='S'):
            if(h== 10**9):
                h=1
            else:
                h=h+1
        elif(i1=='W'):
            if(w==0):
                w=10**9-1
            else:
                w=w-1
        else:
            if(w== 10**9):
                w=1
            else:
                w=w+1
    print("Case #{}: {} {}".format(i+1,w,h))
