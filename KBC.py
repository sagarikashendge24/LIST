# question=["How many continents are there?",              
#         "What is the capital of India?",         
#         "NG mei kaun se course padhaya jaata hai?"]
# options=[["Four", "Nine", "Seven", "Eight"],
#         ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#         ["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
# solution= [3, 4, 1] 
# answer=["3.Seven","4.Eight","3.Chennai","4.Delhi","1.Software Engineer","2.Counseling"]
# i=0
# a=1
# b=0
# count=0
# amount=10000
# while i<len(question):
#     print(question[i])
#     j=0
#     k=1
#     while j<len(options[i]):
#         print(answer[i][j])
#         j=j+1
#     lifeline=input("DO YOU WANT 5050 LIFELINE")
#     if lifeline=="YES":
#         print("5050")
#         if count==0:
#             print(answer[b+i])
#             print(answer[b+a])
#             num =int(input("ENTER THE ANSWER"))
#             if num==solution[i]:
#                 print("YOUR ANSWER IS CORRECT")
#             else:
#                 print("YOUR ANSWER IS WROMG")    
#             count+=1
#         else:
#             print("YOU HAD ALREADY USED LIFELINE")
#             e=int(input("ENTER NUMBER"))
#             if e==solution[i]:
#                 print("YOUR ANSWER IS CORRECT")
#             else:
#                 print("YOUR ANSWER IS WRONG")     
#     elif lifeline=="NO" :
#         f=int(input("CHOOSE THE CORRECT ANSWER"))
#         if f==solution[i]:
#             print("YOUR ANSWER IS CORRECT")
#         else:
#             print("YOUR ANSWER IS WRONG")
#     else:
#         print("NOTHING")
#     print("YOU WON",amount)
#     amount*=i
#     i=i+1
#     a=a+1
#     b=b+1                                  
