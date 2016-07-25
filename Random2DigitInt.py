import random
import datetime
from time import sleep

tryagain_valid = ['y', 'yes']
tryagain = 'yes'
x = random.randint(0,999)
while tryagain.lower() in tryagain_valid:
    x = random.randint(0,999)
    print(x, 'multiply this number by 11 before the computer does\n')
    start = datetime.datetime.now()
    y = int(input())
    end = datetime.datetime.now()
    after_five = start + datetime.timedelta(seconds=9)
    duration = end - start
    if y == (x * 11):
        if end < after_five:
            print('Success. You have beaten the computer in {time} seconds.'.format(time=duration.total_seconds()))
        else:
            print('The computer beat you. You took {time} seconds. better luck next time :)'.format(time=duration.total_seconds()))
    else:
        print('You got the wrong answer. The answer is {answer}. You took {time} seconds.'.format(answer=str(x * 11), time=duration.total_seconds()))
        
    print(x * 11)
    print('To continue type \'y\' or \'yes\'')
    tryagain = input()
