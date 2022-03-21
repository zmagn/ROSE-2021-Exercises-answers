https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/04_Compound_data_types/class_exercise_3.md

my_dict = {'name': ' ', 'homework': ' ', 'quizzes': ' ', 'tests': ' '}
my_dict['name'] = 'Itzik'
my_dict['homework'] = '90.0,97.0,75.0,92.0'
my_dict['quizzes'] = '88.0,40.0,94.0'
my_dict['tests'] = '75.0,90.0'
my_dict['tests'] = '95.0'
print(my_dict)
print(my_dict['name'])
print(my_dict['homework'])
print(my_dict['quizzes'])
print(my_dict['tests'])

Output:

{'name': 'Itzik', 'homework': '90.0,97.0,75.0,92.0', 'quizzes': '88.0,40.0,94.0', 'tests': '95.0'}

Itzik
90.0,97.0,75.0,92.0
88.0,40.0,94.0
95.0
