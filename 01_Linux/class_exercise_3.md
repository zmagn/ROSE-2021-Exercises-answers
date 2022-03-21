https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/01_Linux/class_exercise_3.md

1.Open a terminal
2.Create a Directory linux3 in your home directory
3.Change Directory to linux3
4.Copy the file /home/student/ROSE/docs/course_materials/exercises/01_Linux/roses.txt to linux3 directory
5.Create a directory songs in linux3 directory
6.Copy the file roses.txt to the directory ~/linux3/songs
7.Change the name of the file ~/linux3/songs/roses.txt to ~/linux3/songs/red.txt
8.Print the content of the file ~/linux3/songs/red.txt

1.Click on Terminal

/home/student/

2.mkdir linux3
Output:linux3 - folder show up by using "ls" command.

3.cd linux3/
Output:/home/student/linux3/

4.cp /home/student/ROSE/docs/course_materials/exercises/01_Linux/roses.txt roses.txt
Output:roses.txt shows on "ls" command.

5.mkdir songs
Output:songs - folder show up by using "ls" command.

6.cp roses.txt songs
Output:
[student@zivm linux3]$ tree songs
songs
└── roses.txt

7.mv songs/roses.txt songs/red.txt
Output:
[student@zivm linux3]$ tree songs
songs
└── red.txt

8.cat songs/red.txt 
Output:
Roses are red,
Violets are blue,
Sugar is sweet,
And so are you.

Roses are red,
Violets are blue,
White wine costs less,
Than dinner for two.

Roses are red,
But violets aren’t blue,
They’re purple, you dope,
Now go get a clue.
