https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/03_Variables_and_datatypes/homework_strings.md

Answers for lesson #4:
•Created directory "Homework3" by using mkdir Homework3.
•Changed to "Homework3" directory by using cd Homework3.

♦names.py

1.Create a string variable with your name, call it my_name
2.Create a string variable with your family name, call it my_family_name
3.Create a string variable called my_full_name which is composed from the 2 variables my_name and my_family_name.
4.Create a variable with your city name: call it my_city_name
5.Create a variable my_message with "My name is X and I’m from Y" using the variables you created above

vim names.py

Answer:
1.my_name = "Ziv "
2.my_family_name = "Magnezi"
3.my_full_name = my_name + my_family_name
4.my_city_name = "Netanya"
5.my_message = "My name is " + my_name + "and I'm from " + my_city_name
Output:
My name is Ziv and I'm from Netanya

♦times.py

Receive from the user the values for X and T and prints a nice line like:
"You have to spend X*T minutes this week to complete ROSE homework"
X - The number of questions
T - Time to complete each question

vim times.py

Answer:
X = input('The number of questions ')
T = input('Time to complete each question ')
MNTS = int(X) * int(T)
print(f'You have to spend {MNTS} minutes this week to complete ROSE homework')

♦letter.py

Write a python code that accepts date, name, address1, and address2 (as we learned in the last lesson)
The code should print the following output:

    <date>                 
            For
            <name>
            <address1>

    Dear Mr./Mrs. <name>
    Please visit our office as soon as possible to arrange your payments.
    We can't wait until it’s all done ...

    Sincerely
           Koogle Inc.
           <address2>

vim letter.py

Answer:
date = input('Enter date here ')
name = input('Enter your name here ')
address1 = input('Enter recipient address ')
address2 = input('Enter sender address ')
theletter = "\t" + date + "\n\t\t" + "For" + "\n\t\t" + name + "\n\t\t" + address1 + "\n\n\t" + "Dear Mr./Mrs." + name + "\n\t" + "Please visit our office as soon as possible to arrange your payments." + "\n\t" + "We can't wait until it’s all done ..." + "\n\n\t" + "Sincerely" + "\n\t\t" + "Koogle Inc." + "\n\t\t" + address2
print(theletter)
Output:
Enter date here 19/12/2021
Enter your name here Ziv
Enter recipient address Jerusalem
Enter sender address Netanya
	19/12/2021
		For
		Ziv
		Jerusalem

	Dear Mr./Mrs.Ziv
	Please visit our office as soon as possible to arrange your payments.
	We can't wait until it’s all done ...

	Sincerely
		Koogle Inc.
		Netanya



♦manipulations.py

Declare the following variable :

s = 'work hard dream big'
Perform the following functions:

1.Use the “title()” function on the string variable and print it.
2.Print the length of the string by len() function.
3.Use the “replace(... , ...)” function and replace the first word with the last word.
4.Use the “find()” function to know where is the ‘w’ word in the string.

manipulations.py
s = 'work hard dream big'

Answer:
1.s.title()
Output:'Work Hard Dream Big'
2.len(s)
Output:19
3.s.replace('work','big')
Output:
'big hard dream big'
4.s.find('w')
Output:
0 (That's incase the sentence is "work hard dream big" and not "big hard dream big" otherwise we would get -1)
