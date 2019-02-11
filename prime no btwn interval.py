n,k=map(int,input().split())
for i in range(n,k+1):
    if n>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
