lst=[]

i=1
while 3*i<1000:
    if 5*i<1000:
        lst.append(5*i)
    if ((3*i) not in lst):
        lst.append(3*i)
    i+=1
print (sum(lst))
