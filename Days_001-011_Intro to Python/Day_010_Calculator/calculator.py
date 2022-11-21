from art import logo

#Add
def add(n1,n2):
    return n1+n2

#subtract
def subtract(n1,n2):
    return n1-n2

#Multiplty
def mult(n1,n2):
    return n1*n2

#Divide
def div(n1,n2):
    return n1/n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": mult, 
    "/": div
}


def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    more_math = True

    while more_math:
        operation_symbol = input("Pick an operation: ") 
        num2 = float(input("What is the second number?: "))
        func = operations[operation_symbol]
        answer = func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}: ") == 'y':
            num1 = answer
        else:
            more_math = False
            calculator()

calculator()