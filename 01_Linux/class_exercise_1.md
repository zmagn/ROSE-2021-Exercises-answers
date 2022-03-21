https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/01_Linux/class_exercise_1.md

1.Open a terminal
2.Navigate to your home directory
3.Create a directory called test
4.Navigate to test directory
5.Create a directory called tmp in test directory
6.Navigate to tmp directory
7.Navigate two directories up
8.List the content of this directory in a tree format
9.Navigate to your root directory
10.Navigate to test/tmp directory in your home directory

1.Click on Terminal

/home/student/

2.cd OR cd /home/student/
Output:/home/student/ shows on "pwd" command.

3.mkdir test
Output: test - folder shows on "ls" command.

4.cd test/
Output:/home/student/test/

5.mkdir tmp
Output: tmp - folder shows on "ls" command.

6.cd tmp/
Output:/home/student/test/tmp/

7.cd ../..
Output:/home/student/

8.tree
Output:
[student@zivm ~]$ tree
.
├── Desktop
├── Documents
├── Downloads
├── hello.py
├── hw1
│   ├── other
│   └── web
│       └── website.txt
├── hw2
│   ├── drafts
│   │   └── new_song.txt
│   ├── movies
│   └── songs
│       └── your_song.txt
├── linux3
│   ├── roses.txt
│   └── songs
│       └── red.txt
├── Music
├── Pictures
├── Public
├── ROSE
│   ├── AUTHORS
│   ├── classroom
│   │   ├── connect_service.py
│   │   ├── content_edit.py
│   │   ├── course_creator.py
│   │   ├── README.md
│   │   └── rose_class.py
│   ├── Dockerfile
│   ├── docs
│   │   ├── code-of-conduct.md
│   │   ├── compound_data_types.md
│   │   ├── _config.yml
│   │   ├── control_structures.md
│   │   ├── course_materials
│   │   │   ├── compound_data_types.html
│   │   │   ├── control_structures.html
│   │   │   ├── exceptions.html
│   │   │   ├── exercises
│   │   │   │   ├── 00_Intro
│   │   │   │   │   ├── class_exe.md
│   │   │   │   │   └── homework.md
│   │   │   │   ├── 01_Linux
│   │   │   │   │   ├── class_exercise_1.md
│   │   │   │   │   ├── class_exercise_2.1.md
│   │   │   │   │   ├── class_exercise_2.2.md
│   │   │   │   │   ├── class_exercise_3.md
│   │   │   │   │   ├── class_exercise_4.md
│   │   │   │   │   ├── homework_1.md
│   │   │   │   │   ├── homework_2.md
│   │   │   │   │   └── roses.txt
│   │   │   │   ├── 02_Python_intro
│   │   │   │   │   ├── class_exercise_1.md
│   │   │   │   │   └── homework.md
│   │   │   │   ├── 03_Variables_and_datatypes
│   │   │   │   │   ├── class_exercise_1.md
│   │   │   │   │   ├── class_exercise_2.md
│   │   │   │   │   ├── homework_strings.md
│   │   │   │   │   └── homework_variables.md
│   │   │   │   ├── 04_Compound_data_types
│   │   │   │   │   ├── class_exercise_1.md
│   │   │   │   │   ├── class_exercise_2.md
│   │   │   │   │   ├── class_exercise_3.md
│   │   │   │   │   ├── homework_dictionary.md
│   │   │   │   │   └── homework_list.md
│   │   │   │   ├── 05_Control_structures
│   │   │   │   │   ├── class_exercise_for.md
│   │   │   │   │   ├── class_exercise_if.md
│   │   │   │   │   ├── class_exercise_while_1.md
│   │   │   │   │   ├── class_exercise_while_2.md
│   │   │   │   │   ├── extra.md
│   │   │   │   │   ├── homework_for.md
│   │   │   │   │   ├── homework_if.md
│   │   │   │   │   └── homework_while.md
│   │   │   │   ├── 06_Functions
│   │   │   │   │   ├── class_exercise_1.md
│   │   │   │   │   ├── class_exercise_2.md
│   │   │   │   │   ├── class_exercise_3.md
│   │   │   │   │   └── homework.md
│   │   │   │   ├── 07_Exceptions
│   │   │   │   │   ├── class_exercise_1.md
│   │   │   │   │   └── homework.md
│   │   │   │   ├── 08_Modules_and_packages
│   │   │   │   │   ├── class_exercise_1.md
│   │   │   │   │   └── homework.md
│   │   │   │   ├── 09_Extra
│   │   │   │   │   ├── class_exercise_1.md
│   │   │   │   │   ├── class_exercise_1_solution.py
│   │   │   │   │   ├── class_exercise_2.md
│   │   │   │   │   ├── class_exercise_2_solution.py
│   │   │   │   │   └── homework.md
│   │   │   │   └── test_exercises
│   │   │   │       ├── 01_Linux
│   │   │   │       │   ├── check_class_exercise_1.py
│   │   │   │       │   ├── check_class_exercise_2.1.py
│   │   │   │       │   ├── check_class_exercise_2.2.py
│   │   │   │       │   ├── check_class_exercise_3.py
│   │   │   │       │   ├── check_class_exercise_4.py
│   │   │   │       │   ├── check_homework_1.py
│   │   │   │       │   └── check_homework_2.py
│   │   │   │       ├── 03_Variables_and_datatypes
│   │   │   │       │   ├── test_homework_strings.py
│   │   │   │       │   └── test_homework_variables.py
│   │   │   │       ├── 04_Compound_data_types
│   │   │   │       │   ├── test_homework_dictionaries.py
│   │   │   │       │   └── test_homework_lists.py
│   │   │   │       ├── color_print.py
│   │   │   │       ├── command_dictionary.py
│   │   │   │       ├── conftest.py
│   │   │   │       ├── how_to_add_linux_tests.md
│   │   │   │       ├── how_to_add_python_tests.md
│   │   │   │       ├── linux_tester.py
│   │   │   │       ├── pytest.ini
│   │   │   │       └── rose_check.py
│   │   │   ├── functions.html
│   │   │   ├── homeworks.md
│   │   │   ├── linux_intro.html
│   │   │   ├── media
│   │   │   │   ├── exr_background.jpeg
│   │   │   │   ├── functions.png
│   │   │   │   ├── presentations.css
│   │   │   │   ├── python-icon.png
│   │   │   │   ├── rose_background.jpg
│   │   │   │   ├── slicing.png
│   │   │   │   └── string-slicing.png
│   │   │   ├── modules_packages.html
│   │   │   ├── python_intro.html
│   │   │   ├── README.md
│   │   │   ├── reveal
│   │   │   │   ├── bower.json
│   │   │   │   ├── CONTRIBUTING.md
│   │   │   │   ├── css
│   │   │   │   │   ├── print
│   │   │   │   │   │   ├── paper.css
│   │   │   │   │   │   └── pdf.css
│   │   │   │   │   ├── reveal.css
│   │   │   │   │   ├── reveal.scss
│   │   │   │   │   └── theme
│   │   │   │   │       ├── beige.css
│   │   │   │   │       ├── black.css
│   │   │   │   │       ├── blood.css
│   │   │   │   │       ├── league.css
│   │   │   │   │       ├── moon.css
│   │   │   │   │       ├── night.css
│   │   │   │   │       ├── presentations.css
│   │   │   │   │       ├── README.md
│   │   │   │   │       ├── serif.css
│   │   │   │   │       ├── simple.css
│   │   │   │   │       ├── sky.css
│   │   │   │   │       ├── solarized.css
│   │   │   │   │       ├── source
│   │   │   │   │       │   ├── beige.scss
│   │   │   │   │       │   ├── black.scss
│   │   │   │   │       │   ├── blood.scss
│   │   │   │   │       │   ├── league.scss
│   │   │   │   │       │   ├── moon.scss
│   │   │   │   │       │   ├── night.scss
│   │   │   │   │       │   ├── serif.scss
│   │   │   │   │       │   ├── simple.scss
│   │   │   │   │       │   ├── sky.scss
│   │   │   │   │       │   ├── solarized.scss
│   │   │   │   │       │   └── white.scss
│   │   │   │   │       ├── template
│   │   │   │   │       │   ├── mixins.scss
│   │   │   │   │       │   ├── settings.scss
│   │   │   │   │       │   └── theme.scss
│   │   │   │   │       └── white.css
│   │   │   │   ├── demo.html
│   │   │   │   ├── Gruntfile.js
│   │   │   │   ├── index.html
│   │   │   │   ├── js
│   │   │   │   │   └── reveal.js
│   │   │   │   ├── lib
│   │   │   │   │   ├── css
│   │   │   │   │   │   └── zenburn.css
│   │   │   │   │   ├── font
│   │   │   │   │   │   ├── league-gothic
│   │   │   │   │   │   │   ├── league-gothic.css
│   │   │   │   │   │   │   ├── league-gothic.eot
│   │   │   │   │   │   │   ├── league-gothic.ttf
│   │   │   │   │   │   │   ├── league-gothic.woff
│   │   │   │   │   │   │   └── LICENSE
│   │   │   │   │   │   └── source-sans-pro
│   │   │   │   │   │       ├── LICENSE
│   │   │   │   │   │       ├── source-sans-pro.css
│   │   │   │   │   │       ├── source-sans-pro-italic.eot
│   │   │   │   │   │       ├── source-sans-pro-italic.ttf
│   │   │   │   │   │       ├── source-sans-pro-italic.woff
│   │   │   │   │   │       ├── source-sans-pro-regular.eot
│   │   │   │   │   │       ├── source-sans-pro-regular.ttf
│   │   │   │   │   │       ├── source-sans-pro-regular.woff
│   │   │   │   │   │       ├── source-sans-pro-semibold.eot
│   │   │   │   │   │       ├── source-sans-pro-semibolditalic.eot
│   │   │   │   │   │       ├── source-sans-pro-semibolditalic.ttf
│   │   │   │   │   │       ├── source-sans-pro-semibolditalic.woff
│   │   │   │   │   │       ├── source-sans-pro-semibold.ttf
│   │   │   │   │   │       └── source-sans-pro-semibold.woff
│   │   │   │   │   └── js
│   │   │   │   │       ├── classList.js
│   │   │   │   │       ├── head.min.js
│   │   │   │   │       └── html5shiv.js
│   │   │   │   ├── LICENSE
│   │   │   │   ├── package.json
│   │   │   │   ├── plugin
│   │   │   │   │   ├── highlight
│   │   │   │   │   │   └── highlight.js
│   │   │   │   │   ├── markdown
│   │   │   │   │   │   ├── example.html
│   │   │   │   │   │   ├── example.md
│   │   │   │   │   │   ├── markdown.js
│   │   │   │   │   │   └── marked.js
│   │   │   │   │   ├── math
│   │   │   │   │   │   └── math.js
│   │   │   │   │   ├── multiplex
│   │   │   │   │   │   ├── client.js
│   │   │   │   │   │   ├── index.js
│   │   │   │   │   │   ├── master.js
│   │   │   │   │   │   └── package.json
│   │   │   │   │   ├── notes
│   │   │   │   │   │   ├── notes.html
│   │   │   │   │   │   └── notes.js
│   │   │   │   │   ├── notes-server
│   │   │   │   │   │   ├── client.js
│   │   │   │   │   │   ├── index.js
│   │   │   │   │   │   └── notes.html
│   │   │   │   │   ├── print-pdf
│   │   │   │   │   │   └── print-pdf.js
│   │   │   │   │   ├── search
│   │   │   │   │   │   └── search.js
│   │   │   │   │   └── zoom-js
│   │   │   │   │       └── zoom.js
│   │   │   │   ├── README.md
│   │   │   │   └── test
│   │   │   │       ├── examples
│   │   │   │       │   ├── assets
│   │   │   │       │   │   ├── image1.png
│   │   │   │       │   │   └── image2.png
│   │   │   │       │   ├── barebones.html
│   │   │   │       │   ├── embedded-media.html
│   │   │   │       │   ├── math.html
│   │   │   │       │   ├── slide-backgrounds.html
│   │   │   │       │   └── slide-transitions.html
│   │   │   │       ├── qunit-1.12.0.css
│   │   │   │       ├── qunit-1.12.0.js
│   │   │   │       ├── simple.md
│   │   │   │       ├── test.html
│   │   │   │       ├── test.js
│   │   │   │       ├── test-markdown-element-attributes.html
│   │   │   │       ├── test-markdown-element-attributes.js
│   │   │   │       ├── test-markdown-external.html
│   │   │   │       ├── test-markdown-external.js
│   │   │   │       ├── test-markdown.html
│   │   │   │       ├── test-markdown.js
│   │   │   │       ├── test-markdown-options.html
│   │   │   │       ├── test-markdown-options.js
│   │   │   │       ├── test-markdown-slide-attributes.html
│   │   │   │       ├── test-markdown-slide-attributes.js
│   │   │   │       ├── test-pdf.html
│   │   │   │       └── test-pdf.js
│   │   │   └── variables_data_types.html
│   │   ├── development.md
│   │   ├── examples
│   │   │   └── driver.md
│   │   ├── exceptions.md
│   │   ├── fedora29-install.md
│   │   ├── functions.md
│   │   ├── game.md
│   │   ├── homework.md
│   │   ├── index.md
│   │   ├── linux_intro.md
│   │   ├── materials.md
│   │   ├── modules_packages.md
│   │   ├── python_intro.md
│   │   ├── rose-video-preview.jpg
│   │   ├── side-menu.js
│   │   └── variables_data_types.md
│   ├── examples
│   │   ├── best_driver.pyc
│   │   ├── none.py
│   │   ├── random-driver.py
│   │   ├── README.md
│   │   ├── score.pyc
│   │   └── zigzag.pyc
│   ├── how_to_check_student_exercises.md
│   ├── LICENSE
│   ├── Makefile
│   ├── MANIFEST.in
│   ├── Pipfile
│   ├── pytest.ini
│   ├── README.md
│   ├── rose
│   │   ├── client
│   │   │   ├── car.py
│   │   │   ├── component.py
│   │   │   ├── game.py
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   ├── track.py
│   │   │   └── world.py
│   │   ├── common
│   │   │   ├── actions.py
│   │   │   ├── config.py
│   │   │   ├── error.py
│   │   │   ├── __init__.py
│   │   │   ├── message.py
│   │   │   └── obstacles.py
│   │   ├── __init__.py
│   │   ├── res
│   │   │   ├── bg
│   │   │   │   ├── bg_1.png
│   │   │   │   ├── bg_2.png
│   │   │   │   └── bg_3.png
│   │   │   ├── cars
│   │   │   │   ├── car1.png
│   │   │   │   ├── car2.png
│   │   │   │   ├── car3.png
│   │   │   │   └── car4.png
│   │   │   ├── dashboard
│   │   │   │   └── dashboard.png
│   │   │   ├── end
│   │   │   │   └── final_flag.png
│   │   │   ├── obstacles
│   │   │   │   ├── barrier.png
│   │   │   │   ├── bike.png
│   │   │   │   ├── crack.png
│   │   │   │   ├── penguin.png
│   │   │   │   ├── trash.png
│   │   │   │   └── water.png
│   │   │   ├── soundtrack
│   │   │   │   └── Nyan_Cat.ogg
│   │   │   └── splash
│   │   │       └── splash_screen.png
│   │   ├── server
│   │   │   ├── game.py
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   ├── net.py
│   │   │   ├── player.py
│   │   │   ├── player_test.py
│   │   │   ├── score.py
│   │   │   ├── score_test.py
│   │   │   └── track.py
│   │   └── web
│   │       ├── game.css
│   │       ├── game.js
│   │       ├── index.html
│   │       └── jquery-3.2.1.min.js
│   ├── rose-admin
│   ├── rose-client
│   ├── rose-server
│   └── setup.py
├── Templates
├── test
│   └── tmp
├── thinclient_drives
└── Videos

9.cd /home/student/
Output:/home/student/

10.cd test/tmp/
Output:/home/student/test/tmp/
