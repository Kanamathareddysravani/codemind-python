n=int(input())
a=0
b=1
c=a+b
while c<n:
    c=a+b
    a=b
    b=c
if b==n:
    print('True')
else:
    print('False')