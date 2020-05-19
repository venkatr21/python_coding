def calculate(st,coun):
    i=0
    while i<len(st):
        if st[i]==0:
            st.pop(i)
        else :
            i+=1
    if len(st)==0:
        return coun
    else :
        if len(st)<max(st):
            while len(st)<max(st):
                st.remove(max(st))
            return calculate(st,coun+1)
        else:
            for i in range(len(st)):
                st[i] -=1
            return calculate(st,coun+1)

n = int(input())
st = input().strip().split()
st = [int(i) for i in st]
coun=calculate(st,0)
print(coun)
