
# Simple Python Calculator

def operation(a, b, c):
   if c == '+':
        print(f'\nSum of {a} and {b} is {a+b}')
   elif c == '-':
        print(f'\nDifference of {a} and {b} is {a-b}')
   elif c == '*':
        print(f'\nProduct of {a} and {b} is {a*b}')
   elif c == '/':
        if b == 0:
            print("\nError: Cannot divide by zero, Try again")
            Calculator()
        else:
            print(f'\nQuotient of {a} and {b} is {a/b}')
   elif c == '%':
        if b == 0:
            print("\nError: Cannot find the remainder of a division by zero, Try again")
            Calculator()
        else:
            print(f'\nRemainder of {a} and {b} is {a%b}')
   elif c == '**':
        print(f'\n{a} to the power of {b} is {a**b}')
   else:
        print("\nInvalid operator. Please try again.")
        Calculator()

def Calculator():
    a = int(input('\nEnter 1st number: '))
    b = int(input('Enter 2nd number: '))
    c = str(input('Enter the operator: '))
    operation(a,b,c)

Calculator()
i = str(input("\nWant to continue? (y/n) \n"))
while i=="y":
    Calculator()
    i = str(input("\nWant to continue? (y/n) \n"))
