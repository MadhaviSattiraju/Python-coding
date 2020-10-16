n=int(input("enter a number"))
r1=int(input("enter a starting range"))
r2=int(input("enter a ending range"))
if r1<r2:
    for i in range(r1,r2+1):
        print(n,'*',i,'=',n*i)
else:
    for i in range(r1,r2-1,-1):
        print(n,'*',i,'=',n*i)

