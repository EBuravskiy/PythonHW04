print("Enter the sides of the rectangle:")
print("Side A:")
a = float(input())
print("Side B:")
b = float(input())
area = a*b
perimeter = 2*(a+b)
if area%1 == 0: 
    area = int(area)
if perimeter%1 == 0:
    perimeter = int(perimeter)
print("The area of ​​the rectangle is", area)
print("The perimeter of the rectangle is", perimeter)