print("Temperature Converter")
unit=input("select Input unit (C or F) :")
temp=float(input("Enter temperature :"))
if unit=='c' or unit=='C':
    temp=round((9*temp)/5+32,2)
    print(f"The temperature in Fahrenheit is {temp}F")
elif unit=='F' or unit=='f':
    temp=round((temp-32)*5/9,2)
    print(f"The temperature in celsius is {temp}C")
else:
    print(f"{unit} is not valid")