
##https://www.wolframalpha.com/input/?i=n%5E2-m%5E2-2nm-n%2Bm) integer solution
import time
t=time.time()
def nr(k):
    e1=(3-2*(2**0.5))
    e2=(3+2*(2**0.5))
    d=4*(2**0.5)
    return (e1**k +e2**k)/d


def nb(k):
    e1=(3-2*(2**0.5))
    e2=(3+2*(2**0.5))
    return (2*(e1**k) + (2**0.5)*(e1**k) + 2*(e2**k) - (2**0.5)*(e2**k) + 4)/8


i=1
n=0
while n<10**12:
    n=round(nb(i))+round(nr(i))
    i+=1


print(round(nb(i-1)))

print(time.time()-t)

##better solution in thread 100
##b=15
##r=6
##
##def check(b,r):
##    pn=b*(b-1)
##    pd=(b+r)*(b+r-1)
##    print(b,r)
##    print(pn/pd)
##
##
##for i in range(18):
##    r,b=2*b+r-1,5*b+2*r-2
##    check(b,r)
    
