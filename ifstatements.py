#if statements
age=int(input("Enter your age :"))
if age>18:
    print("You are signed up successfully")
elif age<0:
    print("You better born then try to sign up")
else:
    print("You must be 18+ to sign up")



response=input("Would you like some food? (Y/N) :")

if response=="Y" :
    print("Have some food")
else:
    print("No food for you!")




name=input("Enter your name :")
if name=="":
    print("You didn't typed your name")
else:
    print(f"Hello {name}")

#boolean conditional
for_sale=True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")


