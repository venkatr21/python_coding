from collections import Counter
def dummypal(ch):
    di=Counter(ch)
    di=dict(di)
    ceven=0
    codd=0
    for i in di.values():
            if i%2==0:
                ceven+=0
            else:
                codd+=1
    
    if c==3 or c==0:
        return True
    else :
        return False
test=int(input())
while test:
    ch=input()
    key=dummypal(ch)
    if key:
        print("DPS")
    else :
        print("!DPS")
    test-=1
