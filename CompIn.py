def compintrst(p,t,r):
    A=p*(pow((1+r/100),t))
    CI=A-p
    return CI
p=int(input("enter p"))
t=int(input("enter t"))
r=int(input("enter r"))
print(compintrst(p,t,r))

    

