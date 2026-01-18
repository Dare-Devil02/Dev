name=input("Enter your full name :");
result=len(name)#returns length of the string
print(result)
result=name.find(" ")#find the index in the string
print(result)
result=name.rfind("O")#reverse finding from the string
#-1 return for no result
name=name.capitalize()
print(name)
name=name.upper()
print(name)
name=name.lower()
result=name.isdigit()#returns true if string contains only digits
result=name.isalpha()#return true for only characters in the string (no whitespaces)
phone_number=input("Enter your phone number : ")
result=phone_number.count("-")#counts number of dashes in the string
phone_number=phone_number.replace("-"," ")#replace first value with the second
print(help(str))#returns all the functions available in the given function