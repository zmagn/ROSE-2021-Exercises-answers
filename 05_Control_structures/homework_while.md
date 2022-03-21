https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/05_Control_structures/homework_while.md

#while_average.py

numbers = []
while True:
    number = int(input('Enter a number '))
    numbers.append(int(number))
    if number != 0:
        continue
    elif number == 0:
        break
total_num = int(sum(numbers))
total_lens = len(numbers)
last_num = total_lens - 1
del numbers[last_num]
total_avg = total_num/last_num
print(f'The numbers are: {numbers}')
print(f'The sum of all the numbers is: {total_num}')
print(f'The avg is: {total_avg}')

-------------------------------------------------------------------------------------------------------------------------------
#positive_negative.py

numbers = []
while True:
    number = int(input('Enter a number '))
    numbers.append(int(number))
    if number != 0:
        continue
    if number == 0:
        break
total_lens = len(numbers)
last_num = total_lens -1
del numbers[last_num]
numbersl = len(numbers)
print(f'The numbers are: {numbers}')
print(f'The count of the numbers are: {numbersl}')
