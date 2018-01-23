x=7
count =0
i=1
while count <500:
    n=x*(x+1)/2

    count =0
    i=1
    while i*i<=n: ## very impotant i*i
        if n%i==0:
            count+=2
        i+=1
    x+=1



print (n)



    
    
	
