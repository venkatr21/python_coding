n = int(input())
flag = 1 if n<0 else 0
if n<0:
    n=-1*n
n=str(n)
n=n[::-1]
n=int(n)
n = -1*n if flag==1 else n
print(n)
