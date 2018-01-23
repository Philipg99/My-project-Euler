count=0
for i in range(33,354294):
    st=list(map(int,list(str(i))))
    st=list(map(lambda x:x**5,st))
    st=sum(st)
 
    if st==i:
        print(st)
        count+=st
print (count)
