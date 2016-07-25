x = '  '
for i in range(1, 4):    
    if i == 2:
        x = ' '
    if i == 3:        
        x = ''    
    print(x, '*'* (2*i - 1))
for n in range(2, 0, -1):      
    if n == 2:
        x = ' '  
    if n == 1:
        x = '  '   
    print(x, '*'* (2*n - 1))
