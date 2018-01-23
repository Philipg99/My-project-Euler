x=1
x+=365%7
print(x)
dt={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
count =0
for y in range(1901,2001):
    for i in range(1,13):
        if x==0:
            count+=1
        if i==2 and y%4==0 and y%400!=0:
            x=(x+29%7)%7
        else:
            x=(x+dt[i]%7)%7

print (count)
        
        
