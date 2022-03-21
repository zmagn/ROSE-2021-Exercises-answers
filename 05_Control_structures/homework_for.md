https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/05_Control_structures/homework_for.md

#ten.py

for x in range(1,11):
    print('This is x:', x)

Output:

This is x: 1
This is x: 2
This is x: 3
This is x: 4
This is x: 5
This is x: 6
This is x: 7
This is x: 8
This is x: 9
This is x: 10

-------------------------------------------------------------------------------------------------------------------------------

#natural.py

xl = []
for x in range(1,11):
    xl.append(x)
print(sum(xl))

Output: 55

-------------------------------------------------------------------------------------------------------------------------------

#divided_by_5.py

a = [1, 5, 6, 10, 12, 13, 15, 20, 21, 34, 55, 89, 110, 115 , 152 , 1028]
for x in a:
    if x%5 == 0:
        print(x)

Output:

5
10
15
20
55
110
115

