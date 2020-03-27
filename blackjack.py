import random
from os import system
cate=['spade','heart','diamond','clubs']
cards=['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
val={'ace':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10}
dl=[]
pl=[]
win=True
winner='none'
play={1:'player',2:'Computer'}
chance=1
def gameplay():
    if chance==1:
def pick():
    ct=random.choice(cate)
    cd=random.choice(cards)
    print(ct+'-'+cd)
    return cd
def start(win):
        dl.append(pick())
        dl.append(pick())
        pl.append(pick())
        pl.append(pick())
        while win :
            system('cls')
            print('Dealer:{}'.format(dl))
            print('Player:{}'.format(pl))
            print(f'{play[1]} plays')
            gameplay()
            
start(win)
            
        
    

    
