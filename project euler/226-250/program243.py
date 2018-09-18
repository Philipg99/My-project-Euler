from time import time as ta
wa=ta()

pri=[2,3,5,7,11,13,17,19,23,29,31,37]


def toi(n,pri):
    p=n
    for i in pri:
        if n%i==0:
            p*=(1-1/i)
    return int(p)

n=1
for i in pri:
    n*=i
    if (toi(n,pri)/n-1)<15499/94744:
        print(n)
    print(n,'3e')
    
    
print(ta()-wa)
