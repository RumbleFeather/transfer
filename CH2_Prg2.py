#Joshua Anderson
#CH2 Practice Prg2
#This will calculate the MPG for a car trip

begOdo = float(input("Enter the beginning odometer reading: "))
endOdo = float(input("Enter the ending odometer reading: "))
gallons = float(input("Enter the number of gallons used: "))

miles = endOdo - begOdo
mpg = miles/gallons

print()
print("U Auto Know")
print(f'MPG for the last {miles:.2f} miles is  {mpg:.2f}')