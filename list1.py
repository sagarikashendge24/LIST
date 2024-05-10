# a=[1,2,3,4,5,6,24]
# b=[2,3,1,0,6,7]
# i=0
# z=[]
# while i<len(a):
#     m=a[i]
#     if m not in b :
#         z.append(m)
#     i=i+1
# print(z)     

# =[1,2,3,4,5,6]
# b=[2,3,1,0,6,7]
# i=0
# z=[]
# while i<len(a):
#     c=a[i]
#     if c not in b:
#         z.append(c)
#     i=i+1
# print(z)        

# n=int(input("enter"))
# n=[1,0,0,1,1,1,1,1,1,1,0,0]
# n1=0
# i=1
# while n!=0:
#     rem=n%10
#     n1=n1+(rem*i)
#     n=int(n/10)
# print(n1)    

# n=int(input("enter"))
# n1=0
# i=1
# while n!=0:
#     rem=n%10
#     n1=n1+(rem*i)
#     n=int(n/10)
# print(n1)    
        
# i=0
# while i<=len(a):
#     j=0
#     while i<=len(a[0]):
#         j=j+1
#     s=0
#     while i<=len(a[1]):
#         s=s+1
#     i=i+1
# print(s)
# print(j)              


# n=[23,14,56,12,19,9,15,31,42,43]
# b=0
# c=0
# i=0
# while i<len(n):
#     if n[i]%2==0:
#         c=c+n[i]
#     else:
#         b=b+n[i]
#     i=i+1
# print(c,"even")            
# print(b,"odd")

# n=[30,2,311,34,2,1,34,5,6,4,23,45,66]
# i=0
# a=n[0]
# while i<len(n):
#     if n[i]>a:
#         a=n[i]
#     i=i+1    
# print(a)  
  

# a=int(input("enter the nu"))
# b=int(input("enter the number"))
# i=0
# c=a
# while i<b:
#     c=c+b
#     i=i+1
# print(c)    

# a=[28,17,16,9,7,88]
# b=[30,8,9,4,8,9]
# i=0
# s=0
# d=0
# l=0
# c=len(b) and len(a)
# while i<c:
#     if a[i]>b[i]:
#         s=s+1
#     elif b[i]>a[i]:
#         d=d+1 
#     else:
#         l=0+0
#     i=i+1
# print(s)
# print(d)             

l= ["Swati", "Muugfdiuoudooiskan"," Priyanka","Amishavishwa"]
# i=0
# j=0
# while i<len(l):
#     if j<len(l[i]):
#         j=len(l[i])
#         p=l[i]
#     i=i+1
# print(p)
i=0
j=0
while i <len(l):
    j=j+len(l[i])
    print(l[i],j)
    j=0
    i=i+1


     
