import tictactoe
import allpermutation
print('welcome')
print('MENU!!\n1.Play TICTACTOE\n2.Permute Strings\n3.Quit')
ch=int(input())
if ch==1:
    tictactoe.start()
if ch==2:
    allpermutation.start()
else :
    print('thankyou')
    input()
