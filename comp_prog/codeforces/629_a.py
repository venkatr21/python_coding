if __name__=='__main__':
    test=int(input())
    ar=[]
    br=[]
    for i in range(test):
        a,b=list(map(int,input().strip().split()))
        ar.append(a)
        br.append(b)
    for i in range(test):
        if(ar[i]%br[i]==0):
            print(0)
        else:
            print((br[i]*((ar[i]//br[i])+1))-ar[i])
