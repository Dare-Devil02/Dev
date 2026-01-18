#for loops execute a block of code for a fixed number of times
# you can iterate over a range, string, sequence, etc

#basic syntax
for x in range(1, 11):
    print(x)

#backwards 
for x in reversed(range(1,11)):
    print(x)

#step parameters
for x in range(1,11,2):
    print(x)


credit_card="1234-5678-9012-3456"
#string iteration
for x in credit_card:
    print(x)