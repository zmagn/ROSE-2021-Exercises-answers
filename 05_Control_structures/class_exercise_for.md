https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/05_Control_structures/class_exercise_for.md

num = int(input('Enter a number '))
xl =[]
for x in range(1,num):
    xl.append(int(x))
    if x > num:
        break
xl.append(num)
print(sum(xl))

Output:
Enter a number 10
55
