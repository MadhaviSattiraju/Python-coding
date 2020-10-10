a='madhavi'
b='548'

for i in range(4):
    li=input("Enter the login id")
    pw=input("Enter the password")

    if li==a and pw==b:
        print("logged in successfully")
        break
    else:
        print("wrong credentials")
else:
    print("blocked for 24 hours")

