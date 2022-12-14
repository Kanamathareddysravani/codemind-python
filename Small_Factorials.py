t=int(input())
for i in range(t):
    a=int(input())
    fact=1
    for j in range(1,a+1):
        fact=fact*j
    print(fact)