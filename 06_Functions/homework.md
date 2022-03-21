#good_work.py

#name = input('Enter your name here: ') /// Added the input below instead
def good_work(name, namesecond, namethird):
    print('You are doing good work', name)
    print('Thank you very much', namesecond, 'for your efforts on this project.')
    print('We are looking forward', namethird, 'to see more projects in the future')
good_work(input('Enter a name: '), 'Joe', 'Gordon')

Output:

Enter a name: John
You are doing good work John
Thank you very much Joe for your efforts on this project.
We are looking forward Gordon to see more projects in the future

-------------------------------------------------------------------------------------------------------------------------------

#max.py

def twonums(n1, n2):
    numh = [int(n1), int(n2)]
    print('The list', numh) #It's just to have two different ways to get the max num ☺
    highest = max(numh)
    print(f'Your Max', (highest))
    if n1 < n2:
        print('The max is', n2)
    else:
        print('The max is' , n1)
twonums(int(input('Enter a number: ')), int(input('Enter another number: ')))


Output:

Enter a number: 10
Enter another number: 4
The list [10, 4]
Your Max 10
The max is 10

-------------------------------------------------------------------------------------------------------------------------------

#Multable.py

def multi(a):
    b = 0
    for x in range(0,13,1):
        print(a * x)
multi(int(input('Enter a number: ')))

Output:

Enter a number: 3
0
3
6
9
12
15
18
21
24
27
30
33
36

