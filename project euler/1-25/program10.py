s=0
for i in range (2,2000000):
    sqr = int(i**0.5) +1
    flg=0
    for x in range (2,sqr):
        if i%x==0:
            flg=1
            break
    if flg==0:
        s+=i

print (s)
