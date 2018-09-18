##i dont remember my thinking behind this 
s=0
for i in range(1,16):
    s+=(i-1)
    for j in range(i+1,16):
        s+=i*j
        for k in range(j+1,16):
            s+=i*j*k
            for l in range(k+1,16):
                s+=i*j*k*l
                for m in range(l+1,16):
                    s+=i*j*k*l*m
                    for n in range(m+1,16):
                        s+=i*j*k*l*m*n
                        for o in range(n+1,16):
                            s+=i*j*k*l*m*n*o
f16=1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16
print(f16/s)
                
