def arm_no(n):
    arm=0
    n1=n
    while n>0:
        rem=n%10
        arm+=rem*rem*rem
        n//=10
    if n1==arm:
        return('Armstrong')
    else:
        return('Not an Armstrong')
n=int(input("Enter a number"))
print(arm_no(n))

