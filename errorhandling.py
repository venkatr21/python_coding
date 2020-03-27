print('welcome')
try:
    a=int(input('a value:'))
    b=int(input('b value:'))
    c=a/b
except ZeroDivisionError :
    print('b shouldd not be 0.')
except TypeError :
    print('no spaces allowed here')
except ValueError :
    print(' a and b should be integers')
except :
    print('other errors')
else:
    print(f'{a}/{b}result is {c}')
