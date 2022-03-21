https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/05_Control_structures/extra.md

#median.py

x = [12, 32, 55]
z = 0
h = 0
if len(x)%2 == 0:
    z = int(len(x) / 2)
    h = int((x[z] + x[z - 1])/2)
    print(h)
else:
    z = int(len(x) / 2)
    print(x[z])

Output:
32

-------------------------------------------------------------------------------------------------------------------------------

#multiplication_table.py

temp = int(input('Enter a number: '))
z = 0
y = 0
for x in range(0,13,1):
    print(temp *x)

Output:

Enter a number: 5
0
5
10
15
20
25
30
35
40
45
50
55
60

-------------------------------------------------------------------------------------------------------------------------------

#fibonacci.py

def func(r):
    list = [0, 1]
    t = 0
    if r == 0:
        print('Cant run zero times - minimum is 1')
    else:
        for x in range(0,r,1):
            t = list[len(list) -1] + list[len(list) -2]
            list.append(t)
            print(list)
func(int(input('Enter a number here: ')))


Output:

Enter a number here: 10
[0, 1, 1]
[0, 1, 1, 2]
[0, 1, 1, 2, 3]
[0, 1, 1, 2, 3, 5]
[0, 1, 1, 2, 3, 5, 8]
[0, 1, 1, 2, 3, 5, 8, 13]
[0, 1, 1, 2, 3, 5, 8, 13, 21]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

-------------------------------------------------------------------------------------------------------------------------------

#pattern_a.py

t = int(input('Enter a number: '))
z = ''
for x in range(1, t+1, 1):
    z = z + str(x) + ' '
    print(z)

Output:

Enter a number: 3
1 
1 2 
1 2 3 

-------------------------------------------------------------------------------------------------------------------------------

#pattern_b.py

t = int(input('Enter a number: '))
z = ''
for x in range(t-1, 0, -1):
    z = z + str(x) + ' '
    print(z)


Output:

Enter a number: 5
4 
4 3 
4 3 2 
4 3 2 1 

-------------------------------------------------------------------------------------------------------------------------------

#pattern_c.py

t = int(input('Enter a number: '))
for x in range(1, t+1, 1):
    print('*' * x)
    if x == t:
        for y in range(t-1, -1, -1):
            print('*' * y)

Output:

Enter a number: 4
*
**
***
****
***
**
*

-------------------------------------------------------------------------------------------------------------------------------

#reverse.py

y = [10, 20, 30, 40, 50]
for x in range(len(y)-1, -1, -1):
    print(y[x])

Output:

50
40
30
20
10
