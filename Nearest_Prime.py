def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
t=int(input())
for i in range(t):
    n=int(input())
    m=n
    for j in range(n,1,-1):
        if prime(j):
            a=j
            break
    while m!=0:
        if prime(m):
            b=m
            break
        m+=1
    if (n-a>b-n):
        print(b)
    elif (n-a<=b-n):
        print(a)