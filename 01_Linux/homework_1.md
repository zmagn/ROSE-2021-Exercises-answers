https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/01_Linux/homework_1.md
1.cd
Output:/home/student

2.pwd
Output:/home/student

3.mkdir hw1
Output:hw1 shows up on "ls" command.

4.cd hw1
mkdir docs web other
Output:docs web other - folders show up by using "ls" command.

5.cd web
Output:/home/student/hw1/web

6.touch website.txt
Output:website.txt - shows up by using "ls" command.

7.vim website.txt
(Press I - Insert Mode)
"My favorite song name"
(Press ESC - Exit Insert Mode)
:wq

8.cat website.txt
Output:My favorite song name - shows up by using "cat" command.

9.cd
Output:/home/student - shows up

10.tree
Output:·hw1🠗
		·other
		·web🠗
			·website.txt
		·docs

11.rmdir /home/student/hw1/docs/

12.tree
Output:·hw1🠗
		·other
		·web🠗
			·website.txt

13.cd hw1/web/
Output:/home/student/hw1/web

14.ls
Output:website.txt

15.rm website.txt

16.ls
Output:Nothing shows up since there are no files or folders.

17.cd ..
Output:/home/student/hw1
