import sys
print('What is your number?')
x = input()
a = 2
b = 1
c = 0
d = len(x)
for i in range(10):
    r = ''
    
    if d == 1:
        a -= 2
    if d == 2:
        a -= 1
        b -= 1
        
    if x[a] == '2':
        r = 'two'
    elif x[a] == '3':
        r = 'three'
    elif x[a] == '4':
        r = 'four'
    elif x[a] == '5':
        r = 'five'
    elif x[a] == '6':
        r = 'six'
    elif x[a] == '7':
        r = 'seven'
    elif x[a] == '8':
        r = 'eight'
    elif x[a] == '9':
        r = 'nine'        
    
    if d == 1:
        print(r)
        break
    else:
        pass
    
    fancy = False
    if x[b] == '2':
        t = 'twenty'
    elif x[b] == '3':
        t = 'thirty'
    elif x[b] == '4':
        t = 'forty'
    elif x[b] == '5':
        t = 'fifty'
    elif x[b] == '6':
        t = 'sixty'
    elif x[b] == '7':
        t = 'seventy'
    elif x[b] == '8':
        t = 'eighty'
    elif x[b] == '9':
        t = 'ninety'
    elif x[b:] == '10':
        t = 'ten'
        fancy = True
    elif x[b:] == '11':
        t = 'eleven'
        fancy = True
    elif x[b:] == '12':
        t = 'twelve'
        fancy = True
    elif x[b:] == '13':
        t = 'thirteen'
        fancy = True
    elif x[b:] == '14':
        t = 'fourteen'
        fancy = True
    elif x[b:] == '15':
        t = 'fifteen'
        fancy = True
    elif x[b:] == '16':
        t = 'sixteen'
        fancy = True
    elif x[b:] == '17':
        t = 'seventeen'
        fancy = True
    elif x[b:] == '18':
        t = 'eighteen'
        fancy = True
    elif x[b:] == '19':
        t = 'nineteen'
        fancy = True
    else:
        t = 'Not a valid number'
    
    if d == 2:
        print(t)
        print(r)
        break
    else:
        pass
    
    if x[c] == '1':
        y = 'one hundred'
    elif x[c] == '2':
        y = 'two hundred'
    elif x[c] == '3':
        y = 'three hundred'
    elif x[c] == '4':
        y = 'four hundred'
    elif x[c] == '5':
        y = 'five hundred'
    elif x[c] == '6':
        y = 'six hundred'
    elif x[c] == '7':
        y = 'seven hundred'
    elif x[c] == '8':
        y = 'eight hundred'
    elif x[c] == '9':
        y = 'nine hundred'
    else:
        y = 'Not a valid number'
    print(y)
    print(t)
    if fancy == False:
        print(r)
    break
