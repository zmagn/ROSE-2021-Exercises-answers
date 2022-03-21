https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/01_Linux/homework_2.md

/home/student/

1.mkdir hw2
Output:hw2 shows up on "ls" command.

2.cd hw2/
Output:/home/student/hw2
mkdir songs drafts movies
Output:songs folder, drafts folder, movies folder shows up on "ls" command.

3.tree -d /home/student/
Output:
home/student/
.
├── Desktop
├── Documents
├── Downloads
├── hw1
│   ├── other
│   └── web
├── hw2
│   ├── drafts
│   ├── movies
│   └── songs
├── linux3
│   └── songs
├── Music
├── Pictures
├── Public
├── ROSE
│   ├── classroom
│   ├── docs
│   │   ├── course_materials
│   │   │   ├── exercises
│   │   │   │   ├── 00_Intro
│   │   │   │   ├── 01_Linux
│   │   │   │   ├── 02_Python_intro
│   │   │   │   ├── 03_Variables_and_datatypes
│   │   │   │   ├── 04_Compound_data_types
│   │   │   │   ├── 05_Control_structures
│   │   │   │   ├── 06_Functions
│   │   │   │   ├── 07_Exceptions
│   │   │   │   ├── 08_Modules_and_packages
│   │   │   │   ├── 09_Extra
│   │   │   │   └── test_exercises
│   │   │   │       ├── 01_Linux
│   │   │   │       ├── 03_Variables_and_datatypes
│   │   │   │       └── 04_Compound_data_types
│   │   │   ├── media
│   │   │   └── reveal
│   │   │       ├── css
│   │   │       │   ├── print
│   │   │       │   └── theme
│   │   │       │       ├── source
│   │   │       │       └── template
│   │   │       ├── js
│   │   │       ├── lib
│   │   │       │   ├── css
│   │   │       │   ├── font
│   │   │       │   │   ├── league-gothic
│   │   │       │   │   └── source-sans-pro
│   │   │       │   └── js
│   │   │       ├── plugin
│   │   │       │   ├── highlight
│   │   │       │   ├── markdown
│   │   │       │   ├── math
│   │   │       │   ├── multiplex
│   │   │       │   ├── notes
│   │   │       │   ├── notes-server
│   │   │       │   ├── print-pdf
│   │   │       │   ├── search
│   │   │       │   └── zoom-js
│   │   │       └── test
│   │   │           └── examples
│   │   │               └── assets
│   │   └── examples
│   ├── examples
│   └── rose
│       ├── client
│       ├── common
│       ├── res
│       │   ├── bg
│       │   ├── cars
│       │   ├── dashboard
│       │   ├── end
│       │   ├── obstacles
│       │   ├── soundtrack
│       │   └── splash
│       ├── server
│       └── web
├── Templates
├── test
│   └── tmp
├── thinclient_drives
└── Videos


4.touch songs/my_songs.txt
Output:
tree songs
songs
└── my_songs.txt

5.vim songs/my_songs.txt
(Press I Insert Mode)

Skazi Big Bass Line.
Side Of Ami San.
Ya Bint Al Sultan.
Where is Ramat Gan?
Ein Kmo Maccabi Haifa and blah.
So this is the song.
And I made this up.

(Press ESC to exit Insert Mode)
:wq - Save the file and exit.

Output:cat songs/my_songs.txt ---> the same text shows up.

6.head -n 4 songs/my_songs.txt 
Output:
Skazi Big Bass Line.
Side Of Ami San.
Ya Bint Al Sultan.
Where is Ramat Gan?

7.tail -n 2 songs/my_songs.txt 
Output:
So this is the song.
And I made this up.

8.cp songs/my_songs.txt songs/new_song.txt
Output:[student@zivm hw2]
tree songs
songs
├── my_songs.txt
└── new_song.txt

9.vim songs/new_song.txt 

(Press I Insert Mode)

Ziv
Skazi Big Bass Line.
Side Of Ami San.
Ya Bint Al Sultan.
Where is Ramat Gan?
Ein Kmo Maccabi Haifa and blah.
So this is the song.
And I made this up.
Ziv

(Press ESC to exit Insert Mode)
:wq - Save the file and exit.

Output:cat songs/my_songs.txt ---> the same text shows up.

10.[student@zivm hw2]$ diff songs/my_songs.txt songs/new_song.txt 
Output:
0a1
> Ziv
7a9
> Ziv

OR

[student@zivm hw2]$ vimdiff songs/my_songs.txt songs/new_song.txt
Output:
  --------------------------------------|  Ziv                                  
  Skazi Big Bass Line.                  |  Skazi Big Bass Line.
  Side Of Ami San.                      |  Side Of Ami San.
  Ya Bint Al Sultan.                    |  Ya Bint Al Sultan.
  Where is Ramat Gan?                   |  Where is Ramat Gan?
  Ein Kmo Maccabi Haifa and blah.       |  Ein Kmo Maccabi Haifa and blah.
  So this is the song.                  |  So this is the song.
  And I made this up.                   |  And I made this up.
  --------------------------------------|  Ziv                                  
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
  ~                                     |  ~                                    
songs/my_songs.txt    6,20           All songs/new_song.txt   7,20           All
Type  :qa!  and press <Enter> to abandon all changes and exit Vim

11.mv songs/new_song.txt drafts/
Output:
tree
.
├── drafts
│   └── new_song.txt
├── movies
└── songs
    └── my_songs.txt

12.cd ..
(home/student/)
tree -d

OR

while in hw2 folder I could tree -d /home/student/

Output:
/home/student/
.
├── Desktop
├── Documents
├── Downloads
├── hw1
│   ├── other
│   └── web
├── hw2
│   ├── drafts
│   ├── movies
│   └── songs
├── linux3
│   └── songs
├── Music
├── Pictures
├── Public
├── ROSE
│   ├── classroom
│   ├── docs
│   │   ├── course_materials
│   │   │   ├── exercises
│   │   │   │   ├── 00_Intro
│   │   │   │   ├── 01_Linux
│   │   │   │   ├── 02_Python_intro
│   │   │   │   ├── 03_Variables_and_datatypes
│   │   │   │   ├── 04_Compound_data_types
│   │   │   │   ├── 05_Control_structures
│   │   │   │   ├── 06_Functions
│   │   │   │   ├── 07_Exceptions
│   │   │   │   ├── 08_Modules_and_packages
│   │   │   │   ├── 09_Extra
│   │   │   │   └── test_exercises
│   │   │   │       ├── 01_Linux
│   │   │   │       ├── 03_Variables_and_datatypes
│   │   │   │       └── 04_Compound_data_types
│   │   │   ├── media
│   │   │   └── reveal
│   │   │       ├── css
│   │   │       │   ├── print
│   │   │       │   └── theme
│   │   │       │       ├── source
│   │   │       │       └── template
│   │   │       ├── js
│   │   │       ├── lib
│   │   │       │   ├── css
│   │   │       │   ├── font
│   │   │       │   │   ├── league-gothic
│   │   │       │   │   └── source-sans-pro
│   │   │       │   └── js
│   │   │       ├── plugin
│   │   │       │   ├── highlight
│   │   │       │   ├── markdown
│   │   │       │   ├── math
│   │   │       │   ├── multiplex
│   │   │       │   ├── notes
│   │   │       │   ├── notes-server
│   │   │       │   ├── print-pdf
│   │   │       │   ├── search
│   │   │       │   └── zoom-js
│   │   │       └── test
│   │   │           └── examples
│   │   │               └── assets
│   │   └── examples
│   ├── examples
│   └── rose
│       ├── client
│       ├── common
│       ├── res
│       │   ├── bg
│       │   ├── cars
│       │   ├── dashboard
│       │   ├── end
│       │   ├── obstacles
│       │   ├── soundtrack
│       │   └── splash
│       ├── server
│       └── web
├── Templates
├── test
│   └── tmp
├── thinclient_drives
└── Videos

13.mv /home/student/hw2/songs/my_songs.txt /home/student/hw2/songs/your_song.txt
Output:
ls /home/student/hw2/songs/
your_song.txt
[student@zivm ~]$

14.cat hw2/songs/your_song.txt
Output:
Skazi Big Bass Line.
Side Of Ami San.
Ya Bint Al Sultan.
Where is Ramat Gan?
Ein Kmo Maccabi Haifa and blah.
So this is the song.
And I made this up.

15.clear OR CTRL + L
Output: (It's empty)

16.wc -l hw2/songs/your_song.txt
Output:7 hw2/songs/your_song.txt

