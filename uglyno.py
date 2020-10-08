def ugly(n):
    if n==0:
        return False
    for i in[2,3,5]:
        while n%i==0:
            n/=i
        return True
n=int(input(""))
print(ugly(n))

