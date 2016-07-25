from math import factorial
from math import sqrt
from math import pi
import sys
tryagain_valid = ['yes', 'ok', 'sure', 'y', 'okay', 'yeah', 'yea', 'ya', 'yah', 'mhm','mmhm', 'k', 'kk', 'yea man', 'go']
tryagain = 'yes'
print('Enter Username')
x = input()
if x == 'Suyash' or x == 'SUyash' or x == 'SUaysh' or x == 'Suvansh':
    pass
else:
    print('Enter Password')
    y = input()
    if y != 'netflixrocks123':
        print('Password Incorrect.')
        sys.exit()
    else:
        print('You have successfully entered this computer.')
        pass
print('Would you like to access calculator or other. Enter \"C\" for calculator and \"EC\" for an expression calculator')
z = input()

if z == 'EC':
    def isPrimeNumber(num1):
        isPrime = True
        if num1<2:
            print(num1, 'is not prime nor composite.')
        elif num1 == 2:
            isPrime = True  
        else:
            for a in range(2, num1):
                if num1%a == 0:
                    isPrime = False                
                    break
                else:
                    continue
        return isPrime;

    def is_int(num):
        try:
            x = int(num)
            return True
        except ValueError:
            return False

    print('This is an expression calculator')
    
    tryagain_valid = ['yes', 'ok', 'sure', 'y', 'okay', 'yeah', 'yea', 'ya', 'yah', 'mhm','mmhm', 'k', 'kk', 'yea man', 'go']
    tryagain = 'yes'    
    print('Welcome to Suyash\'s Expression Calculator.')
    while True:
        invalid_input = False
        print('+ is add\n'
            + '- is subtract\n'
            + '* is multiply\n'
            + '/ is divide\n'
            + '// is divide and knock off everything after the decimal\n'
            + '% is remainder\n'
            + '! is factorial\n'
            + '%% is percent of something\n'
            + '^ is to the power of\n'
            + 'sqrt is square root\n'
            + 'hyp is finding the hypotenuse if x and y are legs of a right triangle\n'
            + '#% is division in the form of something remainder something\n'
            + 'OA is area of a circle\n'
            + 'OC is circumference of a circle\n'
            + 'OD is diameter of a circle\n'
            + 'ave is the average of x and y\n'
            + 'pri checks if a number is prime or not\n')           
        print('What is your expression?')
        x = input()
        splits = x.split()
        if len(splits) == 3:
            num1 = int(splits[0])
            num2 = int(splits[2])
            operation = splits[1]
        elif len(splits) == 2:
            if is_int(splits[0]):
                num1 = int(splits[0])
                operation = splits[1]
            elif is_int(splits[1]):
                num1 = int(splits[1])
                operation = splits[0]
            else:
                print("Invalid syntax: must enter a number")
        elif splits[0] == "quit":
            break
        else:
            print("Invalid syntax: must enter expression in format \"<number> <operand> <number>\", \"<number> <operand>\", or \"<operand> <number>\"")
        if operation == '+':
            y = num1 + num2
        elif operation == '-':
            y = num1 - num2
        elif operation == '*':
            y = num1 * num2
        elif operation == '/':
            y = num1/num2
        elif operation == '//':
            y = num1//num2
        elif operation == '%':
            y = num1%num2
        elif operation == '%%':
            y = (num1/100)*num2
        elif operation == 'hyp':
            y = sqrt(num1**2 + num2**2)
        elif operation == '()%':
            y = num1//num2, 'R', num1%num2
        elif operation == 'ave':
            y = (num1+num2)/2
        elif operation == '^':
            y = num1**num2
        elif operation == 'sqrt':
            y = sqrt(num1)    
        elif operation == 'pri':
            y = ''
            if isPrimeNumber(num1):
                print(num1, 'is prime.')
            else:
                print(num1, 'is not prime.')
        elif operation == 'OA':
            y = (num1**2)* pi
        elif operation == 'OC':
            y = (2*num1)* pi
        elif operation == 'OD':
            y = num1*2
        else:
            invalid_input = True
            print('Invalid syntax: operation invalid')
        if not invalid_input:
            print(y, '\n')

elif z == 'C':
    def isPrimeNumber(x):
        isPrime = True
        if x<2:
            print(x, 'is not prime nor composite.')
        elif x == 2:
            isPrime = True  
        else:
            for a in range(2, x):
                if x%a == 0:
                    isPrime = False                
                    break
                else:
                    continue
            return isPrime;
        
    def isBinaryOperation(w):
        if (w == '+') or (w == '-') or (w == '*') or (w == '/') or (w == '//') or (w == '%') or (w == '%%') or (w == 'hyp') or (w == '#%') or (w == 'ave') or (w == '^') or (w == 'g3') or (w == 's3') or (w == 'm3'):
            return 2
        elif (w == 'sqrt') or (w == 'pri'):
            return 1
        elif (w == 'OA') or (w == 'OC') or (w == 'OD') or (w == 'expr'):
            return 0

    print('This is a calculator')
    print('Welcome to Suyash\'s Calculator.')
    while tryagain.lower() in tryagain_valid:
        print('+ is add\n'
            + '- is subtract\n'
            + '* is multiply\n'
            + '/ is divide\n'
            + '// is divide and knock off everything after the decimal\n'
            + '% is remainder\n'
            + '! is factorial\n'
            + '%% is percent of something\n'
            + '^ is to the power of\n'
            + 'sqrt is square root\n'
            + 'hyp is finding the hypotenuse if x and y are legs of a right triangle\n'
            + '#% is division in the form of something remainder something\n'
            + 'OA is area of a circle\n'
            + 'OC is circumference of a circle\n'
            + 'OD is diameter of a circle\n'
            + 'g3 is finding the greatest of three numbers\n'
            + 'm3 is finding the middle of three numbers\n'
            + 's3 is finding the smallest of three numbers\n'
            + 'ave is the average of x and y\n'
            + 'pri checks if a number is prime or not\n'
            + 'expr lets you input an expression and solves that expression. CAUTION use spaces between numbers and operators in the expression.\n')
        print('What\'s your operation?')
        w = input()
        if isBinaryOperation(w) == 2:        
            print('What\'s your 1st number?')
            x = int(input())
            print('What\'s your 2nd number?')
            y = int(input())
        elif isBinaryOperation(w) == 1:
            print('What\'s your number?')
            x = int(input())
        elif isBinaryOperation(w) == 0:
            pass            
        if w == '+':
            print(x+y)
        elif w == '*':
            print(x*y)
        elif w == '-':
            print(x-y)
        elif w == '/':
            print(x+y)
        elif w == '//':
            print(x//y)
        elif w == '%':
            print(x%y)
        elif w == '!':
            print(factorial(x))
        elif w == '%%':
            print((x/100)* y)
        elif w == '^':
            print(x**y)
        elif w == 'sqrt':
            print(sqrt(x))
        elif w == 'hyp':
            print(sqrt((x**2) + (y**2)))
        elif w == '#%':
            print(x//y, 'R', x%y)
        elif w == 'OA':
            print('What\'s the radius of your circle?')
            u = int(input())
            print((u**2)*pi)
        elif w == 'OC':
            print('What\'s the radius of your circle?')
            u = int(input())
            print(2*u*pi)
        elif w == 'OD':
            print('What\'s the radius of your circle?')
            u = int(input())
            print(2*u)
        elif w == 'g3':
            print('what\'s your third number')
            t = int(input())
            print('the largest number is', max([x, y, t]))
        elif w == 's3':
            print('what\'s your third number')
            t = int(input())
            print('the smallest number is', min([x, y, t]))
        elif w == 'm3':
            print('what\'s your third number')
            t = int(input())
            if x>y and x<t or x<y and x>t:
                print('the middle number is', x)
            elif y>x and y<t or y<x and y>t:
                print('the middle number is', y)
            else:
                print('the middle number is', t)
        elif w == 'ave':
                print((x+y)/2)
        elif w == 'pri':
            if isPrimeNumber(x):
                print(x, 'is prime.')
            else:
                print(x, 'is not prime.')
        elif w == 'expr':
            print('What is your expression?')
            x = input()
            splits = x.split()
            num1 = int(splits[0])
            num2 = int(splits[2])
            operation = splits[1]
            if operation == '+':
                y = num1 + num2
            elif operation == '-':
                y = num1 - num2
            elif operation == '*':
                y = num1 * num2
            elif operation == '/':
                y = num1/num2
            elif operation == '//':
                y = num1//num2
            elif operation == '%':
                y = num1%num2
            elif operation == '%%':
                y = (num1/100)*num2
            elif operation == 'hyp':
                y = sqrt(num1**2 + num2**2)
            elif operation == '()%':
                y = num1//num2, 'R', num1%num2
            elif operation == 'ave':
                y = (num1+num2)/2
            elif operation == '^':
                y = num1**num2
            elif operation == 'g3':
                print('what\'s your third number')
                t = int(input())
                y = 'the largest number is', max([num1, num2, t])
            elif operation == 's3':
                print('what\'s your third number')
                t = int(input())
                y = 'the smallest number is', min([num1, num2, t])                
            elif operation == 'm3':
                print('what\'s your third number')
                t = int(input())
                if ((num1>num2) and (num1<t)) or ((num1<num2) and (num1>t)):
                    y = 'the middle number is ' + num1
                elif (num2>num1 and num2<t) or (num2<num1 and num2>t):
                    print('the middle number is', num2)
                else:
                    print('the middle number is', t)
            elif operation == 'sqrt':
                y = sqrt(num1)
            print(y)
        else:
            print('Syntax Error')
        if w == "quit":
            break

print('To continue type "yes". If you\'re a rebel, then feel free to type any other words that denote the same thing (a non-yes word might not work).')
tryagain = input()



