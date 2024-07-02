#Write a function to add two numbers and return the result.

sum = 0
def addition(num1,num2):
    sum = num1 + num2
    return sum

number1 = int(input("Enter num 1- "))
number2 = int(input("Enter num 2- "))
print(addition(number1,number2))