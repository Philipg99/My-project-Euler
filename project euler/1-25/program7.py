lst=[]
i=2
while len(lst)<10002:

    sqr=int(i**0.5)+1

    flg=0
    for x in range(2,sqr):
        if i%x==0:
            flg=1
    if flg==0:
        lst.append(i)
    i+=1
print (lst[10000])
            
        
