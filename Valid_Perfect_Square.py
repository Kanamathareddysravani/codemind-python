t=int(input())
for i in range(t):
    a=int(input())
    flag=0
    for j in range(1,a+1):
        if a==j*j:
            flag=1
            break
    if (flag==0):
        print("False")
    else:
        print("True")