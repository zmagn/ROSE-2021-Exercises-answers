https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/08_Modules_and_packages/class_exercise_1.md

import math
def sinus(x):
    print(x)

try:
    sinus(math.sin(int(input('Enter an intenger number '))))
except ValueError:
    print(f'Integer numbers only')

-------------------------------------------------------------------------------------------------------------------------------

import math
def powa(a,b):
    x = math.pow(a,b)
    print(x)
try:
    a = int(input('Enter a number '))
    b = int(input('Enter another number '))
    powa(a,b)
except ValueError:
    print(f'Integer numbers only')

-------------------------------------------------------------------------------------------------------------------------------

import math
def root(x):
    print(x)
try:
    root(math.sqrt(float(input('Enter a a number '))))
except ValueError:
    print(f'Numbers only')

-------------------------------------------------------------------------------------------------------------------------------

import math
def log(x):
    print(x)
try:
    log(math.log10(int(input('Enter a number '))))
except ValueError:
    print(f'Integer numbers only')
