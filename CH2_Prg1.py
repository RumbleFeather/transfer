#Joshua Anderson
#CH2 Practice Prg1
#This will calculate the a student's remaning credits to graduate

name = input("Enter the student's name: ")
degree = input("Enter the name of the degree program: ")
creds = 64 - float(input('Enter the number of credits completed: '))

print("Pass'em State College")
print(name + " is in the " + degree + " program and has " + str(creds) + " credits left to graduate")