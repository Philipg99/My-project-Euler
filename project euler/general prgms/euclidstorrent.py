def gcd(a, b):
    while b:
        a, b=b, a%b
    return a
def phi(a):
    b=a-1
    c=0
    while b:
        if gcd(a,b)==1:
            c+=1
        b-=1
    return c
