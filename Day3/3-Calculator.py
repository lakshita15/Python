operation = input("enter the operation +,-,* or /")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if operation == '+' :
    print("addition", number_1+number_2)

elif operation == '-':
    print("subtraction", number_1 - number_2)

elif operation == '*':
    print("multiply", number_1 * number_2) 
elif operation == '/':
    print("divide", number_1 / number_2)
else:
    print("invalid")
