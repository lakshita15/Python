#Write a Python program to swap two variables.
"""
1. defne 2 variables
2. assign values
3. swap values
"""
#approach 1 
"""x=10
y=5

x1=x ("x1 is temporary variable to copy value of x")
x=y
y=x1

print("value of x after swap is " , x)
print("value of y after swap is " , y)
"""
#approach 2, without using third variable 
x=10
y=5

x,y=y,x

print("value of x after swap is " , x)
print("value of y after swap is " , y)

