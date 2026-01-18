p=0
r=0
t=0
while True:
    p=float(input("Enter the principal amount :"))
    if p<=0:
        print("Principal can't be less than or equal to zero")
    else:
        break

while True:
    r=float(input("Enter the rate of interest :"))
    if r<=0:
        print("Rate can't be less than or equal to zero")
    else:
        break

while True:
    t=float(input("Enter the time in years :"))
    if t<=0:
        print("Time can't be less than or equal to zero")
    else:
        break

#compound interest logic
amt=p*pow(1+(r/100),t)
print(f"Amount Invested :{p}")
print(f"Interest Earned {(amt-p):.2f}")
print(f"Total Corpus after {t} years at the rate of {r} = ${amt:.2f}")