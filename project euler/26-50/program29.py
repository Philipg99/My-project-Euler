lst=[]
for i in range(2,101):
    for j in range(2,101):
        lst.append(i**j)
print (len(list(set(lst))))
