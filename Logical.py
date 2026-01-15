#logical operators
# and or not
temp=25
is_raining=False
if temp>35 or temp<0 or is_raining:
    print("The outdoor event is cancelled")

else:
    print("The outdoor event is still scheduled")

a=6
b=7




#conditional operators (ternary operator)
num=-5
print("positive" if num>0 else "negative")
result="Even" if num%2==0 else "Odd"
max_num=a if a>b else b
min_num=a if a<b else b
age=25
status="Adult" if age>=18 else "child"
weather="hot" if temp>20 else "cold"
user_role="Admin"
access_level="full access" if user_role=='Admin' else "limited access"
print(result)