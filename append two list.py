n=[[1,8,9,0],[5,8,9,0]]
i=0
c=[]
while i<len(n):
    j=0
    l=n[i]
    while j<len(l):
        k={l:j}
        c.update(k)
        j=j+1
    i=i+1
print(c)        

# while i<len(n):
#     if n[i] not in m:
#         c.append(n[i])
#     i=i+1
# print(c)        