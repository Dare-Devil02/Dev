#lbs to kg
print("Weight converter")
weight=float(input("Enter weight :"))
unit=input("Given weight is in Kilograms or pounds? (K or L)")
if unit=="K"or unit=="k":
    weight=round(weight*2.205,2)
    print(f"Your weight is {weight}lbs")

elif unit=='L'or unit=='l':
    weight=round(weight/2.205,2)
    print(f"Your weight is {weight}Kg")

else:
    print(f"{unit} is invalid")
