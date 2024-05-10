n=[12,3,4,32,13,57,97,34,22,11,0,87,65,7]
i=0
s=0
g=n[0]
while i<len(n):
    s=s+n[i]
    if n[i]>g:
        g=n[i]
    if n[i]<g:
        f=n[i]        
    i=i+1 
print(s,"IS SUM")  
print(g,"IS LARGEST")
print(f,"IS SMALLER")    
