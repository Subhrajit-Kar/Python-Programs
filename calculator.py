# simple calculator program for performing basic mathematical operations (+,-,*,/) using MATCH CASE

def user_input():
    x = float(input("Enter First Number:    "))
    y = float(input("Enter Second Number:   "))
    return x, y 
 
print("<<<<<<<<<<<-----AVAILABLE CHOICES----->>>>>>>>>>>:\n")
print("\t\t1. Addition")
print("\t\t2. Subtraction")
print("\t\t3. Multiplication")
print("\t\t4. Division")
print("\n")

choice = int(input("Enter your Choice:  "))
if 1 <= choice <= 4 :
    x, y = user_input()
    match choice:
        case 1:
            print("You have chose to add the Numbers !!")
            output = x + y 
            print("Result:  ", output)
        case 2:
            print("You have chose to subtract the Numbers !!")
            output = x - y 
            print("Result:  ", output)
        case 3:
            print("You have chose to multiply the Numbers !!")
            output = x * y 
            print("Result:  ", output)
        case 4:
            print("You have chose to divide the Numbers !!")
            if  y != 0:
                output = x/y
                print("Result:  ", output)
            else:
                print("!!!ERROR!!!! Zero cannot be a divisor")
else:
    print("...INVALID CHOICE...")