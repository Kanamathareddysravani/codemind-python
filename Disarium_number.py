import math
n=int(input())
l=int(math.log10(n))+1
sum=0
k=n
while n:
    r=n%10
    sum+=r**l
    n//=10
    l-=1
if sum==k:
    print('True')
else:
    print('False')