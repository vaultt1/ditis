#1. Write a Python Program find an area of a rectangle and perimeter of the rectangle.


length=int(input("Enter Length of Rectangle\n"))
breadth=int(input("Enter Breadth of Rectangle\n"))

area_of_rectangle = length*breadth
perimeter_of_rectangle = 2*(length+breadth)


print(f"Area of rectangle is: {area_of_rectangle}")
print(f"Perimeter of rectangle is: {perimeter_of_rectangle}")