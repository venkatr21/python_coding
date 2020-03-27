n=int(input())
counter=0
if n>9:
    n=n-9
    counter+=1
    while n>=20:
        n=n-20
        counter+=1
    if n%2:
        print(counter)
    else:
        print(n//2-1)
else:
    print(n)
