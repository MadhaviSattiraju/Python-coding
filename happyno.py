n=int(input('enter number:'))
def num(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r**2
        n=n//10
    return(s)
   
while(n>=10):
    k=num(n)
    if k==1 or k==7:
        print('yes')
        break
    else:
        n=k
else:
    print('no')







n=int(input())
sum1=0
def xyz(n):
    sum1=0
    if(n==1 or n==7):
        return ("yes")
    else:
        while(n>0):
            num=n%10
            sum1+=num**2
            n=n//10
        return(xyz(sum1))
print(xyz(n))
