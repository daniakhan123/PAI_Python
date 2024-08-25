num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
opr = input("Enter an operator  :")


if opr == '+':
    print('Addition of num1 and num2 is: ', -(-num1 - num2))
elif opr == '-':
    print('Subtraction of num1 and num2 is: ' , num1 - num2)
elif opr == '*':
    print('Multiplication of num1 and num2 is: ', num1 * num2)
elif opr == '/':
    if num2 != 0:
        print('Division of num1 and num2 is: ',num1 / num2)
    else:
        print('Division by zero is not Possible')
else:
    print('Invalid operator')
