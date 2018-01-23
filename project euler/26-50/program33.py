
full=[]
for i in range(1,10):
    temp=[]
    for j in range(1,10):

        temp+=[i*10+j,j*10+i]
    full+=[temp]
sp=[]
for sub in full:
    for i in range(18):
        for j in range(i+1,18):
  ##          print(sub[i],sub[j],(i+2)//2,(j+2)//2)
            if sub[i]/sub[j]==((i+2)//2)/(((j+2)//2)):
                if sub[i]!=sub[j]:
                    sp+=[sub[i],sub[j]]
print (sp)
        
