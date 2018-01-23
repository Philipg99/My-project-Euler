dictunit={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
dicteens={0:3,1:3,2:3,3:3,4:4,5:3,6:4,7:4,8:3,9:4}
dictens={0:0,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
hun=len('hundredand')
total =len('onethousand')

for i in range(1,1000):
    x=i%10
    total+=dictunit[x]
    i//=10
    if i!=0:
        y=i%10
        if y==1:
            total+=dicteens[x]
        else:
            total+=dictens[y]
        i//=10
        if i!=0:
            z=i%10
            total+=hun+dictunit[z]
            if x==0 and y==0:
                total-=3
print (total)
            
