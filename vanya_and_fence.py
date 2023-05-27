n, h = map(int, input().split())

f = list(map(int, input().split()))

contor=0
for i in f:
    if i<=h:
        contor+=1
    else:
        contor+=2

print(contor)
    
