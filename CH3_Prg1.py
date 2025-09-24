#Joshua Anderson
#CH2 Practice Prg1
#this will calculate a discount for different patrons

cType = input("Enter Customer Type: ")
subtotal = float(input("Enter Subtotal: "))

if cType == "R" or cType == "r":
    if subtotal < 100:
        discount = 0
        
    elif subtotal < 250:
        discount = .10
        
    else:
        discount = .25
        
else:
    
    if cType == "C" or cType == "c":
        
        if subtotal < 250:
            discount = .20
            
        else:
            discount = .30
            
    else:
        
        if cType == "T" or cType == "t":
            
            if subtotal < 500:
                discount = .40
                
            else: 
                discount = .50
            
        else:
            discount = .10

discAmount = subtotal * discount
total = subtotal - discAmount

print()
print("Invoice total: ")
print()
print(f"Discount Percent: {discount:.0%}")
print(f"Discount Amount: ${discAmount:.2f}")
print(f"Total:           ${total:,.2f}")