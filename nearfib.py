def nearFib(n):
a,b = 0,1
while n >= b :
a,b = b,a+b
return b
print(nearFib(int(input())))
