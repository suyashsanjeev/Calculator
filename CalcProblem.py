print('What is your expression?')
x = input()
operation = ''
num1 = 0
num2 = 0
for i in range(len(x)):
    if(x[i] == '+' or x[i] == '-' or x[i] == '*' or x[i] == '/'):
        operation = x[i]
        num1 = int(x[0:i])
        num2 = int(x[i+1:])
    if operation == '+':
        y = num1 + num2
    if operation == '-':
        y = num1 - num2
    if operation == '*':
        y = num1 * num2
    if operation == '/':
        y = num1/num2
print(y)
