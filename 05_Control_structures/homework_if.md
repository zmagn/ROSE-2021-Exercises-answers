https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/05_Control_structures/homework_if.md

#even_or_odd.py

number = input('Please type a number: ')
number = int(number)
if (number%2) == 0:
    print(f'{number} is an even number')
else:
    print(f'{number} is an odd number')


-------------------------------------------------------------------------------------------------------------------------------
#greater_then.py

x = int(input('Number here: '))
if x > 1000:
    print(f'The number is greater than 1000')
else:
    print(f'The number is less than or equals to 1000')

-------------------------------------------------------------------------------------------------------------------------------
#buy_2_get_3.py

x = int(input('How many items have you purchased? '))

if x == 2:
    print(f'you get another item for free!')
if x == 1:
    print(f'add one more item so you can get another item for free!')

-------------------------------------------------------------------------------------------------------------------------------
#bill.py

x = int(input('What\'s the total you need to pay? '))
if x > 1000:
    y = x*0.9
    print(f'Great news you are getting 10% discount on your bill!\nYou need to pay {y} in total')
if x < 1000:
    y = x*0.95
    print(f'Great news you are getting 5% discount on your bill!\nYou need to pay {y} in total')
