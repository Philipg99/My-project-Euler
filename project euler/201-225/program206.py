def cond(n):
    n=str(n)
    for i in range(9):
        if n[i*2]!=str(i+1):
            return False
    return True


l=int(10203040506070809**0.5)
u=int(19293949596979899**0.5)

for i in range(u-1,l,-2):
    if (i-1)%1000000==0:
        print (i-1)
    if cond(i**2):
        print (i*10)
        break

