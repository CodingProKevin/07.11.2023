def checkOP(string):
    global Opos 
    global OP
    Opos = []
    OP = []
    counter = False

    for i in range(len(question)):
        if question[i] == "+" or question[i] == "-" or question[i] == "/" or question[i] == "*":
            counter = True
            Opos.append(i)
            OP.append(question[i])
            
    if counter == False:
        print("Error, There is no operator")
        exit()
    return 

question = input("Enter your query(+,-,/,*):\n")

checkOP(question)

numbers = []
numX = ""
for i in range(len(OP)):
    if i-1 < 0:
        for x in range(len(question)):
            if question[x].isnumeric() == True and x < Opos[i]:
                numX = numX + question[x]
        numbers.append(numX)
        numX = ""

    if i-1 >= 0 and i != len(OP):
        for x in range(len(question)):
            if question[x].isnumeric() == True and x < Opos[i] and x > Opos[i-1]:
                numX = numX + question[x]
        numbers.append(numX)
        numX = ""

    if i+1 >= len(OP):
        for x in range(len(question)):
            if question[x].isnumeric() == True and x > Opos[i]:
                numX = numX + question[x]
        numbers.append(numX)
        numX = ""

print(numbers)



total = 0
for i in range(len(OP)):
    if OP[i] == "/" and total == 0:
         total = int(numbers[i]) / int(numbers[i+1])
    elif OP[i] == "/":
        total = total / int(numbers[i])

for i in range(len(OP)):
    if OP[i] == "*" and total == 0:
         total = int(numbers[i]) * int(numbers[i+1])
    elif OP[i] == "*":
        total = total * int(numbers[i])

for i in range(len(OP)):
    if OP[i] == "+" and total == 0:
         total = int(numbers[i]) + int(numbers[i+1])
    elif OP[i] == "+":
        total = total + int(numbers[i])
        
for i in range(len(OP)):
    if OP[i] == "-" and total == 0:
         total = int(numbers[i]) - int(numbers[i+1])
    elif OP[i] == "-":
        total = total - int(numbers[i])

print(total)