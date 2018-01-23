def p(n):
    x=n*(3*n-1)/2
    return int(x)

h=[0,p(1),p(2)]
man=1
flg=0
while True:
    for i in range(man-1,1,-1):
        if h[i]<h[man]-h[man-1]:
            break
        if h[man]-h[i] in h:
            print (man,i , len(h))
            while h[man]+h[i]>h[len(h)-1]:
                h.append(p(len(h)))
            if h[man]+h[i] in h:
                print (h[man]-h[i],'324567644324234265')
                flg=1
                break
    if flg==1:
        break
    h.append(p(len(h)))
    man+=1
            
        
