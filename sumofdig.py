def sum_digits(n):
    s=0
    while n>0:
        rem=n%10
        s+=rem
        n//=10
    return s
n=int(input("Enter a number"))
print(sum_digits(n))


