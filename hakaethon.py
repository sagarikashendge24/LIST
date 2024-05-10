a=[1,3,5,7,9]
x=max(a)
y=min(a)
l=sum(a)-x
b=sum(a)-y
print(l,b)


# def splitandjoin(line):
#     l=line.split(" ")
#     s="-".join(l)
#     return s
# splitandjoin("tis is string") 

# # a={}
# #

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     lst_marks=student_marks[query_name]
#     percent=sum(lst_marks)/len(lst_marks)
#     print('{p:1:2f}'.format(p=percent))

# a= ["Swati", "Muskan","Priyanka","amisha"]
# i=0
# j=0
# while i<len(a):
#     if j<len(a[i]):
#         j=len(a[i])
#         c=a[i]
#     i=i+1    
# print(c)    
        
