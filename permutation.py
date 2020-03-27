li=[]
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
print(list(sortlist("aaabb",0,4)))
