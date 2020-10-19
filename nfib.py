def fib(n):
    x=0
    y=1
    z=0
    while z<=n:
        x,y=y,z
        z=x+y
    print(z)
n=int(input("Enter a number"))
fib(n)
