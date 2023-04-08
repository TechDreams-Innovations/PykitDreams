def hello():
  
    name = str(input("Enter your name: "))
    
    print("Hello there " + str(name) + "! Welcome to PykitDreams V1.0 - a Python module designed to revolutionise the way you use your computers."))
    
    
def fourfunctionscalculator():  
    
    operation = input("Please enter the symbol for the operation you would like to complete: ")

    number_1 = int(input("Please enter your first number: "))
    number_2 = int(input("Please enter the second number: "))

    if operation == '+':
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print("{} / {} = ".format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("Invalid operator.")
