def checker(l):
    dic={'cakewalk':0,'simple':0,'easy':0,'easy-medium':0,'medium':0,'medium-hard':0,'hard':0}
    for i in l:
        dic[i]+=1
    if dic['cakewalk']==1 and dic['simple']==1 and dic['easy']==1 and (dic['easy-medium']==1 or dic['medium']==1) and (dic['medium-hard']==1 or dic['hard']==1):
        return 1 
    else:
        return 0

#*******************************************************************************
test=int(input())
for i in range(test):
    n=int(input())
    l=[]
    for j in range(n):
        l.append(input())
    res=checker(l)
    if res==1:
        print('Yes')
    else:
        print('No')
