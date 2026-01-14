import math
radius=float(input("Enter the radius of the circle :"))
circumference=round(2*math.pi*radius,2)
area=round(math.pi*radius*radius, 2)
print(f"The circumference of the circle of radius {radius}cm is {circumference}square cm")
print(f"The area of the circle of radius {radius}cm is {area}square cm")