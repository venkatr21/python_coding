def call(st,start,coun):
    if len(st)==2:
        coun[0]+=1
    else:
        for i in range(start,len(st)//2):
            ele = st.pop(i)
            for j in range(len(st)-1,len(st)//2-1,-1):
                if st[j]==ele:
                    ele1 = st.pop(j)
                    call(st,i,coun)
                    st.insert(j,ele1)
            st.insert(i,ele)
                
n=int(input())
st=input().strip()
st=list(st)
l1=[]
l2=[]
ele=[0]
for i in st:
    if st.count(i)%2 !=0:
        print(0)
        break
else:
    call(st,0,ele)
print(ele[0]//2)

