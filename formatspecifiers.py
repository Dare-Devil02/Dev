#format specifiers={value:flags} format a value based on what flags are inserted
price1=3.14159
price2=-987.65
price3=12.34
print(f"Price 1 is ${price1:.2f}")#number of decimal places
print(f"Price 2 is ${price2:10}")#number of spaces in the value
print(f"Price 3 is ${price3:010}")#numbers preceded with 0
print(f"Price 3 is ${price3:<10}")#numbers have spaces at the last
print(f"Price 3 is ${price3:>10}")#numbers have spaces at the start
print(f"Price 3 is ${price3:^10}")#value is now centred
print(f"Price 3 is ${price3:+}")#positive value is preceded with '+' sign 
print(f"Price 3 is ${price3: }")#numbers have spaces  
print(f"Price 3 is ${price3:,}")#thousands separaters
print(f"Price 3 is ${price3:+,.2f}")#values can be combined with comma