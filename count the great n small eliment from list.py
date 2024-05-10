a=[28,17,16,9,7,88]
b=[30,8,9,4,8,9]
i=0
s=0
d=0
l=0
c=len(b) and len(a)
while i<c:
    if a[i]>b[i]:
        s=s+1
    elif b[i]>a[i]:
        d=d+1 
    else:
        l=0+0
    i=i+1
print(s)
print(d)       