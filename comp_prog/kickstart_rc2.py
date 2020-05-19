from collections import Counter
r=int(input())
c = int(input())
st=[]
for i in range(r):
    st.append(list(input().strip()))
dicc = Counter(st)
