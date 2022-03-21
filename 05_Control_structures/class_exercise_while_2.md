https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/05_Control_structures/class_exercise_while_2.md

end = "done"
x = []
while True:
    number = input('Enter a number: ')
    if number != end:
        x.append(int(number))
        continue
    elif x == end:
        break
    print(max(x))
