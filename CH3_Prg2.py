rate = float(input("Enter the current insurance rate: "))



if rate > 0 and rate < 3000:
    age = int(input("Enter age: "))
    
    if age >= 16 and age <= 90:
        accidents = int(input("Enter the number of accidents: "))
        
        if accidents >= 0 and accidents <= 5:
        
            if age >= 30 and accidents < 5:
                discount = rate * .10
                print(f"Congraulations, you are entitled to a ${discount:,.2f}")
                print("Thank you for Driving Safely")
    
            else:
                print("You do not qualify for a discount at this time.") 



    
    