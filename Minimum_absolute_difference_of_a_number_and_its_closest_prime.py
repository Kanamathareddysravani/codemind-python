def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
z=n
for i in range(n,1,-1):
    if prime(i):
        m=i
        break
while z!=0:
    if prime(z):
        y=z
        break
    z+=1
if n-m>y-n or n-m==y-n:
    print(y-n)
elif n-m<y-n:
    print(n-m)