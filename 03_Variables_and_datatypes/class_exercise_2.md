https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/03_Variables_and_datatypes/class_exercise_2.md

Create a new file my_full_name.py using vim editor
Get the user's first name and save it in a new variable first_name
Get the user's last name and save it in a new variable last_name
Print first_name and last_name using f'.{}.' formatting
Save the file and run it on the terminal

vim my_full_name.py
(Press I Insert Mode)
first_name = input('Your first name')
last_name = input('Your last name')
print(f'Hello {first_name} {last_name}!')

Output:
[student@zivm ~]$ python3 my_full_name.py 
Your first name Ziv
Your last name Magnezi
Hello  Ziv  Magnezi!
