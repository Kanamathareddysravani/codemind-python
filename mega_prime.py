n=int(input())
for i in range(2,n):
    if n%i==0:
        print('Not Mega Prime')
        break
else:
    d,p=0,0
    while n:
        r=n%10
        n//=10
        d+=1
        if r==2 or r==3 or r==5 or r==7:
            p+=1
if d==p:
    print('Mega Prime')
else:
    print('Not Mega Prime')