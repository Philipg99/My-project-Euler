def t(n):
    x=n*(n+1)/2
    return int(x) 
def p(n):
    x=n*(3*n-1)/2
    return int(x)
def h(n):
    x=n*(2*n-1)
    return int(x)

pt=285
pp=165
ph=143
while True:
    ph+=1
    while p(pp+1)<=h(ph):
        pp+=1
    while t(pt+1)<=h(ph):
        pt+=1
    if h(ph)==p(pp) and h(ph)==t(pt):
        break
print(h(ph),p(pp),t(pt))
