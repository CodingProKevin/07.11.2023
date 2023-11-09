def checkOP(string):
    global Opos 
    global OP
    counter = False

    for i in range(len(question)):
        if question[i] == "+" or question[i] == "-" or question[i] == "/" or question[i] == "*":
            counter = True
            Opos = i
            OP = question[i]
            return Opos
            
    if counter == False:
        print("Error, There is no operator")
        exit()

question = input("Enter your query(+,-,/,*):\n")

checkOP(question)

num1 = str("")
num2 = str("")
for i in range(len(question)):
    if question[i].isnumeric() == True and i < Opos:
        num1 = num1 + question[i]
    elif question[i].isnumeric() == True and i > Opos:
        num2 = num2 + question[i]

num1 = int(num1)
num2 = int(num2)
if OP == "+":
    total = num1 + num2
if OP == "-":
    total = num1 - num2
if OP == "/":
    try:
        total = num1 / num2
    except:
        print("You cannot divide these 2 number together")
if OP == "*":
    total = num1 * num2

print(total)