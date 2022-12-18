def reve(n):
    rev=0
    while n:
        rev=rev*10+n%10
        n//=10
    return rev
n=int(input())
if n>0:
    print(reve(n))
else:
    n=n*(-1)
    c=reve(n)
    c=str(c)
    print("-"+c)