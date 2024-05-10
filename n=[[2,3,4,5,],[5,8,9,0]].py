n=[[2,3,4,5,],[5,8,9,0]]
# i=0
# c=[]
# while i<len(n):
#     j=i
#     while j<len(n[i]):
#         c.append(j)
#         j=j+1
#     i=i+1
# print(c)        

i=0
a=[]
while i<len(n):
    if i not in a:
        a.extend(n[i])
    i=i+1
print(a)    