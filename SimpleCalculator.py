


while True:
    try:
        num1 = float(input("Enter a number: "))

    except ValueError:
        print('Input should be an integer')
        continue
    break




op = input("Enter an operator: ")
str(op)

while op not in ('+', '-', '*', '/'):
    op = input("Please enter a correct operator\n")


num2 = float(input("Enter another number: "))




if op == "+":
    result = num1+num2

elif op == "-":
        result = num1-num2

elif op == "*":
    result = num1*num2

elif op == "/":
    if num2 == 0:
        result = 'Undefined'
    else:
        result = num1/num2

print(result)



