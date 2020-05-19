def sortlist(w,small,large):
    if small==large:
        li.append(''.join(w))
    else :
        for i in range(small,large):
            w=list(w)
            w[small],w[i]=w[i],w[small]
            ''.join(w)
            sortlist(w,small+1,large)
            w=list(w)
            w[small],w[i]=w[i],w[small]
            ''.join(w)
    return li
if __name__=='__main__':
    test=int(input())
    ar=[]
    br=[]
    for i in range(test):
        a,b=list(map(int,input().strip().split()))
        ar.append(a)
        br.append(b)
    for i in range(test):
        li=[]
        word="a"*(ar[i]-2)+"b"*2
        li=list(sortlist(word,0,ar[i]-1))
        li.sort()
        print(li[ar[i]-br[i]-2])
        
