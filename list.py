l=[2,0,5,0,4,5]
j=len(l)-1
for i in l:
    if i==0:
        l.insert(j+1,0)
        l.remove(i)
    else:
        pass
print(l)

