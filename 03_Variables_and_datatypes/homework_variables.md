https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/03_Variables_and_datatypes/homework_variables.md

Answers for lesson #4:
•Created directory "lesson4" by using mkdir lesson4.
•Changed to "lesson4" directory by using cd lesson4.

♦variables_1.py

1.Declare a variable x with the value 9
2.Declare a variable y with the value 7
3.Declare a variable z with the sum of x and y variables.
4.Print out the contents of the z variable.
vim variables_1.py

Answer:
1.x = 9
2.y = 7
3.z = x+y
4.print(z)
Output:
16


♦variables_2.py
vim variables_2.py
•Accept two numbers from the user (using input) and:

1.Calculate multiplication (*) of the numbers
2.Calculate Subtract (-) of the numbers
3.Calculate Divide (/) of the numbers
4.Calculate Modulus (%) of the numbers

Answer:
•a = input('A number ')
 b = input('Another number ')
1.multi = int(a) * int(b)
 print(multi)
2.sub = int(a) - int(b)
 print(sub)
3.div = int(a) / int(b)
 print(div)
4.mod = int(a) % int(b)
 print(mod)

♦calculations.txt
vim calculations.txt

1.What is the result of 10 ** 3?
2.Given (x = 1), what will be its value of after we run (x += 2)?
3.What is the result of float(1)?
4.What is the result of 10 == “10”?
5.Print the result of the following variable:
  Number = ((((13 * 8 - 4) * 2 + 50) * 4 ) % 127 ) *5

Answer:
1.10**3
Output: 1000

2.x =1
  x +=2
Output: 3

3.float(1)
Output: 1.0

4.10 == "10"
Output: False

5.((((13 * 8 - 4) * 2 + 50) * 4 ) % 127 ) *5
Output: 555
