def year(m):
    if m%4==0 and m%100!=0 or m%400==0:
        return("Leap")
    else:
        return("Not a leap")
m=int(input("Enter a year"))
print(year(m))
