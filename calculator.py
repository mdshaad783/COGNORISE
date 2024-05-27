def sum(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        print("Zero Division Error")
    else:
        return x/y
    
num1 = float(input("Enter 1st Number :\n"))  
num2 = float(input("Enter 2nd Number :\n"))
choice = input("Please select an operation :-\nEnter 1 for Addition....Enter 2 for Subtraction....Enter 3 for Multiplication....Enter 4 for Division....\n")

if choice == '1':
    print("Result : ",sum(num1,num2))
elif choice == '2':
    print("Result : ",sub(num1,num2))
elif choice == '3':
    print("Result : ",mult(num1,num2))
elif choice == '4':
    print("Result : ",div(num1,num2))
else:
    print("Invalid Choice!!")