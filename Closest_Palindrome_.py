def palin(n):
    rev=0
    t=n
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    if t==rev:
        return 1
    else:
        return 0
n=int(input())
for i in range(n-1,0,-1):
    if palin(i):
        a=i
        break
m=n+1
while m!=0:
    if palin(m):
        b=m
        break
    m+=1
if n-a<b-n:
    print(a)
elif n-a>b-n:
    print(b)
elif n-a==b-n:
    print(a,b)