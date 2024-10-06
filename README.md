# FirstYear_Semester1
A strategy board game. The aim of the game is to be the first player to move their own pieces into the right position in front of appropriate sink fields in order to finally move them into the sinks and make them disappear.

GRADE: 85.45 %


Note: Uses SU stdlibs

command-line: <board_size_rows><Board_size_cols><gui_mode> 
standard input as setup and commands

run:
10 10 0 < input.txt


Documentation:

Computer Science 113/114 Semester Project: A three-dimensional board game¶
The second semester project description for CS144 can be found here: LINK.
Project Introduction¶
For the CS113/4 project you will need to implement a strategy board game. The aim of the game is to be the first player to move their own pieces into the right position in front of appropriate sink fields in order to finally move them into the sinks and make them disappear.
Deadlines¶
The project is split into three hand-ins and a demo:
Hand-in	Deadline
First hand-in	Tuesday, 19 March @ 23h55
Second hand-in	Tuesday, 9 April @ @ 23h55
Final hand-in	Monday, 6 May @ 23h55
Demo	To be schedules
This project is to be done individually. This means all of your code has to be your own and teamwork is strictly prohibited. The use of ChatGPT or similar code assistants is strictly forbidden and also considered plagiarism. Any form of plagiarism will be dealt with according to the university’s policy.
All programming knowledge required to complete this project will be covered in class, so it is imperative that you attend classes and stay up to date with the course work. Remember to work on the project steadily throughout the semester. You will not finish if you attempt to do the entire project the day before the deadline. You will most likely run into problems or bugs that take time to find and resolve, so start early and work consistently. Make sure that your project is backed-up in some form or another (flash drive and in the Cloud for example). A computer breaking or a harddrive being eaten by a dog is not an accepted excuse.
Late hand-in will automatically be given a mark of 0.
Questions about the project¶
If you have questions about the project you should follow the steps below:
1.	First ask a fellow student for clarification. Note fellow students are only allowed to give clarifications on helping you to understand the project specifications or help you to set up your computer so that you can write and execute programs. They are not allowed to help you with any of the coding.
2.	If Step 1 does not answer your question, ask one of your class reps.
3.	If Step 2 fails, check if a similar question has been asked and answered on the Microsoft Teams dedicated to this project that answers your question.
4.	If Step 3 fails, create a question on the dedicated Microsoft Teams team. We do not accept direct messages on Teams. Questions that have been addressed by the project specification will be ignored and deleted.
5.	If step 4 fails, ask a Mentor during a mentor session or a Demi during a practical session.
6.	After step 5, if you believe you found an error/ambiguity in the game logic or project specifications, please send an email to cs1project@sun.ac.za with the email subject containing: Project Error - where is your student number. All other emails will be ignored.
Using this document¶
•	On the left side of the page are the different sections of the project specification.
•	On the right side of the page is the table of contents for the current section.
•	On the top right is a search bar that can be used to search for keywords. Use this to check if your questions have not already been answered somewhere on the site.
•	Read and UNDERSTAND the content of the project specification before writing any code!

Game rules¶
This game can only be played by two players.
The player with the light stones starts the game with their turn. The players then take alternating turns. On a player’s turn, each player has to make two moves.
Players take turns repeatedly until the game win/lose condition is met.
Setup¶
The components of the game are:
•	A n by m rectangular game board comprising mxn square board fields.
•	k playing pieces that each can take on one of the following shapes where l, w, h are the lengths, width, and height of a piece in its initial orientation at the beginning of the game.
•	The number of sinks (s), each with dimensions l and w indicating height and width of the sink field.
There are four different playing piece types (l x w x h) with associated piece values:
Dimensions (l, w, h)	Piece type	Piece value	Description
1x1x1	a	1	A normal six-sided die.
1x1x2	b	2	A right rectangular prism with height 2.
1x1x3	c	3	A longer right rectangular prism with height 3.
2x2x2	d	4	A cube with sides of length 2.
There are two different board sink field dimensions:
•	1x1
•	2x2
Illustrative example of a board game:
 
This illustrative board game is of size 10 by 10, comprises four sinks, and 10 playing pieces. Each player has two 1x1x1 pieces, one 2x2x2 piece, one 1x1x2 piece, and one 1x1x3 piece.
The game board coordinates are defined as (0,0) in the bottom left corner. The bottom right corner has coordinates (9,0). Therefore, the coordinates of the various pieces from the illustrative example above are:
•	2x2 sinks at coordinates (1,1) and (7,7).
•	1x1 sinks at coordinates (7,2) and (2,7).
•	2x2x2 playing pieces at coordinates (3,5) and (5,3) for the grey and white player respectively.
•	1x1x3 playing pieces at coordinates (4,4) and (5,5) for the white and grey player respectively.
•	1x1x2 playing pieces at coordinates (3,3) and (6,6) for the white and grey player respectively.
•	1x1x1 playing pieces at coordinates (3,4) and (4,3) for the grey player and (5,6) and (6,5) for the white player.
Rules for starting positions¶
•	Sink fields may not be placed so that they are directly adjacent to other sink fields (to the left, right, up or down).
•	Sink fields are only allowed on board fields that belong to the outer three rows or columns of the game board.
•	Conversely, during game setup and before the first turn is started, playing pieces are only allowed to be on board fields that do not belong to the outer three rows or columns of the game board.
•	During game setup and before the first turn is started, playing pieces may only be placed on their shortest sides.
Win/Lose Conditions¶
•	The player who is the first to sink enough of their own playing pieces into any of the board sink fields such that the sum of their values is equal to or higher than 4, wins the game.
•	A player loses if they can not make any legal moves.
Moving playing pieces¶
Making moves in the game is conditioned on the piece to be moved. Generally, a player is only allowed to move a piece across one of its edges to the next free board field(s).
Illustrative example with a 1x1x2 piece:¶
If the playing piece is upright it may be tilted onto two adjacent fields. See figure below:
   
If the playing piece is lying on its long side, it may be rolled over the long edge onto two adjacent fields. See figure below:
   
If the playing piece is lying on its long side, it may be tipped over a short edge so that it stands upright on an adjacent field. See figure below:
   
Rules for moving pieces¶
•	A player must make the two moves per turn with the same piece or with two different pieces.
•	Exception: a single legal move of the 2x2x2 piece counts as two moves.
•	A player is only allowed to make moves with pieces that belong to them.
•	A playing piece may only be moved onto free fields.
•	On a player’s turn, they must make two moves.
•	In a single turn, it is forbidden to move a piece and return it to its starting position on the second move.
•	A game piece may never be moved beyond the boundary of the game board.
•	A game piece may never be moved over a sink field, unless the game piece is sunk into it wholly.
Sinking playing pieces¶
In order to sink a playing piece into a sink field, it needs to be in the appropriate position so that it can be tipped or rolled into the sink field with a legal move. For example, using a 1x1x2 game piece and a 1x1 sink field, it can only be sunk as depicted below:
     
Once a piece is sunk, it is removed from the board. The player who first sinks enough of their playing pieces such that their combined piece values is higher or equal to 4 wins the game.
Game strategies¶
The tactical aim is to give your opponent the least possible space to make their moves and to block as many of their pieces with as few of your own as possible.
Special moves and fields¶
Special move	Description
Blocked Fields	Before the game commences board fields may be demarcated as blocked. Playing pieces may not be moved onto blocked fields. Blocked fields remain active throughout the entire game.
Hidden Bombs	Before each player’s turn they may choose a non-blocked board field under which to hide a bomb. If any player moves a playing piece onto a field with a hidden bomb the playing piece is immediately removed from the current game. The hidden bomb is discarded. If a hidden bomb is placed on a board field that already contains a hidden bomb both explode and can no longer be triggered.
Freezing Playing Pieces	Twice in a game a player may choose to freeze an opponent’s playing piece. A frozen playing piece may not be moved. Once frozen a playing piece remains frozen for 2 moves. Freezing an opponent’s playing piece is not considered a move.
Moving a Sink Field	Twice in a game a player may choose to move a sink field one position to the left, right, up, or down conditioned on the board field(s) that the sink is moved to are part of the defined board and are not blocked, and that no other sink field is directly adjacent to the moved sink. It should be noted that it is possible to sink a playing piece by moving a sink field “underneath” it. Moving a sink field is considered a single move.


Program Specifications¶
This section details the requirements for the input and output of the implementation of this project. Note that these requirements must be followed exactly. To test your implementation, you may use the pre-submission testing facilities available on SunLearn. See pre-submission testing facilities for more information on these facilities.
Arguments¶
When your program is executed, it takes in three command-line arguments in the following order:
1.	The height of the board (number of rows) as an integer between 8 and 10 inclusive.
2.	The width of the board (number of columns) as an integer between 8 and 10 inclusive.
3.	The GUI indicator as an integer:
•	0 means the game is played in the terminal (text mode).
•	1 means the game is played in the GUI (graphical mode).
You must perform argument validation. If an invalid value is given for any command-line argument, the following error message(s) must be displayed:
•	ERROR: Illegal argument
If too few/too many arguments are given, the program must be terminated with the appropriate error message:
•	ERROR: Too few arguments
•	ERROR: Too many arguments
Program Input¶
When your program is started in terminal mode, it must read all input from stdio, see Coding Specifications for a description of the functions you are required to use. When started in GUI mode, your program may read the board setup input (as described below) from stdio, but must allow moves to be done on the GUI.
Board Setup Input¶
The input given on standard input begins with the lines for the board setup, followed by a # signalling the end of the board setup. Each line in the board setup contains the details of a single board object (a sink, a piece, or a blocked field). Every line begins with a string representing the type of object that is described:
•	s: represents a sink
•	x: represents a blocked field
•	d: represents a piece belonging to the dark player
•	l: represents a piece belonging to the light player
If the object type is a blocked field, the string will be followed by two integers, representing the row and column of the blocked field's locations, respectively.
If the object type is a sink, the string will be followed by an integer, representing the piece type n of the sink (where n represents an nxn sized sink), and then by two integers representing the row and column of the sink's location, respectively. The following are valid piece types for a sink:
Sink Type	Size (lxw)
1	1x1
2	2x2
If the object represents either player's pieces (i.e., d or l), the string will be followed by a second string, representing the piece type, and then by integers representing the row and column of the piece's location, respectively. The following are the valid piece types for a player's piece:
Piece Type	Size (lxwxh)
a	1x1x1
b	1x1x2
c	1x1x3
d	2x2x2
NOTE: all individual input elements in an input line are space-separated.
NOTE: There is no order for the objects read in during the board setup. Your program must support reading in the board objects in any order.
Once all of the board objects are read in, and the final # is read, your program must print the board and begin the playing of the game.
Move Input¶
When in terminal mode, after the board setup (and the # at the end), your program must begin to read moves from stdio.
Your program must continue reading input until either the game is won/lost (due to the win/lose conditions) OR until standard input is empty. A game input that ends without a win/lose condition but with standard input being empty is called a partial game. Your program must not print anything additional at the end of a partial game, but must ensure that it prints the board after processing the last move.
Each move must be on its own line, and consists of two integers and a string (space-separated) in that order. The two integers represent the row and column respectively of the object or field involved in the move. The string represents the move action. The following are the valid move actions:
•	l: Move the piece/sink to the left
•	r: Move the piece/sink to the right
•	u: Move the piece/sink up
•	d: Move the piece/sink down
•	b: Place a bomb on the given field
•	f: Freeze the selected piece
NOTE: Your program must do validation on the move input to ensure that:
1.	If a piece/sink is being moved, that there is a piece/sink at the coordinate given.
2.	If a bomb is being placed, that the coordinate given is not a blocked field and does not already contain a piece or sink.
3.	If a piece is being frozen, that there is a piece at the coordinate given, and that it belongs to the opposite player.
In addition to move input validation, your program must also validate that the move is legal according to the Game rules.
Example inputs¶
The following is a few examples of inputs that will be given to your program. To test if your program reads input correctly, refer to the pre-submission testing facilities.
The following is an example of input for a board setup for a 10x10 board:
s 1 2 7
s 2 1 1
s 2 7 7
s 1 7 2
x 0 0
x 0 9
x 9 0
x 9 9
d d 3 5
d a 3 4
l b 3 3
l c 4 4
d a 4 3
l a 5 6
d c 5 5
l d 5 3
d b 6 6
l a 6 5
The following is an example of input for board setup and moves using a 10x10 board where light wins:
s 2 1 7
s 2 1 1
s 2 7 7
s 2 7 1
l a 3 3
l a 6 6
l a 6 3
l a 3 6
d a 4 4
d a 4 5
d a 5 4
d a 5 5
#
3 3 l
3 2 d
4 4 l
4 3 d
6 6 r
6 7 u
5 5 r
5 6 u
3 6 r
3 7 d
4 5 r
4 6 d
6 3 l
6 2 u
Program output¶
When run in terminal mode, the only output of the program should be error messages (see error messages, win/lose messages, and boards, which are printed after every move (including a move that results in a win/lose condition). The following is an example of how the board must be printed (from the first example input above):
   0  1  2  3  4  5  6  7  8  9
  +--+--+--+--+--+--+--+--+--+--+
9 | x|  |  |  |  |  |  |  |  | x|
  +--+--+--+--+--+--+--+--+--+--+
8 |  |  |  |  |  |  |  | s| s|  |
  +--+--+--+--+--+--+--+--+--+--+
7 |  |  | s|  |  |  |  | s| s|  |
  +--+--+--+--+--+--+--+--+--+--+
6 |  |  |  |53|53| a| B|  |  |  |
  +--+--+--+--+--+--+--+--+--+--+
5 |  |  |  | d|53| C| a|  |  |  |
  +--+--+--+--+--+--+--+--+--+--+
4 |  |  |  | A| c|35|35|  |  |  |
  +--+--+--+--+--+--+--+--+--+--+
3 |  |  |  | b| A| D|35|  |  |  |
  +--+--+--+--+--+--+--+--+--+--+
2 |  | s| s|  |  |  |  | s|  |  |
  +--+--+--+--+--+--+--+--+--+--+
1 |  | s| s|  |  |  |  |  |  |  |
  +--+--+--+--+--+--+--+--+--+--+
0 | x|  |  |  |  |  |  |  |  | x|
  +--+--+--+--+--+--+--+--+--+--+
The following rules must be applied when printing the board:
•	Each field must be printed as two characters.
•	An empty field must be printed as two space characters ( ).
•	Sinks must be displayed as a space followed by s on all fields they occupy.
•	Blocked fields must be displayed as a space followed by x.
•	Pieces belonging to the dark player must be displayed in capitals, and pieces belonging to the light player in lowercase letters.
•	Each piece must be displayed in the following way:
•	The bottom left-most field belonging to the piece must have the piece type as a single letter (a, b, c, or d) with a space character before it.
•	Every other field belonging to the piece must have an integer representing the bottom left-most field the piece occupies, where the integer is calculated as: rowx(number of columns) + column. For example, in the example board above, the d piece belonging to the light player with bottom left-most field 5 3 has the identifier: 5x10 + 3 = 53, which is then displayed on the other 3 board fields the piece occupies. The integer must be padded on the right by single space if it is a single digit.
•	The board must be followed/terminated by a newline character (\n)
NOTE: You are not required to print out hidden bombs and frozen pieces, these aspects of the game should be checked internally by your program but not visible on the board.
Win/lose messages¶
If a game results in a win or lose condition for either of the players, the following messages must be printed out after printing the board on which the win/lose condition is met.
Win message¶
•	Light:
•	Light wins!
•	Dark:
•	Dark wins!
Lose message¶
•	Light:
•	Light loses
•	Dark:
•	Dark loses
NOTE: The above-mentioned messages must be printed out exactly as indicated above (note capitalizations and exclamation marks !). When printed out, the win or lose messages above must be followed by a newline character (\n). To test your implementation, make use of the Pre-submission testing facilities.
Error messages¶
If your program encounters an illegal board object, illegal move, or any other error, it must print the corresponding error message. In terminal mode, it must terminate directly after printing the message. In GUI mode, your program may terminate, or continue running (so that you can continue playing by trying a different move, for example). All error messages must be followed/terminated by a newline character (\n). The following is a comprehensive list of all the error messages your program is required to produce under various circumstances:
•	When a coordinate given is not an integer or is out of the range of the board (both in the board setup and move input):
•	ERROR: Field r c not on board, where r (row) and c (column) is the field given
•	When the object type (first string on a line of the board setup input) is not one of the legal object types (legal object types are s, l, d and x):
•	ERROR: Invalid object type t, where t is the invalid object type string
•	When the piece type for a sink or a player's piece is not one of the legal piece types (legal piece types are 1 or 2 for a sink and a, b, c, and d for a player piece):
•	ERROR: Invalid piece type t, where t is the invalid piece type string
•	When an attempt is made to place a sink that will not be fully in the outer three rows or columns:
•	ERROR: Sink in the wrong position
•	When an attempt is made to place a piece that will be in the outer three rows or columns:
•	ERROR: Piece in the wrong position
•	When an attempt is made to place a piece, sink or blocked field, or to move a piece or sink on/to a field that is not empty:
•	ERROR: Field r c not free, where r (row) and c (column) is the first coordinate starting from the bottom left that is not empty
•	When the direction given for a move is not one of the valid directions listed here:
•	ERROR: Invalid direction d, where d is the invalid direction
•	When an attempt is made to place a bomb after the first move of a player's turn, or after a bomb has already been placed:
•	ERROR: Cannot place bomb after move
•	When an attempt is made to freeze a piece after that player has already frozen twice in a game:
•	ERROR: No freezings left
•	When a player attempts to move a piece that does not belong to them, OR when a player attempts to freeze their own piece:
•	ERROR: Piece does not belong to the correct player
•	When the coordinate given for a move does not a piece on that field:
•	ERROR: No piece on field r c, where r (row) and c (column) is the coordinate given
•	When a player attempts to move one of their own pieces that is currently frozen:
•	ERROR: Cannot move frozen piece
•	When a player attempts to move a sink after that player has already moved a sink twice in the current game:
•	ERROR: No sink moves left
•	When an attempt is made to move a 2x2x2 (b type) piece after the first move of a player's turn:
•	ERROR: Cannot move a 2x2x2 piece on the second move
•	When an attempt is made to move a piece/sink when the move would result in the piece/sink being moved off the board:
•	ERROR: Cannot move beyond the board
•	When an attempt is made on the second move of a player's turn to move a piece/sink back to the position it was in before the first move of that player's turn:
•	ERROR: Piece cannot be returned to starting position
•	When an attempt is made to move or place a sink so that it occupies a field directly adjacent (to the left, right, up or down) to another sink:
•	ERROR: Sink cannot be next to another sink
•	When the program is supplied with less than 3 command-line arguments:
•	ERROR: Too few arguments
•	When the program is supplied with more than 3 command-line arguments:
•	ERROR: Too many arguments
•	When the program is supplied with an invalid command-line argument:
•	ERROR: Illegal argument


GUI Mode¶
This section describes the requirements for GUI mode, as well as suggestions for what your GUI mode may look like. Note that the requirements in this section must be followed exactly, however any suggestions given are just to give you an idea of what the GUI mode should look like, and are not required.
NOTE: Although the GUI counts a noticeable amount to your final project mark, it does not have a higher mark allocation than the rest of the project. Please do not spend most of your time making your GUI look nice. Although there may be a few marks for your GUI's aesthetics, a nice looking GUI alone will not allow you to pass the project. You are encouraged to focus on the functionality (i.e. implementing the rules of the game) first, and ensuring this is done well before implementing the GUI.
Starting GUI mode¶
Your program must start GUI mode when executed with the command line argument for GUI indicator equal to 1 (see Arguments). Your program must still start in terminal mode if the GUI indicator is equal to 0.
GUI functionality¶
All of the functionality of the game described in game rules must be available in GUI mode, including the special moves and fields.
GUI input¶
Your program must implement input of the board setup and moves. You are, however, free to decide how you implement input, provided that you are not using any external libraries that are not allowed. The following are suggestions for how you may implement input in GUI mode:
•	You may implement move input by handling mouse clicks on the GUI.
Example: You may handle mouse clicks on the GUI by using stddraw.mouseX(), stddraw.mouseY() and stddraw.mousePressed(). stddraw.mousePressed() returns True if the mouse has been pressed since you last checked, or False otherwise, stddraw.mouseX() and stddraw.mouseY() returns the x and y coordinate respectively of the position of the mouse when it was clicked last. The following code snippet gives an example for how to wait for and get location of a mouse click:
while (not stddraw.mousePressed()):
  stddraw.show(0)
y_coord = int(stddraw.mouseY())
x_coord = int(stddraw.mouseX())
•	You may implement move input by handling keyboard input on the GUI.
Example: You may handle the keys pressed on the keyboard by using stddraw.nextKeyTyped() and stddraw.hasNextKeyTyped(). NOTE: Each key press from the GUI is stored in a queue. stddraw.hasNextKeyTyped() returns True if there is one or more key presses still on the queue (i.e. the program user has pressed a key that you have not yet handled), or False otherwise. stddraw.nextKeyTyped() returns the character of the key that has been pressed at the front of the key queue, subsequent calls to stddraw.nextKeyTyped() will return the next elements in the queue, provided the queue is not empty. The following code snippet gives an example for how to wait for and get a single next key pressed:
while (not stddraw.hasNextKeyTyped()):
  stddraw.show(0)
key_pressed = stddraw.nextKeyTyped()
•	You may implement board setup and move input in GUI mode with standard input using stdio as in the terminal mode.
•	You may use any other way for implementing input for the GUI, provided you adhere to the rules outlined in the rest of the project specification, especially in the Coding specifications.
GUI visualization¶
Your program must visualize the game using stddraw when in GUI mode. You are not allowed to use pygame directly or any other library for your GUI visualization. Your visualization must contain row and column numbering, and must display and update the game board while the game is played. You are, however, free to decide how your GUI may look. Below is a screenshot of how your GUI may look, and should be an indication of what is expected, but is not required.
 


Code Specifications¶
This section details the requirements and guidelines that you must follow when coding this project. Your code will be analysed to identify whether or not these requirements are satisfied. Any non-adherence to the following specifications will attract mark penalties or result in a mark of 0. If you are unsure of something, please follow the steps in Questions about the Project.
Classes¶
Your project may only consist of one file, namely the SUxxxxxxxx.py file. You are NOT allowed to use object-oriented programming (OOP) during the development of your program. Therefore, no classes should be defined within your Python file. You are not allowed to use any type annotation. If you don’t know what that is, good. You will learn about these in CS144.
Libraries¶
You must ONLY use the standard libraries provided by the university. Refer to Tutorial0 on SunLearn on how to install the required SU standard libraries.
The explicit use of numpy, as well as the use of any other external libraries is strictly prohibited.
Input and output¶
You are only allowed to use the stdio module from the standard libraries when working with input/ output. Using functions such as open() or input() would be disastrous and could cause you to receive zero for the project. You are also not allowed to use sys.stdin to read from standard input. You must use stdio.
When working with input, we highly recommend you use stdio.readString() exclusively to read individual inputs from standard input only when you program expects to find an input. Although you are allowed to use functions such as stdio.readLine(), stdio.readAllLines(), or stdio.readAllStrings(), we highly recommend you only use stdio.readString().
Graphical User Interface (GUI)¶
You must use the stddraw module from the standard libraries for displaying the GUI in GUI mode. Your program may not use any other library to draw the graphical user interface. In particular, your program must not use pygame, or call any pygame functions in your program. You may only use the standard functions provided by the stddraw module.
Global variables¶
The use of global variables is permitted, however please keep the number of global variables reasonable.
Functions¶
The use of functions is permitted for all hand-ins. There are functions that have been provided to you in the skeleton code. There are no functions that must be used, all are left up to your discretion. The functions may be modified, left as is, or may go simply unused.
Documentation and style¶
Your program must be well documented with comments, so that it is easy for anyone to understand how your project is structured as well as making it much easier for it to be marked. It is important to use meaningful names for variables and functions. Neat code is also much easier to debug, so make sure you indent correctly.
Compatibility¶
Please note that your program will have to be coded in Python 3.8.0, 3.8.10 (NARGA), or 3.11.7.4 (FHARGA). Please refer to Tutorial0 on SunLeanr on how to install the correct python version on your personal computers.
For hand-ins 1 and 2, make use of the Smoke Test and MVP Test to check whether you have compatibility issues.
For the final hand-in, it is your responsibility to check that your program works properly on the lab computers in NARGA/FHARGA.
For CS114 students we will use the NARGA computers to test submitions, as well as to conduct the demos of your final projects. Please ensure that your program works on Ubuntu on the NARGA computers.
For CS113 students we will use the FHARGA computers to test submitions, as well as to conduct the demos of your final projects. Please ensure that your program works on Windows on the FHARGA computers.


Skeleton Code¶
Welcome to the project skeleton page, where we will introduce you to the concept of skeleton code, and explain how you should use the project skeleton throughout the development process.
The project skeleton is supplied as a starting point for your project. By carefully studying its contents, you will be able to use it as a guide throughout the development process. The project skeleton is a Python file that contains skeleton code, which establishes the basic structure of the project. It can be downloaded from here.
The skeleton file, SUxxxxxxxx.py, contains the following:
•	Function signatures which can be used as a starting point for the project.
•	Documentation, which often includes hints about the program's functionality.
At first, the skeleton might seem slightly overwhelming. There is a fair amount of text, the majority of which is documentation that explains what each function may be used for. Do not let this intimidate you. The skeleton is designed to help you.
Summary of Important Considerations¶
This section will emphasize some of the most important points to consider while implementing your solution.
Renaming Your File Before Submission¶
When you begin working with the skeleton file, it is a good idea to first rename the skeleton file to be specific to you. You must rename the skeleton file named SUxxxxxxxx.py by replacing the xxxxxxxx part with your own SU student number. For example, if your student number is 12345678, you will rename the file to SU12345678.py. NOTE: You must rename your skeleton file before you submit it to SunLearn for the second (and third) hand-in. If you fail to do this, our automated marking scripts will not be able to mark your submission.
How to use the project skeleton¶
Most of the project skeleton consists of function signatures. These are lines of code that describe a particular function (if you don't know what this is yet, don't worry, you will learn about it in this course). You are not required to use the functions provided in the skeleton code, and they are only provided as a guideline for what we think would be a good way to structure your program. Following this structure will help you not to make things hard to implement later on in the project when your program gets more complex. That being said, you are free to modify any of the functions given in the skeleton code, and to add and remove functions as you see fit. You may also add and remove arguments to the functions given in the skeleton code if you do not use the ones given, or need to use others. You may also add global variables to the skeleton code in the section provided. We however urge you to try to keep the number of global variables in your program to a minimum, as too many global variables may make it harder to find errors in your program.
Making sure you have a program entry point¶
There is only one aspect of the skeleton file that you must keep and have in your submissions. This is the program entry point, which begins with the line:
if __name__ == "__main__":
The code after this will be the first code to run when your program is started. In the skeleton file, some code is provided here to give you an indication of how to run your program. However you must change this code before submitting your program for the second and third hand-in. You however must not remove the line if __name__ == "__main__":, as this would restrict us from running your program correctly.
Only Use the Python and Booksite Standard Libraries¶
You are strictly forbidden from importing any libraries or modules that are not part of the Python standard libraries or the booksite library (stdio/stdarray/stddraw). If you use an unsupported library/ module, your program will not be marked.
NOTE: Do not download the textbook's libraries from the Princeton website -- they do not work. The university supplies you with a patched version of the booksite libraries which will be available on SunLearn. You must download these files and install them according to the installation instructions provided with the libraries.

