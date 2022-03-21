https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/06_Functions/class_exercise_2.md

number = int(input('Enter a number '))
number2 = int(input('Enter a number '))
def is_divided(number):
    if number % number2 == 0:
        return True
    else:
        return False
result = number % number2 #Just to check if it actually returns 0 or 1
print(result)
print(is_divided(number))
