mat=0
for i in range(1,100):
    for j in range(1,100):
        t=sum(list(map(int,list(str(i**j)))))
        if t>mat:
            mat=t
print(mat)
	
