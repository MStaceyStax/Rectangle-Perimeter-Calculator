import calculator
    
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculator.area(length, width)
perimeter = calculator.perimeter(length, width)

print(f"the area of the rectangle is: {area}")
print(f"the perimeter of the rectangle is {perimeter}")

