x=2**1000
total=0
while x>0:
    total+=x%10
    x//=10
print (total)
