for t in range (int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in range (n):
        try:
            if i!=0 and i!=n-1 and arr[i]>arr[i+1] and arr[i]>arr[i-1]:
                c+=1
        except IndexError:
            pass
    print("Case #{}: {}".format(t+1,c))