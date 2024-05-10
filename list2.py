#total nsum
#  n=[10,11,12,13,14,17,18,19]
# a=30
# i=0
# b=[]
# while i<len(n):
#     j=4
#     while j<len(n):
#         if n[i]+n[j]==a:
#             b.append([n[i],n[j]])
#         j=j+1
#     i=i+1
# print(b)        
    
# # report card
# marks=[
# [78, 76, 94, 86, 88],
# [91, 71, 98, 65, 76],
# [95, 45, 78, 42, 59]
# ]
# i=0
# sum=0
# m=len(marks[0]) and len(marks[1]) and len(marks[2]) 
# while i<m:
#     m1=marks[0][1]+marks[1][i]+marks[2][i]
#     # print(m1)
#     sum=sum+m1
#     i=i+1
# print(sum)  
# print(m1)     

# kitne admi the
# e = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# a=[]
# b=[]
# while i<len(e):
#     if e[i]%2==0:
#         a.append(e[i])
#     else:
#         b.append(e[i])
#     i=i+1
# print(a,"even")
# print(b,"odd")    

# odd even count
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


# n=[23,14,56,12,19,9,15,31,42,43]
# b=0
# c=0
# i=0
# a=0
# d=0
# while i<len(n):
#     if n[i]%2==0:
#         c=c+n[i]
#         a=c/len(n)
#     else:
#         b=b+n[i]
#         d=b/len(n)
#     i=i+1
# print(a,"even")            
# print(d,"odd")

# sum,count of odd ,even and total number
# n=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# s1=0
# s2=0
# b=0
# d=0
# while i<len(n):
#     if n[i]%2==0:
#         b=b+1
#         s1=s1+n[i]
#     else:
#         d=d+1
#         s2=s2+n[i]
#     i=i+1
# s=s1+s2
# c=b+d
# print("sum =",s1,"count =",b,"OF EVEN NUMBER")           
# print("sum =",s2,"count =",d,"OF ODD NUMBER")
# print("sum =",s,"count =",c,"OF ALL NUMBERS")

#kitne corore pati
# n=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100] 
# i=0
# c=0
# d=0
# e=0
# while i<len(n):
#     if n[i]>=10000000:
#         c=c+1
#     elif n[i]>=100000:
#         d=d+1
#     else:
#         e=e+1        
#     i=i+1
# print(c,"CROREPATI")
# print(d,"LAKHPATI")
# print(e,"DILWALE")    



c=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
# c=[1,1,1,1,1,3,4,5,6,4,3,3,2,4,5,7,7,4,3,2,2,2,3,4,4,8]
i=0
b=[]
a=[]
y=[]
while i<len(c):
    c1=0
    j=0
    while j<len(c):
        if c[i]==c[j]:
            b.append(c[i])
            c1=c1+1
        j=j+1
    k=0
    while k<1:
        if c[i]not in a:
            a.append(c[i])
#             #...print(c[i],"times",c1)
#             #...print((c[i],c1))
            y.append([c[i],c1])
        k=k+1
    i=i+1
print(y)               

# m=[[8,3,4],
#    [1,5,9],
#    [6,7,2,]]
# i=0
# b=15
# a=len(m[0]) and len(m[1]) and len(m[2])
# while i<a:
#     if m[0][0]+m[0][1]+m[0][2]==b:
#         if m[1][0]+m[1][1]+m[1][2]==b:
#             if m[2][0]+m[2][1]+m[2][2]==b:
#                 if m[0][0]+m[1][0]+m[2][0]==b:
#                     if m[0][1]+m[1][1]+m[2][1]==b:
#                         if m[0][2]+m[1][2]+m[2][2]==b:
#                             print("IT IS MAGIC SQUARE")
#                             break
#                         else:
#                              print("IT IS NOT MAGIC SQUARE")
#                              break
#                     else:
#                         print("IT IS NOT MAGIC SQUARE")
#                         break
#                 else:
#                     print("IT IS NOT MAGIC SQUARE")
#                     break
#             else:
#                 print("IT IS NOT MAGIC SQUARE")
#                 break
#         else:
#             print("IT IS NOT MAGIC SQUARE")
#             break
#     else:
#         print("IT IS NOT A MAGIC SQUARE")
#         break
#     i=i+1 


# a=[2,4,1,4]
# i=0
# while i<len(a):

        
# marks=[
# [78, 76, 94, 86, 88]
# [91, 71, 98, 65, 76]
# [95, 45, 78, 42, 59]
# ]
# i=0
# sum=0
# while i<len(marks):
#     j=0
#     k=0
#     while j<len(marks[i]):
#         k=k+(marks[i][j])
#         j=j+1
#     sum+=k    
#     i=i+1
# print(sum)    


# def birthdayCakeCandles(candles):
#     i=0
#     j=[]
#     d=0
#     while i<candles:
#         num=int(input("Enter the heights of candle"))
#         j.append(num)
#         k=j[0]
#         if k>j[i]:
#             d=d+1        
#         i=i+1    
#     print(j[i])  
# birthdayCakeCandles(4)  


# m=[[8,3,4],
#    [1,5,9],
#    [6,7,2,]]
# i=0
# p=len(m[0]) and len(m[1]) and len(m[2])
# while i <(p):
#     a=m[0][i]+m[1][i]+m[2][i]
#     # b=m[0][]
#     print(m)
#     sum=sum+m
#     i=i+1
# print(sum)    