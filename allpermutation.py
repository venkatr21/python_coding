def permute(arr,l,r):
    if l==r:
        print(''.join(arr))
    else:
        for i in range(l,r+1):
            arr[i],arr[l]=arr[l],arr[i]
            permute(arr,l+1,r)
            arr[i],arr[l]=arr[l],arr[i]
def start():
    print("Enter the input string")
    ch=input().strip()
    print("The permutations are:")
    permute(list(ch),0,len(ch)-1)
    input()
if __name__ == '__main__':
    start()
