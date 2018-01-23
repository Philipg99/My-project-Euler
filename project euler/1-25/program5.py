##fact=[]
##
##for num in range(2,21):
##    lst=[]
##    i=2
##    while True:
##        if i>num:
##            break
##        if num%i==0:
##            while num%i==0:
##                lst.append(i)
##                num/=i
##        i+=1
##    fact +=list(set(lst) - set(fact))
##
##print(fact)
##    

fact={}
for i in range (2,21):
    fact[i]= fact.get(i,0)
for num in range(2,21):
    lst={}
    i=2
    while True:
        if i>num:
            break
        if num%i==0:
            while num%i==0:
                lst[i]= lst.get(i,0)+1
                num/=i
        i+=1
    for prime in lst:
        if lst[prime]>fact[prime]:
            fact[prime]=lst[prime]
##print (fact)
num=1
for k in fact:
    if fact[k]!=0:
     num*=(k**fact[k])

print (num)
