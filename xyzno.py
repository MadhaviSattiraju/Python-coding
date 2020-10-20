n=int(input())
num=n
sum1=0
sum2=0
while(num>0):
    nu=num%10
    sum1+=nu**2
    num//=10
for i in range(2,n//2):
    if(n%i==0):
        sum2+=i
if(sum1==sum2):
    print("yes")
else:
    print("no")

