https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/04_Compound_data_types/homework_dictionary.md

# 1 - Countries

flights = {'Italy': 2, 'Spain': 3, 'Israel': 1}
flights['Belgium'] = 1
del flights['Italy']
print(f'how many times Udi was in Spain :', flights['Spain'])

Output:

how many times Udi was in Spain : 3

# 2 - Family members average age

familyavg = {'ages' : ' '}
familyavg['Samira'] = 8
familyavg['Moshe'] = 13
familyavg['Asher'] = 16
familyavg['Ronit'] = 23
familyavg['Haim'] = 40
familyavg['Dina'] = 39
familyavg['ages'] = (familyavg['Samira'] + familyavg['Moshe'] + familyavg['Asher'] + familyavg['Ronit'] + familyavg['Haim'] + familyavg['Dina'])/6
print(familyavg)
print(f'The average ages:', float(familyavg['ages']))

Output:

{'ages': 23.166666666666668, 'Samira': 8, 'Moshe': 13, 'Asher': 16, 'Ronit': 23, 'Haim': 40, 'Dina': 39}
The average ages: 23.166666666666668
