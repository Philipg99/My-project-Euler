f=[1,1]
count=0

for i in range(1000):
    f[0],f[1]=f[0]+f[1]*2,f[0]+f[1]
    if len(str(f[0]))>len(str(f[1])):
        count+=1

print(count)
