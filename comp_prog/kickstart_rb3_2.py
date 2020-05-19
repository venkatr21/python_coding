def parserst(his,st):
    if(len(his)==0):
        return(st)
    else:
        p=his.pop()
        le=len(st)
        i=st.rindex(')')
        retst = st[p+1:i]*int(st[p-1])
        print(st,p,i,retst)
        st = st[0:p-1]+retst+st[i+1:le]
        st=parserst(his,st)
    return(st)
            
testcase = int(input())
for i in range(testcase):
    st = input().strip()
    his=[]
    for j in range(len(st)):
        if(st[j]=='('):
            his.append(j)
    h=1
    w=1
    for i1 in parserst(his,st):
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
