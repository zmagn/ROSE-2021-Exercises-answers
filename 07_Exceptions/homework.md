https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/07_Exceptions/homework.md

#ex1_exceptions.py

try:
    a = int(input('Enter an intergener number to continue: '))
    targil = a * 1
    print('Your picked the number',a)
except ValueError:
    print('That was not an intergener number')


-------------------------------------------------------------------------------------------------------------------------------

#ex2_exceptions.py

a = 3
try:
    if a < 4:
        b = a/(a-3)
        print('Value of b is',b)
except ZeroDivisionError:
    print('Can\'t divide by zero')
except NameError:
    print('Something isn\'t right with some of the variables')

Output:
Can't divide by Zero

#if I change b variable to something else:
Something isn't right with some of the variables
