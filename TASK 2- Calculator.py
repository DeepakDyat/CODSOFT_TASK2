#TASK 2
#Calculator

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


print("Select Operations")
print(
    "1. Addition\n"\
    "2. Subtraction\n"\
    "3. Multiplication\n"\
    "4. Division\n")

choice = int(input("Enter choice of operation"))

n1 = int(input("Enter the First Number: "))
n2 = int(input("Enter the Second Number: "))

if choice == 1:
    print (n1, "+", n2, "=", addition(n1, n2))

elif choice == 2:
    print (n1, "-", n2, "=", subtraction(n1, n2)) 

elif choice == 3:
    print (n1, "*", n2, "=", multiplication(n1, n2)) 
    
elif choice == 4:
    print (n1, "/", n2, "=", division(n1, n2)) 
    
else:
    print("Invalid Input")