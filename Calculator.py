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
while True:
    question = input("Enter your query(+,-,/,*):\n")

    if question == "exit" or question == "q":
        exit()

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
            
    while ('/' in OP):
        for x,y in enumerate(OP):
            if y == "/":
                try:
                    numbers[x] = int(numbers[x]) / int(numbers[x+1])
                    numbers.remove(numbers[x+1])
                    OP.remove(y)
                    break
                except:
                    print("The was an error with dividing")
                    exit()
    while ('*' in OP):        
        for x,y in enumerate(OP):
            if y == "*":
                numbers[x] = int(numbers[x]) * int(numbers[x+1])
                numbers.remove(numbers[x+1])
                OP.remove(y)
    while ('+' in OP) or ('-' in OP):
        for x,y in enumerate(OP):
            if y == "+":
                numbers[x] = int(numbers[x]) + int(numbers[x+1])
                numbers.remove(numbers[x+1])
                OP.remove(y)
                break
            if y == "-":
                numbers[x] = int(numbers[x]) - int(numbers[x+1])
                numbers.remove(numbers[x+1])
                OP.remove(y)
                break
    print(numbers[0])