n=int(input())
rev=0
c=0
res=0
while n:
    r=n%10
    rev=rev*10+r
    n//=10
while rev:
    r=rev%10
    if r==6 and c==0:
        r=9
        c+=1
    res=res*10+r
    rev//=10
print(res)