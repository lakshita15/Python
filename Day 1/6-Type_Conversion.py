# birth_year = input("enter birth year")
# age = 2024 - birth_year
# print(age) #TypeError: unsupported operand type(s) for -: 'int' and 'str'

birth_year = input("enter birth year")
print(type(birth_year)) #=>print type class of string
age = 2024 - int(birth_year) # => data type(varname)=>>> it is called type conversion
print(type(birth_year)) #=>print type class of int
print(age) 