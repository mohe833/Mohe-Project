# Mini Calculator by Mohammed Keyru
# This program can add, subtract, multiply, and divide two numbers.
def add(a, b):
   return a + b
def subtract(a, b):
   return a - b
def multiply(a, b):
   return a * b
def divide(a, b):
   if b != 0:
       return a / b
   else:
       return "No number can't be divided by zero"
print("Welcome to Mohe's Calculator!")
print("Choose an operation: +  -  *  /")
# Ask the user for input
operation = input("Enter operation: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Calculate result
if operation == "+":
   result = add(num1, num2)
elif operation == "-":
   result = subtract(num1, num2)
elif operation == "*":
   result = multiply(num1, num2)
elif operation == "/":
   result = divide(num1, num2)
else:
   result = "Invalid operation!"
print("Result:", result)
print("Thanks for using my calculator!")