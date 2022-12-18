def selfnumber(n):
    c,d=0,0
    tem=n
    while n:
        r=n%10
        if r!=0 and tem%r==0:
            c+=1
        n//=10
        d+=1
    if d==c:
        print(tem,end=' ')
a=int(input())
b=int(input())
for i in range(a,b+1):
    selfnumber(i)
