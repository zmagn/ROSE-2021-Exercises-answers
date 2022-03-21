https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/07_Exceptions/class_exercise_1.md

try:
    y = int(input('Enter a number '))
    #y = input('Enter a number okay? ')
    #y = int(y)
    x = y/0
    print('Horray you divided by ZERO!')
except ZeroDivisionError:
    print('Nope, can\'t divide by zero')
