#To calculate perimeter/circumference and area of shapes such as triangle, rectangle,square and circle.

shape_name = input("Please enter the name of shape you want to find area for: triangle, rectangle , square or circle :  ")
shape_name.lower()

if shape_name == "triangle" :
   base =   float(input("Enter base : "))
   height = float(input("Enter height : "))
   area = 0.5*base*height
   side1 = float(input("Enter side 1 : "))
   side2 = float(input("Enter side 2 : "))
   side3 = float(input("Enter side 3 : "))
   perimeter = side1+side2+side3
   print(f"Area of triangle is {area} and the perimeter is {perimeter}")

elif shape_name == "rectangle" :
   length =   float(input("Enter length : "))
   breadth = float(input("Enter breadth : "))
   perimeter = 2 * (length + breadth)
   area = length * breadth
   print(f"Area of rectangle is {area} and the perimeter is {perimeter}")

elif shape_name == "square" :
   side =   float(input("Enter side : "))
   perimeter = 4 * side
   area = side * side
   print(f"Area of square is {area} and the perimeter is {perimeter}")

elif shape_name == "circle" :
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * 3.14 * radius
    area = 3.14 * radius ** 2
    print(f"Area of the circle is {area} and the Circumference of the circle is {circumference}")

else:
   print("Invalid input")
   
