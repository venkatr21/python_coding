def finder(s,t,f,b):
    if sorted(s[i])!=sorted(t[i]):
        return('cannot be formed')
    else:
        a=''
        mini=0
        s=list(s)
        while len(s)>0:
            ele = s.pop(0)
            first = f.pop(0)
            last = b.pop(0)
            a1=ele+a
            a2=a+ele
            if(t.find(a1)!=-1 and t.find(a2)!=-1):
                if(first<=last):
                    a=a1
                    mini+=first
                else:
                    a=a2
                    mini+=last
            elif t.find(a1)!=-1:
                a=a1
                mini+=first
            elif t.find(a2)!=-1:
                a=a2
                mini+=last
            else:
                return('cannot be formed')
        return(mini)
                    
            

test = int(input())
s=[]
t=[]
f=[]
b=[]
for i in range(test):
    n=int(input())
    s.append(input().strip())
    t.append(input().strip())
    f.append(list(map(int,input().strip().split())))
    b.append(list(map(int,input().strip().split())))
    res = finder(s[i],t[i],f[i],b[i])
    print(res)
    
    
