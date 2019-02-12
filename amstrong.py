n= int(input())
summ=0
t=n
while t>0:
    digit=t%10
    summ=summ+digit**3
    t=t//10
if n==summ:
    print("yes")
else:
    print("no")
