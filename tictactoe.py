from os import system
def printer(l):
    print("   |   |   ")
    print(f' {l[6]} | {l[7]} |{l[8]} ')
    print("   |   |   ")
    print('------------')
    print("   |   |   ")
    print(f' {l[3]} | {l[4]} |{l[5]} ')
    print("   |   |   ")
    print('------------')
    print("   |   |   ")
    print(f' {l[0]} | {l[1]} |{l[2]} ')
    print("   |   |   ")
    return l
def inserter(key,l,p1,p2):
    flag=1
    while flag==1:
        print(f'player{key} enter the number(position) [1-9]')
        ch=int(input())-1
        if l[ch]!=' ':
            print('wrong choice!enter again')
        else:
            flag=0
    if key==1:
        l[ch]=p1
        key=2
    else:
        l[ch]=p2
        key=1
    return key
def checker(win,l,p1):
    if l[0]==l[1]==l[2]!=' ' or l[3]==l[4]==l[5]!=' ' or l[6]==l[7]==l[8]!=' ' or l[0]==l[3]==l[6]!=' ' or l[1]==l[4]==l[7]!=' ' or l[2]==l[5]==l[8]!=' ' or l[0]==l[4]==l[8]!=' ' or l[2]==l[4]==l[6]!=' ':
        if l[0]==p1 or l[3]==p1 or l[6]==p1 or l[1]==p1 or l[2]==p1:
            system('cls')
            l=printer(l)
            print('player 1 wins')
            input()
            win=1
        else:
            system('cls')
            l=printer(l)
            print('player 2 wins')
            input()
            win=1
    elif ' ' not in l:
        l=printer(l)
        print('Match draw')
        input()
        win=1
    else:
        pass
        win=0
        system('cls')
    return win
    
def start():       
    l=[' ']*9
    print('TIC-TAC-TOE GAME')
    print('Select symbol for player 1(X or O):')
    p1=input()
    p2='O' if (p1=='X' or p1=='x') else 'X'
    if (p1=='X' or p1=='x'):
        key=1
        print('Player 1 will start')
    else:
        key=2
        print('player 2 will start')
    win=0
    while win==0:
        l=printer(l)
        key=inserter(key,l,p1,p2)
        win=checker(win,l,p1)
if __name__ =='__main__':
    start()
