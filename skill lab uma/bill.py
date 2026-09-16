def calculate_bill(units):
    bill_amt=0
    if units<=100:
        bill_amt=units*2
    elif units<=200:
        bill_amt=(100*2)+((units-100)*3)
    elif units<=300:
        bill_amt=(100*2)+(100*3)+((units-200)*5)
    elif units>300:
        bill_amt=(100*2)+(100*3)+(100*5)+((units-300)*7)
    return bill_amt


units=int(input("Enter the units: "))
bill=calculate_bill(units)
if bill<100:
    print(f"Your Electricity bill is 100")
else:
    print(f"Your Electricity bill is {bill}")