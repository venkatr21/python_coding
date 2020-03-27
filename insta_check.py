followers_list=[]
following_list=[]
print('Enter no of followers')
followers=int(input())
print('Enter no of following')
following=int(input())
print('Enter followers')
for i in range(followers):
    followers_list.append(input())
print('Enter following')
for i in range(following):
    following_list.append(input())
l1=set(followers_list)
l2=set(following_list)
l1.difference(l2)

    
