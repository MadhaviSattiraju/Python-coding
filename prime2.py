import math
n=int(input('enter a number'))
for i in range(2,abs(int(math.sqrt(n)))+1):
    if n%i==0:
        print(n,'is not prime')
        break
else:
    print(n,'is a prime')

