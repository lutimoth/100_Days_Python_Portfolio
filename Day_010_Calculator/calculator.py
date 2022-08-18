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

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

for symbol in operations:
    print(symbol)
    
operation_symbol = input("Pick an operation from the line above: ") 

func = operations[operation_symbol]
answer = func(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")