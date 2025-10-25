print("Welcome to My Python Calculator!")
operations = ['+', '-', '*', '/']

first_number = float(input("What is the first number?: "))
for operation in operations:
  print(operation)

operation = input("Pick and operation: ")

second_number = float(input("What is the next number?: "))

if operation == '+':
  answer = first_number + second_number
elif operation == '-':
  answer = first_number - second_number
elif operation == '*':
  answer = first_number * second_number
elif operation == '/':
  answer = first_number / second_number

print(f"{first_number} {operation} {second_number} = {answer}")
