https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/01_Linux/class_exercise_4.md

pwd ---> /homes/student
mkdir linux4
cd linux4
cp /home/student/ROSE/docs/course_material/exercises/01_Linux/roses.txt /home/student/linux4
touch roses1.txt roses2.txt roses3.txt
head -n 5 roses.txt
tail -n 4 roses.txt
rm roses.txt
cd ..
rm -r linux4
