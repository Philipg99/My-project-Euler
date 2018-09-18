target =100
ways=[1]

for i in range(target):
    ways+=[0]

for i in range(1,target):
    for j in range(i,target+1):
        ways[j]+=ways[j-i]

print(ways[100])
