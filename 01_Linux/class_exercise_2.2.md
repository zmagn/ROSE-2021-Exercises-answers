https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/01_Linux/class_exercise_2.2.md

Replace all "Roses" with "watermelons"

Save and exit the file

If you still have some time left, type man vim and find more useful shortcuts:
$ man vim

/home/student/

vim roses.txt
Output:
Ziv Magnezi
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
Yabadaba doo
Violets are blue

/Roses - To search for "Roses"

typed "watermelons" instead of Roses on both lines.

Output:
Ziv Magnezi
Violets are blue,
Sugar is sweet,
And so are you.

watermelons are red,
Violets are blue,
White wine costs less,
Than dinner for two.

watermelons are red,
But violets aren’t blue,
They’re purple, you dope,
Now go get a clue.
Yabadaba doo
Violets are blue

OR

/Roses - To search for "Roses"

then type "cgn"

The mark is on Roses now I type "watermelons" to replace the word.
After that I press ESC and then Press "N" to get to the next "Rose" word I want to replace.
The mark is on Roses now I type "watermelons" to replace the word.
I press ESC and then :wq to save the file as well ☺

Also answers by Ella:
%s/roses/watermelons/g
OR
sed 's/roses/watermelons/g' -i myfile
