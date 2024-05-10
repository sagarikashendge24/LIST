n=[1,1,1,1,1,2,2,2,3,3,3,3,6,6,6,6,6]
i=0
a=[]
while i<len(n):
    j=0
    count=0
    while j<len(n):
        if n[i]==n[j]:
            
            count+=1
        j+=1
    if n in a:
        i+=1
        continue
    a.append(n[i])
    print(n[i],count)
print(a)

        
