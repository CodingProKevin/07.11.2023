def calculate():
    num1 = input("Please enter your first number: ")
    while num1.replace(".", "").isnumeric() == False:
        print("You have not entered a valid value")
        num1 = input("Please enter your first number: ")

    operator = input("please choose an operator of the following:\n1)+\n2)-\n3)/\n4)*\n")
    while operator != "+" and operator != "-" and operator != "/" and operator != "*":
        print("You have not entered a correct operator")
        operator = input("please choose an operator of the following:\n1)+\n2)-\n3)/\n4)*\n")

    num2 = input("Please enter your second number: ")
    while num2.replace(".", "").isnumeric() == False:
        print("You have not entered a valid value")
        num2 = input("Please enter your second number: ")

    num1 = float(num1)
    num2 = float(num2)

    if operator == "+":
        solution = num1 + num2
    elif operator == "-":
        solution = num1 - num2
    elif operator == "/":
        try:
            solution = num1 / num2
        except:
            print("There is an error when dividing these numbers")
            return
            
    elif operator == "*":
        solution = num1 * num2

    print("The answer to",num1,operator,num2,"=",round(solution, 2))
    return


while True:
    calculate()