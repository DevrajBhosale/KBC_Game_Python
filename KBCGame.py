questions = [
    ["1. What is the full form of DBMS?","a) Data of Binary Management System",
        "b) Database Management System",
        "c) Database Management Service",
        "d) Data Backup Management System","b"],

    ["2. What is DBMS?","a) DBMS is a collection of queries",
        "b) DBMS is a high-level language",
        "c) DBMS is a programming language",
        "d) DBMS stores, modifies and retrieves data","d"],

    ["3. Who created the first DBMS?","a) Edgar Frank Codd",
        "b) Charles Bachman",
        "c) Charles Babbage",
        "d) Sharon B. Codd","b"],
    
    ["4. Which type of data can be stored in the database?","a) Image oriented data",
        "b) Text, files containing data",
        "c) Data in the form of audio or video",
        "d) All of the above","d"],
    
    ["5. Which of the following is not a type of database?", "a) Hierarchical",
        "b) Network",
        "c) Distributed",
        "d) Decentralized","d"]
]

prices = [100,200,300,400,500]
money = 0
for i in range(len(questions)):
    question = questions[i]
    print(f"Question for price {prices[i]} is:\n")
    print(f"{question[0]}")
    print(f"{question[1]}         {question[2]}")
    print(f"{question[3]}         {question[4]}")
    reply = input("Enter the Correct Answer option: ")
    if(reply != "a" and reply != "b" and reply != "c" and reply != "d"):
        print("Entered Option is Incorrect ")
        break
    else:
        if(reply == question[-1]):
            print(f"Correct Answer, you have won Rs. {prices[i]}")
            money = prices[i]
        else:
            print("Wrong Answer")
            money = prices[i-1]
            break

print(f"Your Take away money is {money}")