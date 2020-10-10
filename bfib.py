def beforefib(n):
    a,b=0,1
    while b<=n:
        c=a+b
        a=b
        b=c
        print(a,b)
    return b
n=int(input())
print(n)
print(beforefib(n))
