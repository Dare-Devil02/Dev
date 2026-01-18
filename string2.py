#indexing = accessing elements of a sequence using [] (indexing operator)
#[start:end:step]
credit_number="1234-5678-9012-3456"
print(credit_number[0])
print(credit_number[0:4])#ending index is excluded
print(credit_number[5:9:2])
print(credit_number[5:])#print everything till the ending
print(credit_number[-1])#from the last of the string
print(credit_number[::2])#everything at the step of 2 
print(credit_number[::-1])#everything from the last