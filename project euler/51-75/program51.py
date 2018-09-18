import re
from time import time as t 
x=input()

s='inininininininininininininininininininin'
c=0
for i in range(len(s)-len(x)+1):
    if s[i:i+len(x)]==x:
            c+=1
w=t()
print(len(re.findall(x,s)))
print(t()-w)
