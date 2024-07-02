'''
def greet_user():
    print("hello")
    print("welcome")


print("start")
greet_user()
print("finish")

'''

#Passing positional parameters
'''
def greet_user(Firstname, Lastname):
    print(f"hello {Firstname} {Lastname}")
    print("welcome")


print("start")
greet_user("John", "Doe")
print("finish")
'''
#Passing keyword arguements:- they improe the readability of code, makes it easier to read in case we have a lot of arguements in a function

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If mixing both positional and keyword arguments, we should always define positional argument first, and then write the respective keyword arguments
'''
def greet_user(Firstname, Lastname):
    print(f"hello {Firstname} {Lastname}")
    print("welcome")


print("start")
greet_user(firstname="John", "Doe") =>this is wrong
print("finish")
'''

# you can return the value from a function in python, if nothing is returned  the default value that is returned from a function is none that is similar to the null Keyword in Java C++, Or c

'''
def square(number):
    print(number*number)
    #return number*number

# square_is = square(3)
# print(square_is)
print(square(3)) 

'''

