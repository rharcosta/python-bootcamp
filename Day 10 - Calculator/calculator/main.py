from art import logo
from replit import clear

print(logo)

def init():
    first_number = float(input("\nFirst number: "))

    start = True
    while start:
        operation = input("\nPic an operator (+, -, *, /): ")
        second_number = float(input("\nNext number: "))
    
        def calculations(n1, n2, operator):
            if operator == "+":
                return n1 + n2
            elif operator == "-":
                return n1 - n2
            elif operator == "*":
                return n1 * n2
            elif operator == "/":
                return n1 / n2
            else:
                return "Invalid operator"
    
        result = calculations(first_number, second_number, operation)
        print(f"\n{first_number} {operation} {second_number} = {result}")
        answer = input(f"\nType 'Y' to continue calculating with {result} or type 'N' to start a new calculation: ").upper()
        if answer == "Y":
            first_number = result 
        else:
            clear()
            init()

init()