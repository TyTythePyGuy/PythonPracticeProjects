from art import logo
#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

def sqrt(n1, n2):
  return n1 ** n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
  "**": sqrt
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for operator in operations:
    print(operator)
  working = True

  while working == True:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == 'y':
      num1 = answer
    else:
      working = False
      calculator()

calculator()
