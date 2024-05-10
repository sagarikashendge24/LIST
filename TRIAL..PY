print("🙏🏻WELCOME TO KBC🙏🏻")
print("🏆⚡KON BANEGA CODEPATI⚡🏆")
print()
question=["🔹Q1.How many continents are there❓",              
        "🔹Q2.What is the capital of India❓",         
        "🔹Q3.NG mei kaun se course padhaya jaata hai❓"]
option=[["1.Four", "2.Nine", "3.Seven", "4.Eight"],
        ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
        ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution= [3, 4, 1] 
answer=["3.Seven","4.Eight","3.Chennai","4.Delhi","1.Software Engineer","2.Counseling"]
i=0
amount=100000
count=0
b=0
a=1
while i<len(question):
    print(question[i])
    j=0
    k=1
    while j<len(option[i]):
        print(option[i][j])
        j=j+1
    lifeline=input("DO YOU WANT LIFELINE❤ ")   
    if lifeline=="YES" :
            print("5️⃣ 0️⃣ 5️⃣ 0️⃣")
            if count==0:
                    print("❤️",answer[b+i])
                    print("❤️",answer[b+a])
                    num=int(input("ENTER THE ANSWER"))
                    if num ==solution[i]:
                            print("YOUR ANSWER IS RIGHT✔️")
                            print(amount)
                    else:
                            print("YOUR ANSWER IS WRONG❌")  
                            print("YOU LOOSE THE GAME😕😔")
                            break 
                    amount=amount+500000           
                    count=count+1
                    print()
            else:
                    print("YOUR HAD ALREADY USED LIFELINE😕")
                    e=int(input("ENTER THE ANSWER"))
                    if e==solution[i]:
                            print("YOUR ANSWER IS RIGHT✔️")
                            print(amount)
                    else:
                            print("YOUR ANSWER IS WRONG❌")
                            print("YOU LOOSE THE GAME😕😔")
                            break
    else:
            f=int(input("ENTER THE ANSWER"))
            if f==solution[i]:
                    print("YOUR ANSWER IS RIGHT✔️")
                    print(amount)
            else:
                    print("YOUR ANSWER IS WRONG❌ ")
                    print("YOU LOOSE THE GAME😕😔")
                    break
            amount=amount+500000    
            print()                
    i=i+1
    a=a+1
    b=b+1                 
print("🏆YOU WON🏆",amount,"💸💸") 
print("THANK YOU FOR PLAYING🤝")