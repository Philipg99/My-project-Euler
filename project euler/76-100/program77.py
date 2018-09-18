
## quick copy paste of problem 76

target =100
ways=[1]
primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]


for i in range(target):
    ways+=[0]

for i in primes:
    for j in range(i,target+1):
        ways[j]+=ways[j-i]


for i in range(100):
    if ways[i]>5000:
        print(i)
        break

