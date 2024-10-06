"""
Skeleton code for CS114 project 2024: A 3D board game.

This skeleton code for the project is intended as a starting point for students
to get an idea of how they can begin to code the project. You are not required
to use any of the functions in this skeleton code, however you may find some of
the ideas useful. You are however required to have the line:

if __name__ == "__main__":

but you are free to and should modify the lines following this.

None of the functions are implemented yet, so if you would like to
use a particular function, you need to implement it yourself. If you decide not
to use any of the functions, you are free to leave them empty or remove them
from this file. You are also free to alter the function signatures (the name of
the function and its arguments), so if you need to pass more arguments to the
function, or do not need a particular argument, you are also free to add and
remove arguments as you see fit. We provide the function signatures only as a
guide for how we think you can start to approach the project.
"""

# imports
# Your imports go here
import sys
import stdio
import stdarray
import stddraw

# global variables
# Your global variables go here

global row_input
global col_input
global moved_d
global move_count
global sink_move_dark
global sink_move_light
global all_moves
global counter
global bombs


def find_sink_fields(row, col, board):
    '''
        Find all the fields belonging to a sink

        args:
            row(int) :  value of the row of the sink being checked
            col(int) :  value of the column of the sink being checked
            board(2D array of str) : The game board

        returns:
            Values(array of str) : the row and column of all the fields of the sink
    '''
    values = [str(row) + str(col)]
    if row == 0 :
        if col == 0 :
            if board[row][col+1] == ' s' : values += [str(row)  + str(col+1)]
            if board[row+1][col+1] == ' s' : values += [str(row+1)  + str(col+1)]
            if board[row+1][col] == ' s' : values += [str(row+1)  + str(col+1)]
        elif col == col_input-1 :
            if board[row][col-1] == ' s' : values += [str(row)  + str(col-1)]
            if board[row+1][col-1] == ' s' : values += [str(row+1)  + str(col-1)]
            if board[row+1][col] == ' s' : values += [str(row+1)  + str(col)]
        else:
            if board[row+1][col-1] == ' s' : values += [str(row+1)  + str(col-1)]
            if board[row+1][col] == ' s' : values += [str(row+1)  + str(col)]
            if board[row+1][col+1] == ' s' : values += [str(row+1)  + str(col+1)]
            if board[row][col-1] == ' s' : values += [str(row)  + str(col-1)]
            if board[row][col+1] == ' s' : values += [str(row)  + str(col+1)]
    elif row == row_input-1:
        if col == 0 :
            if board[row][col+1] == ' s' : values += [str(row)  + str(col+1)]
            if board[row-1][col+1] == ' s' : values += [str(row-1)  + str(col+1)]
            if board[row-1][col] == ' s' : values += [str(row-1)  + str(col)]
        elif col == col_input-1 :
            if board[row][col-1] == ' s' : values += [str(row)  + str(col-1)]
            if board[row-1][col-1] == ' s' : values += [str(row-1)  + str(col-1)]
            if board[row-1][col] == ' s' : values += [str(row-1)  + str(col)]
        else:
            if board[row-1][col-1] == ' s' : values += [str(row-1)  + str(col-1)]
            if board[row-1][col] == ' s' : values += [str(row-1)  + str(col)]
            if board[row-1][col+1] == ' s' : values += [str(row-1)  + str(col+1)]
            if board[row][col-1] == ' s' : values += [str(row)  + str(col-1)]
            if board[row][col+1] == ' s' : values += [str(row)  + str(col+1)]
    else:
        if col == 0 :
            if board[row-1][col] == ' s' : values += [str(row-1)  + str(col)]
            if board[row-1][col+1] == ' s' : values += [str(row-1)  + str(col+1)]
            if board[row+1][col] == ' s' : values += [str(row+1)  + str(col)]
            if board[row+1][col+1] == ' s' : values += [str(row+1)  + str(col+1)]
            if board[row][col+1] == ' s' : values += [str(row)  + str(col+1)]
        elif col == col_input-1 :
            if board[row-1][col-1] == ' s' : values += [str(row-1)  + str(col-1)]
            if board[row-1][col] == ' s' : values += [str(row-1)  + str(col)]
            if board[row+1][col-1] == ' s' : values += [str(row+1)  + str(col-1)]
            if board[row+1][col] == ' s' : values += [str(row+1)  + str(col)]
            if board[row][col-1] == ' s' : values += [str(row)  + str(col-1)]
        else:
            if board[row-1][col-1] == ' s' : values += [str(row-1)  + str(col-1)]
            if board[row-1][col] == ' s' : values += [str(row-1)  + str(col)]
            if board[row-1][col+1] == ' s' : values += [str(row-1)  + str(col+1)]
            if board[row][col-1] == ' s' : values += [str(row)  + str(col-1)]
            if board[row][col+1] == ' s' : values += [str(row)  + str(col+1)]
            if board[row+1][col-1] == ' s' : values += [str(row+1)  + str(col-1)]
            if board[row+1][col+1] == ' s' : values += [str(row+1)  + str(col+1)]
            if board[row+1][col] == ' s' : values += [str(row+1)  + str(col)]

    return values


def check_sink_range(board,row_input, col_input, row, col, type):
    '''
        Check if sink placement is valid

        args:
            board(2D array of str): The game board
            row_input(int): The amount of rows on the game board
            col_input(int): The  amount of columns on the game board
            row(int): The value of the row being checked
            col(int): the value of the column being checked
            type(str): the type of piece being placed
    '''
    temp_board = stdarray.create2D(row_input,col_input,"  ")
    valid = True
    #valid plot
    ##########################################

    if type == '2' :
        for i in range(2,row_input-3):
            for j in range(2,col_input-3):
                temp_board[i][j] = ' I'
        for i in range(row_input):
            temp_board[i][col_input-1] = ' I'
        for i in range(col_input):
            temp_board[row_input-1][i] = ' I'
    else:
        for i in range(3,row_input-3):
            for j in range(3,col_input-3):
                temp_board[i][j] = ' I'

    for i in range(row_input):
        for j in range(col_input):
            if not board[i][j] == '  ' :
                temp_board[i][j] = ' N'

    for i in range(row_input):
            for j in range(col_input):
                if board[i][j] == " s" :
                    temp_board[i][j] = ' S'
                    if i == 0:
                        if j == 0:
                            temp_board[i+1][j] = ' S' #bo
                            temp_board[i][j+1] = ' S' #regs
                        else:
                            if j == col_input-1:
                                temp_board[i+1][j] = ' S' #bo
                                temp_board[i][j-1] = ' S' #links
                            else:
                                temp_board[i+1][j] = ' S' #bo
                                temp_board[i][j-1] = ' S' #links
                                temp_board[i][j+1] = ' S' #regs
                    else:
                        if i == row_input-1:
                            if j == 0:
                                temp_board[i-1][j] = ' S' #onder
                                temp_board[i][j+1] = ' S' #regs
                            else:
                                if j == col_input-1:
                                    temp_board[i-1][j] = ' S' #onder
                                    temp_board[i][j-1] = ' S' #links
                                else:
                                    temp_board[i-1][j] = ' S' #onder
                                    temp_board[i][j-1] = ' S' #links
                                    temp_board[i][j+1] = ' S' #regs
                        else:
                            if j == 0:
                                temp_board[i+1][j] = ' S' #bo
                                temp_board[i-1][j] = ' S' #onder
                                temp_board[i][j+1] = ' S' #regs
                            else:
                                if j == col_input-1:
                                    temp_board[i+1][j] = ' S' #bo
                                    temp_board[i-1][j] = ' S' #onder
                                    temp_board[i][j-1] = ' S' #links
                                else:
                                    temp_board[i+1][j] = ' S' #bo
                                    temp_board[i-1][j] = ' S' #onder
                                    temp_board[i][j-1] = ' S' #links
                                    temp_board[i][j+1] = ' S' #regs

    if temp_board[row][col] == ' N' : 
        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
        exit()#other peice
    if temp_board[row][col] == ' S' :
        stdio.writeln('ERROR: Sink cannot be next to another sink')
        exit()#other sink                                

    if type.upper() == "2":
        if row == 0:
            if col == 0:
               if temp_board[row+1][col] == ' N' : 
                    stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                    exit()#other peice
               if temp_board[row][col+1] == ' N' :
                   stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                   exit()#other peice
               if temp_board[row+1][col+1] == ' N' :
                   stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                   exit()#other peice

               if temp_board[row+1][col] == ' S' : 
                    stdio.writeln('ERROR: Sink cannot be next to another sink')
                    exit()#other sink
               if temp_board[row][col+1] == ' S' :
                   stdio.writeln('ERROR: Sink cannot be next to another sink')
                   exit()#other sink
               if temp_board[row+1][col+1] == ' S' :
                   stdio.writeln('ERROR: Sink cannot be next to another sink')
                   exit()#other sink
            else:
                if col == col_input-1:
                   valid == False
                else:
                    if temp_board[row+1][col] == ' N' : 
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice
                    if temp_board[row][col+1] == ' N' :
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice
                    if temp_board[row+1][col+1] == ' N' :
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice
                    if temp_board[row+1][col] == ' S' : 
                         stdio.writeln('ERROR: Sink cannot be next to another sink')
                         exit()#other sink
                    if temp_board[row][col+1] == ' S' :
                        stdio.writeln('ERROR: Sink cannot be next to another sink')
                        exit()#other sink
                    if temp_board[row+1][col+1] == ' S' :
                        stdio.writeln('ERROR: Sink cannot be next to another sink')
                        exit()#other sink
        else:
            if row == row_input-1:
               valid == False
            else:
                if col == 0:
                    if temp_board[row+1][col] == ' N' : 
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice
                    if temp_board[row][col+1] == ' N' :
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice
                    if temp_board[row+1][col+1] == ' N' :
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice
                    if temp_board[row+1][col] == ' S' : 
                         stdio.writeln('ERROR: Sink cannot be next to another sink')
                         exit()#other sink
                    if temp_board[row][col+1] == ' S' :
                        stdio.writeln('ERROR: Sink cannot be next to another sink')
                        exit()#other sink
                    if temp_board[row+1][col+1] == ' S' :
                        stdio.writeln('ERROR: Sink cannot be next to another sink')
                        exit()#other sink
                else:
                    if col == col_input-1:
                       valid == False
                    else:
                        if temp_board[row+1][col] == ' N' : 
                            stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                            exit()#other peice
                        if temp_board[row][col+1] == ' N' :
                            stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                            exit()#other peice
                        if temp_board[row+1][col+1] == ' N' :
                            stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                            exit()#other peice
                        if temp_board[row+1][col] == ' S' : 
                             stdio.writeln('ERROR: Sink cannot be next to another sink')
                             exit()#other sink
                        if temp_board[row][col+1] == ' S' :
                            stdio.writeln('ERROR: Sink cannot be next to another sink')
                            exit()#other sink
                        if temp_board[row+1][col+1] == ' S' :
                            stdio.writeln('ERROR: Sink cannot be next to another sink')
                            exit()#other sink

    if temp_board[row][col] == ' I':
            if type == "2" :
                if   (1 < row < row_input - 3 ) and  (1 < col < col_input - 3 ) :
                    stdio.writeln('ERROR: Sink in the wrong position')
                    exit() 
                if row == row_input-1 and col == col_input-1:
                    stdio.writeln('ERROR: Field ' + str(row) + ' ' + str(col+1) + ' not on board')
                    exit() 
                else:
                    if row == row_input-1  :
                        stdio.writeln('ERROR: Field ' + str(row+1) + ' ' + str(col) + ' not on board')
                        exit() 
                    if col == col_input-1:
                        stdio.writeln('ERROR: Field ' + str(row) + ' ' + str(col+1) + ' not on board')
                        exit() 
            else:
                if (2 < row < row_input - 3 ) and (2 < col < col_input - 3 ) :
                    stdio.writeln('ERROR: Sink in the wrong position')
                    exit()


def check_piece_range(board,row_input, col_input, row, col,type,first):
    '''
    Check if piece placement is valid

    args:
        board(2D array of str): The game board
        row_input(int): The amount of rows on the game board
        col_input(int): The amount of columns on the game board
        row(int): The value of the row being checked
        col(int): The value of the column being checked
        type(str): The type of piece being checked
        first(bool): If currently busy with the board setup the value is True else False
    '''
    valid = True
    if first:
        temp_board = stdarray.create2D(row_input,col_input," I")
        if type.upper() == 'D' :
            for i in range(3,row_input-4):
                for j in range(3,col_input-4):
                    temp_board[i][j] = '  '
        else:
            for i in range(3,row_input-3):
                for j in range(3,row_input-3):
                    if board[i][j] == '  ' :
                        temp_board[i][j] = '  '
        for i in range(row_input):
            for j in range(col_input):
                if not board[i][j] == '  ' :
                    temp_board[i][j] = ' N'
    else:
        temp_board = stdarray.create2D(row_input,col_input," I")
        if type.upper() == 'D' :
            for i in range(row_input):
                temp_board[i][col_input-1] = ' I'
            for i in range(col_input):
                temp_board[row_input-1][i] = ' I'

        for i in range(row_input):
            for j in range(col_input):
                if not board[i][j] == '  ' :
                    temp_board[i][j] = ' N'

    ###############################################                        
    #valid 2 size
    ############################
    if temp_board[row][col] == ' N' : 
        stdio.writeln('ERROR: Field ' + str(row) + ' ' + str(col) + ' not free')
        exit()#other peice               

    if type.upper() == "D":
        if row == 0:
            if col == 0:
               if temp_board[row+1][col] == ' N' : 
                    stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                    exit()#other peice
               if temp_board[row][col+1] == ' N' :
                   stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                   exit()#other peice
               if temp_board[row+1][col+1] == ' N' :
                   stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                   exit()#other peice               
            else:
                if col == col_input-1:
                   valid == False
                else:
                    if temp_board[row+1][col] == ' N' : 
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice
                    if temp_board[row][col+1] == ' N' :
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice
                    if temp_board[row+1][col+1] == ' N' :
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice  
        else:
            if row == row_input-1:
               valid == False
            else:
                if col == 0:
                    if temp_board[row+1][col] == ' N' : 
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice
                    if temp_board[row][col+1] == ' N' :
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice
                    if temp_board[row+1][col+1] == ' N' :
                        stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                        exit()#other peice                    
                else:
                    if col == col_input-1:
                       valid == False
                    else:
                        if temp_board[row+1][col] == ' N' : 
                            stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                            exit()#other peice
                        if temp_board[row][col+1] == ' N' :
                            stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                            exit()#other peice
                        if temp_board[row+1][col+1] == ' N' :
                            stdio.writeln('ERROR: ERROR: Field ' + str(row) + str(col) + ' not free')
                            exit()#other peice

    if temp_board[row][col] == ' I':
            if type == "D" :
                if (1 < row < row_input - 3 ) and (1 < col < col_input - 3 ) :
                    stdio.writeln('ERROR: Piece in the wrong position')
                    exit() 
            else:
                if  not (2 < row < row_input - 3 ) or   not (2 < col < col_input - 3 ) :
                    stdio.writeln('ERROR: Piece in the wrong position')
                    exit()


def check_piece_upright(row, col, board):
    '''
    Checks if the piece is upright or on it's side

    args:
        board(2D array of str): The game board
        row_input(int): The amount of rows on the game board
        col_input(int): The amount of columns on the game board

    returns:
        valid(bool): If the piece is upright the value is True
    '''
    piece = get_piece_fields(row,col,board)
    valid = True
    if len(piece) == 2 or len(piece) == 3 : valid = False
    return valid


def get_piece_fields(row, col, board):
    '''
    Finds the value of all the fields belonging to a piece

    args:
        row(int): the value of the row of the piece being checked
        col(int): the value of the coloumn of the piece being checked
        board(@d array of str): the game board

    returns:
        coordinates(array of str): all the fields belonging to a piece
    '''
    coordinates = []
    if 0 <= row <= row_input-1 and 0 <= col <= col_input-1:
        if board[row][col] != '  ' and board[row][col] != ' s' and board[row][col] != ' x' :
            if not board[row][col] in [' a',' b',' c',' d',' A',' B',' C',' D',]:
                value = int(board[row][col])
                row  =   value // col_input
                col = value - (row*col_input)      
            coordinates.append(str(row)+str(col))
            value = str(row* col_input + col)
            for i in range(row_input):
                for j in range(col_input):
                    if board[i][j] == value :
                        coordinates.append(str(i)+str(j)) 
    return coordinates


def error_message(errors,gui_mode):
    '''
    Displays error message
    
    args:
        errors(str): the error message to be displayed'''
    if gui_mode == 0:
        stdio.writeln(errors)
        exit()
    else:
        stddraw.setPenColor(stddraw.BOOK_RED)
        stddraw.setFontSize(24)
        
        stddraw.text(0.5,0.92,errors) 
        stddraw.setPenColor()
        stddraw.setFontSize()
        stddraw.show()


def validate_move(row, col, direction, board,last_player,sink,previous_move):
    """
    Checks whether the given move is valid by checking that all aspects of the
    move are legal.

    Args:
        row (int): The row of the object to move
        col (int): The column of the object to move
        direction (str): The direction of the move
        board (2D array of str): The game board
        last_player (str): the player whom is supposed to play this round
        sink (array of str): list of all the sink fields
        previous_move (array of str): all fields from the previous move

    Returns:
        bool: True if the move is valid, False otherwise
    """
    global move_count
    global moved_d
    global sink_move_dark
    global sink_move_light

    sunk = False
    
    piece = board[row][col]
    
    new_position = []
    
    if (piece == ' s'):
            team_check = last_player
    else:
        if piece == ' a' or piece == ' b' or piece == ' c' or piece == ' d':
            team_check = 'Light'
        else:
            team_check = 'Dark'

    #if (piece == ' s') and (move_count == 0):
    #    team_check = last_player
    #elif (piece == ' s'):
    #    if last_player == "Light" :
    #        team_check = 'Dark'
    #    else:
    #        team_check = 'Light'

    #if moved_d:
    #    if last_player == "Light" :
    #     team_check = 'Dark'
    #    else:   
    #        team_check = 'Light'


    if (last_player != team_check) :
        errors = 'ERROR: Piece does not belong to the correct player'
        error_message(errors,gui_input)
    
    last_player = team_check
    moved_d = False

    if last_player == 'Light':
        sink_move = sink_move_light
    else:
        sink_move = sink_move_dark


    if piece == ' s' :
        sink_values = find_sink_fields(row,col,board)
        if sink_move >= 2 :
            errors = 'ERROR: No sink moves left'
            error_message(errors,gui_input)
        """for i in range(len(sink_values)):
            x = int(sink_values[i]) // 10
            y = int(sink_values[i]) % 10      #kan op oomblik sink onder peice in beweeg en tel nie dan vir punte nie
            if direction == 'l' :
                if board[x][y-1] == ' s':
                    errors = 'ERROR: Sink cannot be next to another sink'
                    error_message(errors,gui_input)
            elif direction == 'r' :
                if board[x][y+1] == ' s':
                    errors = 'ERROR: Sink cannot be next to another sink'
                    error_message(errors,gui_input)
            elif direction == 'u' :
                if board[x+1][y] == ' s':
                    errors = 'ERROR: Sink cannot be next to another sink'
                    error_message(errors,gui_input)
            elif direction == 'd' :
                if board[x-1][y] == ' s':
                    errors = 'ERROR: Sink cannot be next to another sink'
                    error_message(errors,gui_input)"""
        sink_move += 1
    else:
        changed = False
        piece = piece.upper()
        
        if piece == ' A':
            if direction == "l" :                
                if ((col-1) < 0) or ((col-1) > (col_input-1)):
                    errors = 'ERROR: Cannot move beyond the board'
                    error_message(errors,gui_input)
                    changed =True
                if  not changed and not board[row][col-1] in ['  ',' s'] : 
                    errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                    error_message(errors,gui_input)
                    changed =True
               
                new_position += [str(row)+str(col-1)]
            elif direction == "r" :
                if ((col+1) < 0) or ((col+1) > (col_input-1)):
                    errors = 'ERROR: Cannot move beyond the board'
                    error_message(errors,gui_input)
                    changed =True
                if not changed and not board[row][col+1] in ['  ',' s']: 
                    errors = 'ERROR: Field ' + str(row) +' '+ str(col+1) + ' not free'
                    error_message(errors,gui_input)
                    changed =True
                
                new_position += [str(row)+str(col+1)]
            elif direction == "u" :
                if ((row+1) < 0) or ((row+1) > (row_input-1)):
                    errors = 'ERROR: Cannot move beyond the board'
                    error_message(errors,gui_input)
                    changed =True
                if not changed and not board[row+1][col] in ['  ',' s']: 
                    errors = 'ERROR: Field ' + str(row+1) +' '+ str(col) + ' not free'
                    error_message(errors,gui_input)
                    changed =True
                
                new_position += [str(row+1)+str(col)]
            elif direction == "d" :
                if ((row-1) < 0) or ((row-1) > (row_input-1)):
                    errors = 'ERROR: Cannot move beyond the board'
                    error_message(errors,gui_input)
                    changed =True
                if not changed and not board[row-1][col] in ['  ',' s']: 
                    errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                    error_message(errors,gui_input)
                    changed =True
                
                new_position += [str(row-1)+str(col)]
        elif check_piece_upright(row,col,board):
            if piece == " B" :
                if direction == "l" :
                    if ((col-1) < 0) or ((col-1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col-2) < 0) or ((col-2) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True
                    if not changed and not board[row][col-1] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                   
                    if not changed and not board[row][col-2] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col-2) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    new_position += [str(row)+str(col-1)]
                    new_position += [str(row)+str(col-2)]
                elif direction == "r" :
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if  not changed and not board[row][col+1] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col+1) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row][col+2] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col+2) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    new_position += [str(row)+str(col+1)]
                    new_position += [str(row)+str(col+2)]
                elif direction == "u" :
                    if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True
                    if not changed and not board[row+1][col] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row+1) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if  not changed and not board[row+2][col] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row+2) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    new_position += [str(row+1)+str(col)]
                    new_position += [str(row+2)+str(col)]
                elif direction == "d" :
                    if ((row-2) < 0) or ((row-2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if not changed and not board[row-2][col] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row-2) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if  not changed and not board[row-1][col] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    new_position += [str(row-2)+str(col)]
                    new_position += [str(row-1)+str(col)]
            elif piece == " C" :
                if direction == "l" :
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col-3) < 0) or ((col-3) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col-2) < 0) or ((col-2) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True     
                    if not changed and not board[row][col-3] in ['  ',' s'] :
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col-3) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row][col-2] in ['  ',' s'] :
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col-2) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                   
                    if not changed and not board[row][col-1] in ['  ',' s'] :
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    new_position += [str(row)+str(col-3)]
                    new_position += [str(row)+str(col-2)]
                    new_position += [str(row)+str(col-1)]
                elif direction == "r" :
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col +2) < 0) or ((col +2) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col+3) < 0) or ((col+3) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if not changed and not board[row][col+1] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col+1) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row][col+2] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col+2) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row][col+3] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col+3) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    new_position += [str(row)+str(col+1)]
                    new_position += [str(row)+str(col+2)]
                    new_position += [str(row)+str(col+3)]
                elif direction == "u" :
                    if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row+3) < 0) or ((row+3) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if not changed and not board[row+1][col] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row+1) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                   
                    if not changed and not board[row+2][col] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row+2) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row+3][col] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row+3) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    new_position += [str(row+1)+str(col)]
                    new_position += [str(row+2)+str(col)]
                    new_position += [str(row+3)+str(col)]
                elif direction == "d" :
                    if ((row-3) < 0) or ((row-3) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row-2) < 0) or ((row-2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if not changed and not board[row-3][col] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row-3) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                   
                    if not changed and not board[row-2][col] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row-2) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row-1][col] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                   
                    new_position += [str(row-3)+str(col)]
                    new_position += [str(row-2)+str(col)]
                    new_position += [str(row-1)+str(col)]
            else:
                if move_count == 1 :
                    errors = 'ERROR: Cannot move a 2x2x2 piece on the second move'
                    error_message(errors,gui_input)
                    changed =True
                if direction == "l" :
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col-2) < 0) or ((col-2) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col-2) < 0) or ((col-2) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if not changed and not board[row][col-2]   in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col-2) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row][col-1]   in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row+1][col-2] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row+1) +' '+ str(col-2) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row+1][col-1] in ['  ',' s']:
                        errors = 'ERROR: Field ' + str(row+1) +' '+ str(col-1) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                   
                    new_position += [str(row)+str(col-2)]
                    new_position += [str(row)+str(col-1)]
                    new_position += [str(row+1)+str(col-2)]
                    new_position += [str(row+1)+str(col-1)]
                elif direction == "r" :
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True
                    if ((row) < 0) or ((row) > (row_input-1)) or ((col+3) < 0) or ((col+3) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+3) < 0) or ((col+3) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True     
                    if not changed and not board[row][col+2]   in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col+2) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                     
                    if not changed and not board[row][col+3]   in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col+3) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row+1][col+2] in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+2) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row+1][col+3] in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+3) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    new_position += [str(row)+str(col+2)]
                    new_position += [str(row)+str(col+3)]
                    new_position += [str(row+1)+str(col+2)]
                    new_position += [str(row+1)+str(col+3)]
                elif direction == "u" :
                    if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row+3) < 0) or ((row+3) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row+3) < 0) or ((row+3) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True
                    if not changed and not board[row+2][col]   in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row+2) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    if not changed and not board[row+3][col]   in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row+3) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                   
                    if not changed and not board[row+2][col+1] in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row+2) +' '+ str(col+1) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row+3][col+1] in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row+3) +' '+ str(col+1) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                     
                    new_position += [str(row+2)+str(col)]
                    new_position += [str(row+3)+str(col)]
                    new_position += [str(row+2)+str(col+1)]
                    new_position += [str(row+3)+str(col+1)]
                elif direction == "d" :
                    if ((row-2) < 0) or ((row-2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row-2) < 0) or ((row-2) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        error_message(errors,gui_input)
                        changed =True 
                    if not changed and not board[row-2][col]   in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row-2) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                   
                    if not changed and not board[row-1][col]   in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row-2][col+1] in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row-2) +' '+ str(col+1) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    if not changed and not board[row-1][col+1] in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row-1) +' '+ str(col+1) + ' not free'
                        error_message(errors,gui_input)
                        changed =True
                    
                    new_position += [str(row-2)+str(col)]
                    new_position += [str(row-1)+str(col)]
                    new_position += [str(row-2)+str(col+1)]
                    new_position += [str(row-1)+str(col+1)]
                    moved_d = True
        else:
            if piece == " B" :
                if check_vertical(row,col,board) :
                    if direction == "l" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input)
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input)
                        if not changed and not board[row][col-1]   in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                            error_message(errors,gui_input)
                         
                        if not changed and not board[row+1][col-1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col-1) + ' not free'
                            error_message(errors,gui_input)
                         
                        new_position += [str(row)+str(col-1)]
                        new_position += [str(row+1)+str(col-1)]
                    elif direction == "r" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if not changed and not board[row][col+1]   in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+1) + ' not free'
                            error_message(errors,gui_input)
                        
                        if not changed and not board[row+1][col+1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+1) + ' not free'
                            error_message(errors,gui_input)
                        
                        new_position += [str(row)+str(col+1)]
                        new_position += [str(row+1)+str(col+1)]
                    elif direction == "u" :
                        if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if not changed and not board[row+2][col]  in ['  ',' s'] :
                            errors = 'ERROR: Field ' + str(row+2) +' '+ str(col) + ' not free'
                            error_message(errors,gui_input)
                        
                        new_position += [str(row+2)+str(col)]
                    elif direction == "d" :
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if not changed and not board[row-1][col]  in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                            error_message(errors,gui_input)
                       
                        new_position += [str(row-1)+str(col)]                        
                else:
                    if direction == "l" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input)
                        if not changed and not board[row][col-1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                            error_message(errors,gui_input)
                        
                        new_position += [str(row)+str(col-1)]
                    elif direction == "r" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if not changed and not board[row][col+2] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+2) + ' not free'
                            error_message(errors,gui_input)
                        
                        new_position += [str(row)+str(col+2)]
                    elif direction == "u" :
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if not changed and not board[row+1][col]   in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col) + ' not free'
                            error_message(errors,gui_input)
                        
                        if not changed and not board[row+1][col+1] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+1) + ' not free'
                            error_message(errors,gui_input)
                        
                        new_position += [str(row+1)+str(col)]
                        new_position += [str(row+1)+str(col+1)]
                    elif direction == "d" :
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input)
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if not changed and not board[row-1][col]   in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                            error_message(errors,gui_input)
                         
                        if not changed and not board[row-1][col+1] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col+1) + ' not free'
                            error_message(errors,gui_input)
                        
                        new_position += [str(row-1)+str(col)]
                        new_position += [str(row-1)+str(col+1)]
            elif piece == " C" :
                if check_vertical(row,col,board) :
                    if direction == "l" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if not changed and not board[row][col-1]   in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                            error_message(errors,gui_input)
                        
                        if not changed and not board[row+1][col-1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col-1) + ' not free'
                            error_message(errors,gui_input)
                        
                        if not changed and not board[row+2][col-1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+2) +' '+ str(col-1) + ' not free'
                            error_message(errors,gui_input)
                        
                        new_position += [str(row)+str(col-1)]
                        new_position += [str(row+1)+str(col-1)]
                        new_position += [str(row+2)+str(col-1)]
                    elif direction == "r" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if not changed and not board[row][col+1]   in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+1) + ' not free'
                            error_message(errors,gui_input)
                        
                        if not changed and not board[row+1][col+1] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+1) + ' not free'
                            error_message(errors,gui_input)
                        
                        if not changed and not board[row+2][col+1] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+2) +' '+ str(col+1) + ' not free'
                            error_message(errors,gui_input)
                        
                        new_position += [str(row)+str(col+1)]
                        new_position += [str(row+1)+str(col+1)]
                        new_position += [str(row+2)+str(col+1)]
                    elif direction == "u" :
                        if ((row+3) < 0) or ((row+3) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if not changed and not board[row+3][col] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+3) +' '+ str(col) + ' not free'
                            error_message(errors,gui_input)
                        
                        new_position += [str(row+3)+str(col)]
                    elif direction == "d" :
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input)
                        if not changed and not board[row-1][col] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                            error_message(errors,gui_input)
                         
                        new_position += [str(row-1)+str(col)]
                else:
                    if direction == "l" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input)
                        if not changed and not board[row][col-1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                            error_message(errors,gui_input)
                       
                        new_position += [str(row)+str(col-1)] 
                    elif direction == "r" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col+3) < 0) or ((col+3) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if not changed and not board[row][col+3] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+3) + ' not free'
                            error_message(errors,gui_input)
                        
                        new_position += [str(row)+str(col+3)]
                    elif direction == "u" :
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input)
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input)
                        
                        if not changed and not board[row+1][col]   in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col) + ' not free'
                            error_message(errors,gui_input)
                        
                        if not changed and not board[row+1][col+1] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+1) + ' not free'
                            error_message(errors,gui_input)
                         
                        if not changed and not board[row+1][col+2] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+2) + ' not free'
                            error_message(errors,gui_input)
                         
                        new_position += [str(row+1)+str(col)]
                        new_position += [str(row+1)+str(col+1)]
                        new_position += [str(row+1)+str(col+2)]
                    elif direction == "d" :
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input) 
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            error_message(errors,gui_input)
                        if not changed and not board[row-1][col]   in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                            error_message(errors,gui_input)
                        
                        if not changed and not board[row-1][col+1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col+1) + ' not free'
                            error_message(errors,gui_input)
                        
                        if not changed and not board[row-1][col+2] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col+2) + ' not free'
                            error_message(errors,gui_input)
                         
                        new_position += [str(row-1)+str(col)]
                        new_position += [str(row-1)+str(col+1)]
                        new_position += [str(row-1)+str(col+2)]

    found = 0
    sink_checked = False
    for i in range(len(new_position)):
        if new_position[i] in previous_move:
            found += 1
        if new_position[i] in sink:
            sink_checked = True


    if sink_checked:
        valid = True
        for i in range(len(new_position)):
            test = new_position[i]
            x = int(test[0])
            y = int(test[1])
            if board[x][y] != ' s':
                valid = False
            elif not valid:
                errors = 'ERROR: Field ' + str(x) +' '+ str(y) + ' not free'
                error_message(errors,gui_input)

           

    



    if found == len(previous_move) and found != 0 :
        errors = 'ERROR: Piece cannot be returned to starting position'
        error_message(errors,gui_input)

    

    move_count = move_count + 1
    if last_player == "Light":
        sink_move_light = sink_move
    else:
        sink_move_dark = sink_move


def find_sink(board):
    '''
    Finds all the sink fields on the game board

    args:
        board(2D array of str) : the game board

    returns:
        a(array of string): all the fields containing a sink
    '''
    a = []
    for i in range(row_input):
        for j in range(col_input):
            if board[i][j] == " s" :
                a += [str(i)+str(j)]
    return a


def check_vertical(row, col, board):
    '''
    Check if the piece is vertical

    args:  
        row(int): the value of the row of the piece
        col(int): the value of the column of the piece
        broad(2D array of str): the game board

    returns:
        if vertical True else false
    '''
    piece_fields = get_piece_fields(row,col,board)
    value1 = piece_fields[0]
    value2 = piece_fields[1]
    if value1[0] == value2[0] :
        return  False
    else:
        return  True


def do_move(row, col, direction, board, scores, gui_mode,sink):
    '''
    executes the move by moving the pieces on the game board

    args:
        row (int): the row of the piece being moved
        col (int): the col of the piece being moved
        direction (string): the direction for the piece to be moved in
        board (2D array of string): the game board
        scores (array of int): the current score of the game
        gui_mode (bool): if true the program is to be run in gui mode
        sink (array of str):  all the fields of all the sinks on the board  
    
    '''
    global moved_d
    global bombs
    sunk = False
    score = 0
    piece = board[row][col]
    if piece == ' s' :
        sink_values = find_sink_fields(row,col,board)
        for i in range(len(sink_values)):
            x = int(sink_values[i]) // 10
            y = int(sink_values[i]) % 10      #kan op oomblik sink onder peice in beweeg en tel nie dan vir punte nie
            if direction == 'l' :
                board[x][y-1] = board[x][y]
            elif direction == 'r' :
                board[x][y+1] = board[x][y]
            elif direction == 'u' :
                board[x+1][y] = board[x][y]
            elif direction == 'd' :
                board[x-1][y] = board[x][y]
            board[x][y] = '  '
        
    else:
        if piece == ' a' or piece == ' b' or piece == ' c' or piece == ' d':
            team = 'Light'
        else:
            team = 'Dark'
        piece = piece.upper()
        if piece == ' A':
            if direction == "l" :
                piece = board[row][col]
                new_spot = board[row][col-1]
                if not new_spot == " s" :
                    board[row][col-1] = board[row][col]
                else:
                    sunk = True
                    board[row][col-1] = " s"
                origin_x = row
                origin_y = col-1
            elif direction == "r" :
                piece = board[row][col]
                new_spot = board[row][col+1]
                if not new_spot == " s" :
                    board[row][col+1] = board[row][col]
                else:
                    sunk = True
                    board[row][col+1] = " s"
                origin_x = row
                origin_y = col+1
            elif direction == "u" :
                piece = board[row][col]
                new_spot = board[row+1][col]
                if not new_spot == " s" :
                    board[row+1][col] = board[row][col]
                else:
                    sunk = True
                    board[row+1][col] = " s"
                origin_x = row+1
                origin_y = col
            elif direction == "d" :
                piece = board[row][col]
                new_spot = board[row-1][col]
                if not new_spot == " s" :
                    board[row-1][col] = board[row][col] 
                else:
                    sunk = True
                    board[row-1][col] = " s"
                origin_x = row-1
                origin_y = col
            board[row][col] = '  '
            
        elif check_piece_upright(row,col,board):
            if piece == " B" :
                if direction == "l" :
                    board[row][col-2] = board[row][col]
                    origin_x = row
                    origin_y = col-2
                    board[row][col-1] = str(row*col_input + (col-2))
                elif direction == "r" :
                    board[row][col+2] = str(row*col_input + (col+1))
                    board[row][col+1] = board[row][col]
                    origin_x = row
                    origin_y = col+1
                elif direction == "u" :
                    board[row+2][col] = str((row+1)*col_input + (col))
                    board[row+1][col] = board[row][col]
                    origin_x = row+1
                    origin_y = col
                elif direction == "d" :
                    board[row-2][col] = board[row][col]
                    board[row-1][col] = str((row-2)*col_input + (col))
                    origin_x = row-2
                    origin_y = col
                board[row][col] = '  '
            elif piece == " C" :
                if direction == "l" :
                    board[row][col-3] = board[row][col]
                    board[row][col-2] =  str(row*col_input + (col-3))
                    board[row][col-1] =  str(row*col_input + (col-3))
                    origin_x = row
                    origin_y = col-3
                elif direction == "r" :
                    board[row][col+3] =  str(row*col_input + (col+1))
                    board[row][col+2] =  str(row*col_input + (col+1))
                    board[row][col+1] = board[row][col]
                    origin_x = row
                    origin_y = col+1
                elif direction == "u" :
                    board[row+3][col] =  str((row+1)*col_input + (col))
                    board[row+2][col] =  str((row+1)*col_input + (col))
                    board[row+1][col] = board[row][col]
                    origin_x = row+1
                    origin_y = col
                elif direction == "d" :
                    board[row-3][col] = board[row][col]
                    board[row-2][col] =  str((row-3)*col_input + (col))
                    board[row-1][col] =  str((row-3)*col_input + (col))
                    origin_x = row-3
                    origin_y = col
                board[row][col] = '  '
            else:
                if direction == "l" :
                    board[row][col-2] = board[row][col]
                    board[row][col-1] =  str(row*col_input + (col-2))
                    board[row+1][col-2] =  str(row*col_input + (col-2))
                    board[row+1][col-1] =  str(row*col_input + (col-2))
                    origin_x = row
                    origin_y = col-2
                elif direction == "r" :
                    board[row][col+2] = board[row][col]
                    board[row][col+3] =  str(row*col_input + (col+2))
                    board[row+1][col+2] =  str(row*col_input + (col+2))
                    board[row+1][col+3] =  str(row*col_input + (col+2))
                    origin_x = row
                    origin_y = col+2
                elif direction == "u" :
                    board[row+3][col] = str((row+2)*col_input + (col))
                    board[row+2][col] =   board[row][col]
                    board[row+3][col+1] =  str((row+2)*col_input + (col))
                    board[row+2][col+1] =  str((row+2)*col_input + (col))
                    origin_x = row+3
                    origin_y = col
                elif direction == "d" :
                    board[row-2][col] = board[row][col]
                    board[row-1][col] =  str((row-2)*col_input + (col))
                    board[row-2][col+1] =  str((row-2)*col_input + (col))
                    board[row-1][col+1] =   str((row-2)*col_input + (col))
                    origin_x = row-2
                    origin_y = col
                board[row][col] = '  '
                board[row+1][col+1] = '  '
                board[row+1][col] = '  '
                board[row][col+1] = '  '
                moved_d = True
        else:
            if piece == " B" :
                if check_vertical(row,col,board) :
                    if direction == "l" :
                        board[row][col-1] = board[row][col]
                        board[row+1][col-1] = str((row) * col_input + (col-1))
                        origin_x = row
                        origin_y = col-1
                    elif direction == "r" :
                        board[row][col+1] = board[row][col]
                        board[row+1][col+1] = str((row) * col_input + (col+1))
                        origin_x = row
                        origin_y = col+1
                    elif direction == "u" :
                        board[row+2][col] = board[row][col]
                        origin_x = row+2
                        origin_y = col
                    elif direction == "d" :
                        board[row-1][col] = board[row][col]
                        origin_x = row-1
                        origin_y = col
                    board[row][col] = '  '
                    board[row+1][col] = '  '
                else:
                    if direction == "l" :
                        board[row][col-1] = board[row][col]
                        origin_x = row
                        origin_y = col-1
                    elif direction == "r" :
                        board[row][col+2] = board[row][col]
                        origin_x = row
                        origin_y = col+2
                    elif direction == "u" :
                        board[row+1][col] = board[row][col]
                        board[row+1][col+1] = str((row+1) * col_input + (col))     
                        origin_x = row+1
                        origin_y = col               
                    elif direction == "d" :
                        board[row-1][col] = board[row][col]
                        board[row-1][col+1] = str((row-1) * col_input + (col))
                        origin_x = row-1
                        origin_y = col
                    board[row][col] = '  '
                    board[row][col+1] = '  '
            elif piece == " C" :
                if check_vertical(row,col,board) :
                    if direction == "l" :
                        board[row][col-1] = board[row][col]
                        board[row+1][col-1] = str((row) * col_input + (col-1))
                        board[row+2][col-1] = str((row) * col_input + (col-1))
                        origin_x = row
                        origin_y = col-1
                    elif direction == "r" :
                        board[row][col+1] = board[row][col]
                        board[row+1][col+1] = str((row) * col_input + (col+1))
                        board[row+2][col+1] = str((row) * col_input + (col+1))
                        origin_x = row
                        origin_y = col+1
                    elif direction == "u" :
                        board[row+3][col] = board[row][col]
                        origin_x = row+3
                        origin_y = col
                    elif direction == "d" :
                        board[row-1][col] = board[row][col]
                        origin_x = row-1
                        origin_y = col
                    board[row][col] = '  '
                    board[row+1][col] = '  '
                    board[row+2][col] = '  '
                else:
                    if direction == "l" :
                        board[row][col-1] = board[row][col]
                        origin_x = row
                        origin_y = col-1
                    elif direction == "r" :
                        board[row][col+3] = board[row][col]
                        origin_x = row
                        origin_y = col+3
                    elif direction == "u" :
                        board[row+1][col] = board[row][col]
                        board[row+1][col+1] = str((row+1) * col_input + (col)) 
                        board[row+1][col+2] = str((row+1) * col_input + (col))       
                        origin_x = row+1
                        origin_y = col                
                    elif direction == "d" :
                        board[row-1][col] = board[row][col]
                        board[row-1][col+1] = str((row-1) * col_input + (col))
                        board[row-1][col+2] = str((row-1) * col_input + (col))    
                        origin_x = row-1
                        origin_y = col
                    board[row][col] = '  '
                    board[row][col+1] = '  '
                    board[row][col+2] = '  '

        if len(sink) != 0:
            sunk_counter = 0
            fields = get_piece_fields(origin_x,origin_y,board)
            for i in range(len(fields)):
                if (fields[i]) in sink :
                    sunk_counter += 1
                    if sunk_counter == 1:
                        bfirst = True
                        temp = fields[i]
                        tempx = (temp[0])
                        tempy = (temp[1])      
            if sunk_counter != len(fields) and sunk_counter > 0:
                erros = 'ERROR: Field '+ tempx + ' ' +  tempy +' not free'
                error_message(erros,gui_input)
            else:
                if sunk_counter == len(fields):
                    sunk = True

        


        if sunk :
            piece = piece.upper()
            for i in range(len(sink)):
                x = int(sink[i]) // 10
                y = int(sink[i]) % 10
                board[x][y] = ' s'
            if piece == ' A': 
                score = 1
            elif piece== ' B': 
                score = 2
            elif piece == ' C': 
                score = 3
            elif piece == ' D': 
                score = 4

            if team == "Light" :
                scores[0] += score
            else:
                scores[1] += score   
        else:
            bomb_check = get_piece_fields(origin_x,origin_y,board)
            bombed = False
            for i in range(len(bomb_check)):
                temp = bomb_check[i]
                row = int(temp[0])
                col = int(temp[1])
                if bombs[row][col]:
                    bombed = True
                    bombs[row][col] = False
            if bombed:
                for i in range(len(bomb_check)):
                    temp = bomb_check[i]
                    row = int(temp[0])
                    col = int(temp[1])
                    board[row][col] = '  '


def generate_all_moves(board):
    """
    Generates a list of all moves (valid or invalid) that could potentially be
    played on the current board.

    Args:
        board (2D array of str): The game board

    Returns:
        array of moves: The moves that could be played on the given board
    """

    possible_moves = []
    temp = []
    for i in range(row_input):
        for j in range(col_input):
            if board[i][j] in [' a',' b',' c',' d',' A',' B',' C',' D'] :
                possible_moves += [str(i) + str(j) + 'u']
                possible_moves += [str(i) + str(j) + 'd']
                possible_moves += [str(i) + str(j) + 'r']
                possible_moves += [str(i) + str(j) + 'l']
            if board[i][j] == ' s':
               values = find_sink_fields(i,j,board)
               values.sort()
               bottom_left = min(values)
               if not (bottom_left + 'u') in possible_moves:
                possible_moves += [bottom_left + 'u']
                possible_moves += [bottom_left + 'd']
                possible_moves += [bottom_left + 'r']
                possible_moves += [bottom_left + 'l'] 

    return possible_moves


def read_board(row_input, col_input):
    """
    This function reads in the board from stdin and constructs the board,
    returning this board when it is done.

    args:
        row_input(int): the amount of rows on the board
        col_input(int): the amount of columns on the board
    """   
    arrBoard = stdarray.create2D(row_input,col_input,"  ")
    bEnd = False
    while (not bEnd) and not (stdio.isEmpty()):
        input = []
        icount = 0
        input.append(stdio.readString())           

        if input[0] == '#' : 
             bEnd = True
        else :
            if input[0] == "s" : 
                input.append(stdio.readString())
                input.append(stdio.readString())
                input.append(stdio.readString())
                validate_setup_file(input[0],input[1],input[2],input[3])
                type = input[1]
                row = int(input[2])
                col = int(input[3])
                check_sink_range(arrBoard,row_input, col_input, row, col, type)
                plot_piece(arrBoard,row,col,type,'')

            else:
                if input[0] == "x" : 
                    input.append(stdio.readString())
                    input.append(stdio.readString())
                    validate_setup_file(input[0],'',input[1],input[2])
                    type = input[1]
                    row = int(input[1])
                    col = int(input[2])
                    plot_piece(arrBoard,row,col,type,'')
                else:
                    if input[0] == "d" : 
                        input.append(stdio.readString())
                        input.append(stdio.readString())
                        input.append(stdio.readString())
                        validate_setup_file(input[0],input[1],input[2],input[3])
                        type = input[1]
                        row = int(input[2])
                        col = int(input[3])
                        check_piece_range(arrBoard,row_input, col_input, row, col,type,True)
                        plot_piece(arrBoard,row,col,type,input[0])
                    else:
                        if input[0] == "l" :
                            input.append(stdio.readString())
                            input.append(stdio.readString())
                            input.append(stdio.readString()) 
                            validate_setup_file(input[0],input[1],input[2],input[3])
                            type = input[1]
                            row = int(input[2])
                            col = int(input[3])
                            check_piece_range(arrBoard,row_input, col_input, row, col,type,True)
                            plot_piece(arrBoard,row,col,type,input[0])
                        else:
                            validate_setup_file(input[0],'','','')
                        
    return arrBoard


def print_board(board):
   '''
   displays the game board in its current state
   
   args:
       board(2D array of str): the game board '''
   col_index = '   '
   line = '  +'
   for i in range(col_input):
       line += '--+'
       col_index += str(i) + '  '
   stdio.writeln(col_index)    
   stdio.writeln(line)
   for i in range(row_input-1,-1,-1):
        temp = str(i) + ' |'
        for j in range(col_input):
            if len(board[i][j]) == 1 :
                temp += ' ' + board[i][j] + '|'
            else:
                temp += board[i][j] + '|'
        stdio.writeln(temp)
        stdio.writeln(line)
   #stdio.writeln('')


def draw_game(board):
    """
    Draws the given board using standard draw.

    Args:
        board (2D array of str): The game board
    """
    left_side = 0.1
    right_side = 0.9
    top_side = 0.9
    bottom_side = 0.1
    interval_spacings = 0.8 / row_input
    block_size = [0.8 / row_input,0.8 / col_input]


    #blocks
    counter_y = 0.1
    for i in range(row_input):
        counter_x = 0.1
        for j in range(col_input):
            if board[i][j] != '  ':
                temp = (get_piece_fields(i,j,board))
                actual_value = ''
                if temp != []:
                    temp = temp[0]
                    actual_value = board[int(temp[0])][int(temp[1])]
                    if   actual_value.upper() == ' A': stddraw.setPenColor(stddraw.color.BOOK_LIGHT_BLUE)
                    elif actual_value.upper() == ' B': stddraw.setPenColor(stddraw.color.GRAY)
                    elif actual_value.upper() == ' C': stddraw.setPenColor(stddraw.color.DARK_GRAY)
                    else: stddraw.setPenColor(stddraw.color.LIGHT_GRAY)
                else:
                    if board[i][j] == ' s': stddraw.setPenColor(stddraw._DEFAULT_PEN_COLOR)
                    elif board[i][j] == ' x': stddraw.setPenColor(stddraw.BOOK_RED)

                stddraw.filledRectangle(counter_x  ,counter_y  ,block_size[0]  ,block_size[1])
            counter_x += block_size[0]
        counter_y += block_size[1]

    #lines
    stddraw.line(left_side,bottom_side,left_side,top_side)
    stddraw.line(right_side,bottom_side,left_side,bottom_side)

    counter = 0
    interval_spacings = block_size[0]
    for i in range(row_input):
        counter += interval_spacings
        stddraw.line(left_side + counter,bottom_side,left_side + counter,top_side)
        stddraw.text(left_side - 0.05 ,bottom_side + (counter - (block_size[1] * 0.5)),str(i))
        stddraw.text(right_side + 0.05 ,bottom_side + (counter - (block_size[1] * 0.5)),str(i))


    counter = 0
    interval_spacings = block_size[1]
    for i in range(col_input):
        counter += interval_spacings
        stddraw.line(right_side,bottom_side + counter,left_side,bottom_side + counter)
        stddraw.text(left_side + (counter - (block_size[0] * 0.5)),top_side + 0.05,str(i))
        stddraw.text(left_side + (counter - (block_size[0] * 0.5)),bottom_side - 0.05,str(i))


    #names
    checked = []
    counter_y = 0.1
    for i in range(row_input):
        counter_x = 0.1
        for j in range(col_input):
            if board[i][j] != '  ':
                stddraw.setPenColor(stddraw._DEFAULT_PEN_COLOR)
                temp = (get_piece_fields(i,j,board))
                actual_value = ''
                if temp != []:
                    first = True
                    for k in range(len(temp)):
                        if not temp[k] in checked:
                            if first:
                                first = False
                                check = min(temp)
                                actual_value = board[int(check[0])][int(check[1])]
                                if actual_value.upper() == ' A':     
                                    stddraw.text(counter_x + (block_size[0] * 0.5),counter_y + (block_size[1] * 0.5),actual_value)
                                
                                elif actual_value.upper() == ' B': 
                                    stddraw.setPenColor(stddraw.color.GRAY)
                                    if check_piece_upright(i,j,board): 
                                        stddraw.setPenColor(stddraw._DEFAULT_PEN_COLOR)  
                                        stddraw.text(counter_x + (block_size[0] * 0.5),counter_y + (block_size[1] * 0.5),actual_value)
                                    else:
                                        if check_vertical(i,j,board):
                                            stddraw.filledRectangle(counter_x  ,counter_y  ,block_size[0]  ,block_size[1]*2 - 0.002 )
                                            stddraw.setPenColor(stddraw._DEFAULT_PEN_COLOR)
                                            stddraw.text(counter_x + (block_size[0] * 0.5),counter_y + (block_size[1]),actual_value)
                                        else:
                                            stddraw.filledRectangle(counter_x  ,counter_y  ,block_size[0]*2  ,block_size[1] - 0.002 )
                                            stddraw.setPenColor(stddraw._DEFAULT_PEN_COLOR)
                                            stddraw.text(counter_x + (block_size[0]),counter_y + (block_size[1] * 0.5),actual_value)

                                elif actual_value.upper() == ' C': 
                                    stddraw.setPenColor(stddraw.color.DARK_GRAY)
                                    if check_piece_upright(i,j,board):    
                                        stddraw.setPenColor(stddraw._DEFAULT_PEN_COLOR)
                                        stddraw.text(counter_x + (block_size[0] * 0.5),counter_y + (block_size[1] * 0.5),actual_value)
                                    else:
                                        if check_vertical(i,j,board):
                                            stddraw.filledRectangle(counter_x  ,counter_y -0.001 ,block_size[0]  ,block_size[1]*3)
                                            stddraw.setPenColor(stddraw._DEFAULT_PEN_COLOR)
                                            stddraw.text(counter_x + (block_size[0] * 0.5),counter_y +  block_size[1] +(block_size[1] * 0.5),actual_value)
                                        else:
                                            stddraw.filledRectangle(counter_x  ,counter_y  ,block_size[0]*3  ,block_size[1] - 0.002 )
                                            stddraw.setPenColor(stddraw._DEFAULT_PEN_COLOR)
                                            stddraw.text(counter_x + block_size[0] + (block_size[0] * 0.5),counter_y +(block_size[1] * 0.5),actual_value)

                                else: 
                                    stddraw.setPenColor(stddraw.color.LIGHT_GRAY)
                                    stddraw.filledRectangle(counter_x + 0.003 ,counter_y  ,block_size[0]*2  - 0.005,block_size[1]*2 - 0.002 )
                                    stddraw.setPenColor(stddraw._DEFAULT_PEN_COLOR)
                                    stddraw.text(counter_x + (block_size[0]),counter_y + (block_size[1]),actual_value)

                            checked += [temp[k]]
            counter_x += block_size[0]
        counter_y += block_size[1]
    # When implemented correctly, this function can be called after each move to
    # re-draw the game for the GUI.
    # remove the following line when you add something to this function:


def validate_setup_file(piece, type, row, col):
    '''
    validates wheather the setup file provided is legal
    
    args:   
        piece(str): the type of piece being placed
        type(str): the size of the piece being placed
        row(str): the row where the piece will be placed
        col(str): the column where the piece will be placed'''
    
    if not piece in ['s','l','d','x']:
        errors = 'ERROR: Invalid object type '+ piece + ''
        error_message(errors,gui_input)
    if piece != 'x':
        if piece == 's' :
            if not type in ['1','2']:
                errors = 'ERROR: Invalid piece type '+ type + ''
                error_message(errors,gui_input)
        else:
            if not type in ['a','b','c','d']:
                errors = 'ERROR: Invalid piece type '+ type + ''
                error_message(errors,gui_input)

    try:
        int(row)
    except ValueError:
        errors = 'ERROR: Field '+ row + ' ' + col +' not on board'
        error_message(errors,gui_input)
    try:
        int(col)
    except ValueError:
        errors = 'ERROR: Field '+ row + ' ' + col +' not on board'
        error_message(errors,gui_input)

    if (int(row) < 0) or (int(row) > (row_input-1)) or (int(col) < 0) or (int(col) > (col_input-1)):
        errors = 'ERROR: Field '+ str(row)+' ' +str(col) + ' not on board'
        error_message(errors,gui_input)
    
    
def validate_move_file(row,col,move):
    '''
    validates wheather the setup file provided is legal
    
    args:   
        move(str): the direction in which the piece wil be moved
        row(str): the row where the piece will be moved
        col(str): the column where the piece will be moved'''
    

    if ((row) < 0) or ((row) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
        errors = 'ERROR: Field '+ str(row)+' ' +str(col) + ' not on board'
        error_message(errors,gui_input)

    if board[row][col] == '  ':
        errors = 'ERROR: No piece on field '+ str(row)+' ' +str(col) +''
        error_message(errors,gui_input)

    if not move in ['l','r','u','d']:
        errors = 'ERROR: Invalid direction '+ move + ''
        error_message(errors,gui_input)


def check_legal_moves(board,team,move_count):
    '''
    Checks if a legal move is avalible
    
    args:
        board(2D array of str): the game board
        team(str): the team which is supposed to play
        move_count(int): the amount of moves made in a row'''
    
    itterator = 0
    moves_list = generate_all_moves(board)
    lengte = len(moves_list)
    new_position = []
    while itterator < lengte :
        temp = moves_list[itterator]
        row = int(temp[0])
        col = int(temp[1])
        direction = temp[2]
        piece = board[row][col]
        if piece in [' a',' b',' c',' d']:
            check_team = "Light"
        else:
            check_team = "Dark"
        if team == check_team:
            changed = False
            piece = piece.upper()
            
            if piece == ' A':
                if direction == "l" :                
                    if ((col-1) < 0) or ((col-1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        moves_list[itterator] = ' '
                        changed =True
                    if  not changed and not board[row][col-1] in ['  ',' s'] : 
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                        moves_list[itterator] = ' '
                        changed =True
                   
                    new_position += [str(row)+str(col-1)]
                elif direction == "r" :
                    if ((col+1) < 0) or ((col+1) > (col_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        moves_list[itterator] = ' '
                        changed =True
                    if not changed and not board[row][col+1] in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row) +' '+ str(col+1) + ' not free'
                        moves_list[itterator] = ' '
                        changed =True
                    
                    new_position += [str(row)+str(col+1)]
                elif direction == "u" :
                    if ((row+1) < 0) or ((row+1) > (row_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        moves_list[itterator] = ' '
                        changed =True
                    if not changed and not board[row+1][col] in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row+1) +' '+ str(col) + ' not free'
                        moves_list[itterator] = ' '
                        changed =True
                    
                    new_position += [str(row+1)+str(col)]
                elif direction == "d" :
                    if ((row-1) < 0) or ((row-1) > (row_input-1)):
                        errors = 'ERROR: Cannot move beyond the board'
                        moves_list[itterator] = ' '
                        changed =True
                    if not changed and not board[row-1][col] in ['  ',' s']: 
                        errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                        moves_list[itterator] = ' '
                        changed =True
                    
                    new_position += [str(row-1)+str(col)]
            elif check_piece_upright(row,col,board):
                if piece == " B" :
                    if direction == "l" :
                        if ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col-2) < 0) or ((col-2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True
                        if not changed and not board[row][col-1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                       
                        if not changed and not board[row][col-2] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-2) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        new_position += [str(row)+str(col-1)]
                        new_position += [str(row)+str(col-2)]
                    elif direction == "r" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if  not changed and not board[row][col+1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+1) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row][col+2] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+2) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        new_position += [str(row)+str(col+1)]
                        new_position += [str(row)+str(col+2)]
                    elif direction == "u" :
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True
                        if not changed and not board[row+1][col] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if  not changed and not board[row+2][col] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+2) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        new_position += [str(row+1)+str(col)]
                        new_position += [str(row+2)+str(col)]
                    elif direction == "d" :
                        if ((row-2) < 0) or ((row-2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if not changed and not board[row-2][col] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row-2) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if  not changed and not board[row-1][col] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        new_position += [str(row-2)+str(col)]
                        new_position += [str(row-1)+str(col)]
                elif piece == " C" :
                    if direction == "l" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col-3) < 0) or ((col-3) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col-2) < 0) or ((col-2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True     
                        if not changed and not board[row][col-3] in ['  ',' s'] :
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-3) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row][col-2] in ['  ',' s'] :
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-2) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                       
                        if not changed and not board[row][col-1] in ['  ',' s'] :
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        new_position += [str(row)+str(col-3)]
                        new_position += [str(row)+str(col-2)]
                        new_position += [str(row)+str(col-1)]
                    elif direction == "r" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col +2) < 0) or ((col +2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col+3) < 0) or ((col+3) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 

                        if not changed and not board[row][col+1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+1) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row][col+2] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+2) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row][col+3] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+3) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        new_position += [str(row)+str(col+1)]
                        new_position += [str(row)+str(col+2)]
                        new_position += [str(row)+str(col+3)]
                    elif direction == "u" :
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row+3) < 0) or ((row+3) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 

                        if not changed and not board[row+1][col] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                       
                        if not changed and not board[row+2][col] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+2) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row+3][col] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+3) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        new_position += [str(row+1)+str(col)]
                        new_position += [str(row+2)+str(col)]
                        new_position += [str(row+3)+str(col)]
                    elif direction == "d" :
                        if ((row-3) < 0) or ((row-3) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row-2) < 0) or ((row-2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if not changed and not board[row-3][col] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row-3) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                       
                        if not changed and not board[row-2][col] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row-2) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row-1][col] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                       
                        new_position += [str(row-3)+str(col)]
                        new_position += [str(row-2)+str(col)]
                        new_position += [str(row-1)+str(col)]
                else:
                    if move_count == 1 :
                        errors = 'ERROR: Cannot move a 2x2x2 piece on the second move'
                        moves_list[itterator] = ' '
                        changed =True
                    if direction == "l" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col-2) < 0) or ((col-2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col-2) < 0) or ((col-2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if not changed and not board[row][col-2]   in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-2) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row][col-1]   in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row+1][col-2] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col-2) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row+1][col-1] in ['  ',' s']:
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col-1) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                       
                        new_position += [str(row)+str(col-2)]
                        new_position += [str(row)+str(col-1)]
                        new_position += [str(row+1)+str(col-2)]
                        new_position += [str(row+1)+str(col-1)]
                    elif direction == "r" :
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True
                        if ((row) < 0) or ((row) > (row_input-1)) or ((col+3) < 0) or ((col+3) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+3) < 0) or ((col+3) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True     
                        if not changed and not board[row][col+2]   in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+2) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                         
                        if not changed and not board[row][col+3]   in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row) +' '+ str(col+3) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row+1][col+2] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+2) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row+1][col+3] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+3) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        new_position += [str(row)+str(col+2)]
                        new_position += [str(row)+str(col+3)]
                        new_position += [str(row+1)+str(col+2)]
                        new_position += [str(row+1)+str(col+3)]
                    elif direction == "u" :


                        if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 

                        if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 

                        if ((row+3) < 0) or ((row+3) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row+3) < 0) or ((row+3) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True
                        if not changed and not board[row+2][col]   in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+2) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True

                        if not changed and not board[row+3][col]   in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+3) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                       
                        if not changed and not board[row+2][col+1] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+2) +' '+ str(col+1) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True

                        

                        if not changed and not board[row+3][col+1] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row+3) +' '+ str(col+1) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True

                         
                        new_position += [str(row+2)+str(col)]
                        new_position += [str(row+3)+str(col)]
                        new_position += [str(row+2)+str(col+1)]
                        new_position += [str(row+3)+str(col+1)]
                    elif direction == "d" :
                        if ((row-2) < 0) or ((row-2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row-2) < 0) or ((row-2) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 
                        if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                            errors = 'ERROR: Cannot move beyond the board'
                            moves_list[itterator] = ' '
                            changed =True 

                        if not changed and not board[row-2][col]   in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row-2) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                       
                        if not changed and not board[row-1][col]   in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row-2][col+1] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row-2) +' '+ str(col+1) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        if not changed and not board[row-1][col+1] in ['  ',' s']: 
                            errors = 'ERROR: Field ' + str(row-1) +' '+ str(col+1) + ' not free'
                            moves_list[itterator] = ' '
                            changed =True
                        
                        new_position += [str(row-2)+str(col)]
                        new_position += [str(row-1)+str(col)]
                        new_position += [str(row-2)+str(col+1)]
                        new_position += [str(row-1)+str(col+1)]
                        moved_d = True

            else:
                if piece == " B" :
                    if check_vertical(row,col,board) :
                        if direction == "l" :
                            if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True
                            if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True

                            if not changed and not board[row][col-1]   in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                             
                            if not changed and not board[row+1][col-1] in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row+1) +' '+ str(col-1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                             
                            new_position += [str(row)+str(col-1)]
                            new_position += [str(row+1)+str(col-1)]
                        elif direction == "r" :
                            if ((row) < 0) or ((row) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 
                            if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 

                            if not changed and not board[row][col+1]   in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row) +' '+ str(col+1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            if not changed and not board[row+1][col+1] in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            new_position += [str(row)+str(col+1)]
                            new_position += [str(row+1)+str(col+1)]
                        elif direction == "u" :
                            if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 

                            if not changed and not board[row+2][col]  in ['  ',' s'] :
                                errors = 'ERROR: Field ' + str(row+2) +' '+ str(col) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            new_position += [str(row+2)+str(col)]
                        elif direction == "d" :
                            if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 

                            if not changed and not board[row-1][col]  in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                           
                            new_position += [str(row-1)+str(col)]                        
                    else:
                        if direction == "l" :
                            if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True

                            if not changed and not board[row][col-1] in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            new_position += [str(row)+str(col-1)]
                        elif direction == "r" :
                            if ((row) < 0) or ((row) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 

                            if not changed and not board[row][col+2] in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row) +' '+ str(col+2) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            new_position += [str(row)+str(col+2)]
                        elif direction == "u" :
                            if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 
                            if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 

                            if not changed and not board[row+1][col]   in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row+1) +' '+ str(col) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            if not changed and not board[row+1][col+1] in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            new_position += [str(row+1)+str(col)]
                            new_position += [str(row+1)+str(col+1)]
                        elif direction == "d" :
                            if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True
                            if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 

                            if not changed and not board[row-1][col]   in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                             
                            if not changed and not board[row-1][col+1] in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row-1) +' '+ str(col+1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            new_position += [str(row-1)+str(col)]
                            new_position += [str(row-1)+str(col+1)]
                elif piece == " C" :
                    if check_vertical(row,col,board) :
                        if direction == "l" :
                            if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 
                            if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 
                            if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 

                            if not changed and not board[row][col-1]   in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            if not changed and not board[row+1][col-1] in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row+1) +' '+ str(col-1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            if not changed and not board[row+2][col-1] in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row+2) +' '+ str(col-1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            new_position += [str(row)+str(col-1)]
                            new_position += [str(row+1)+str(col-1)]
                            new_position += [str(row+2)+str(col-1)]
                        elif direction == "r" :
                            if ((row) < 0) or ((row) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 
                            if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 
                            if ((row+2) < 0) or ((row+2) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 

                            if not changed and not board[row][col+1]   in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row) +' '+ str(col+1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            if not changed and not board[row+1][col+1] in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            if not changed and not board[row+2][col+1] in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row+2) +' '+ str(col+1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            new_position += [str(row)+str(col+1)]
                            new_position += [str(row+1)+str(col+1)]
                            new_position += [str(row+2)+str(col+1)]
                        elif direction == "u" :
                            if ((row+3) < 0) or ((row+3) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 

                            if not changed and not board[row+3][col] in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row+3) +' '+ str(col) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            new_position += [str(row+3)+str(col)]
                        elif direction == "d" :
                            if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True

                            if not changed and not board[row-1][col] in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                             
                            new_position += [str(row-1)+str(col)]
                    else:
                        if direction == "l" :
                            if ((row) < 0) or ((row) > (row_input-1)) or ((col-1) < 0) or ((col-1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True

                            if not changed and not board[row][col-1] in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row) +' '+ str(col-1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                           
                            new_position += [str(row)+str(col-1)] 
                        elif direction == "r" :
                            if ((row) < 0) or ((row) > (row_input-1)) or ((col+3) < 0) or ((col+3) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 

                            if not changed and not board[row][col+3] in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row) +' '+ str(col+3) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            new_position += [str(row)+str(col+3)]
                        elif direction == "u" :
                            if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 
                            if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True
                            if ((row+1) < 0) or ((row+1) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True
                            

                            if not changed and not board[row+1][col]   in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row+1) +' '+ str(col) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            if not changed and not board[row+1][col+1] in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                             
                            if not changed and not board[row+1][col+2] in ['  ',' s']: 
                                errors = 'ERROR: Field ' + str(row+1) +' '+ str(col+2) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                             
                            new_position += [str(row+1)+str(col)]
                            new_position += [str(row+1)+str(col+1)]
                            new_position += [str(row+1)+str(col+2)]
                        elif direction == "d" :
                            if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 
                            if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col+1) < 0) or ((col+1) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True 
                            if ((row-1) < 0) or ((row-1) > (row_input-1)) or ((col+2) < 0) or ((col+2) > (col_input-1)):
                                errors = 'ERROR: Cannot move beyond the board'
                                moves_list[itterator] = ' '
                                changed =True

                            if not changed and not board[row-1][col]   in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row-1) +' '+ str(col) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            if not changed and not board[row-1][col+1] in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row-1) +' '+ str(col+1) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                            
                            if not changed and not board[row-1][col+2] in ['  ',' s']:
                                errors = 'ERROR: Field ' + str(row-1) +' '+ str(col+2) + ' not free'
                                moves_list[itterator] = ' '
                                changed =True
                             
                            new_position += [str(row-1)+str(col)]
                            new_position += [str(row-1)+str(col+1)]
                            new_position += [str(row-1)+str(col+2)]
        else:
            moves_list[itterator] = ' '
        lengte = len(moves_list)
        itterator += 1
    valid = False
    i = 0
    j = 0
    while not valid and i < lengte:
        if moves_list[i] != ' ':
            valid = True
        i += 1
    return valid


def game_loop(board, gui_mode):
    """
    Executes the main game loop including
        * reading in a move
        * checking if the move is valid
        * if it is, doing the move
        * printing (or displaying) the board
        * and repeating.

    Args:
        board (2D array of str): The game board
        gui_mode (bool): The mode of the game, True if gui_mode, False if terminal mode
    """
    # If implemented well, this function can be used for both terminal and GUI mode.
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    scores = [0,0]
    winner = False
    player = 'Light'
    global all_moves
    global move_count
    global sink_move_light
    global sink_move_dark
    global bombs
    bombs = stdarray.create2D(row_input,col_input,False)
    all_moves = []
    pervious_fields = []
    test = 0
    for i in range(row_input):
        for j in range(col_input):
            if board[i][j] != '  ':
                test += 1
    if test != 0 :
        bDraw = False
    else:
        bDraw = True

    if gui_mode == 0 :
        print_board(board)
        while not bDraw and not winner and not stdio.isEmpty():
            #all_moves = generate_all_moves
            if move_count == 2 :
                    move_count = 0
                    if player == "Light" :
                        player = 'Dark'
                    else:   
                        player = 'Light'
            if moved_d:
                    move_count = 0
                    if player == "Light" :
                        player = 'Dark'
                    else:   
                        player = 'Light'

            if not check_legal_moves(board,player,move_count) :
                bDraw = True
            else:
                row = (stdio.readString())
                col = (stdio.readString())
                move = stdio.readString()
                check_row_col(row,col)
                row = int(row)
                col = int(col)
                if move == 'b' :
                    place_bomb(board,row,col,move_count)
                else:
                    sink = find_sink(board)
                    counter = 0
                    temp_field =(get_piece_fields(row,col,board))
                    if len(temp_field) != 0:
                        temp_field = min(temp_field)
                        row = int(temp_field[0])
                        col = int(temp_field[1])           
                
                    if move_count == 0 :
                        pervious_fields = get_piece_fields(row,col,board)
                    validate_move_file(row,col,move)
                    validate_move(row, col, move, board,player,sink,pervious_fields)
                    do_move(row, col, move, board, scores, gui_mode,sink)

                print_board(board)
            if scores[0] >= 4 :
                winner = True
                stdio.writeln("Light wins!")
            elif scores[1] >= 4 : 
                winner = True
                stdio.writeln("Dark wins!")
        
        
        light_counter = 0
        drak_counter  = 0 
        for i in range(row_input):
            for j in range(col_input):
                if board[i][j] in [' a',' b',' c',' d']:
                    light_counter += 1
                if board[i][j] in [' A',' B',' C',' D']:
                    drak_counter += 1

        if move_count == 2 :
            move_count = 0
            if player == "Light" :
                player = 'Dark'
            else:   
                player = 'Light'
        if moved_d:
            move_count = 0
            if player == "Light" :
                player = 'Dark'
            else:   
                player = 'Light'

        if player == 'Light':
            if light_counter > 0:
                if not check_legal_moves(board,player,move_count) and not winner:
                    bDraw = True 
        else:
            if drak_counter > 0:
                if not check_legal_moves(board,player,move_count) and not winner:
                    bDraw = True    
        if bDraw:
            stdio.writeln(player +" loses") 
    else:
        while not bDraw and not winner and not stdio.isEmpty():
            stddraw.clear(stddraw.WHITE)
            draw_game(board)
            while (not stddraw.hasNextKeyTyped()):
                stddraw.show(0)
            key_pressed = stddraw.nextKeyTyped()
            if move_count == 2 :
                        move_count = 0
                        if player == "Light" :
                            player = 'Dark'
                        else:   
                            player = 'Light'
            if moved_d:
                    move_count = 0
                    if player == "Light" :
                        player = 'Dark'
                    else:   
                        player = 'Light'
            if not check_legal_moves(board,player,move_count) :
                bDraw = True
            else:
                row = (stdio.readString())
                col = (stdio.readString())
                move = stdio.readString()
                check_row_col(row,col)
                row = int(row)
                col = int(col)
                if move == 'b' :
                    place_bomb(board,row,col,move_count)
                else:
                    sink = find_sink(board)
                    counter = 0
                    temp_field =(get_piece_fields(row,col,board))
                    if len(temp_field) != 0:
                        temp_field = min(temp_field)
                        row = int(temp_field[0])
                        col = int(temp_field[1])           
                
                    if move_count == 0 :
                        pervious_fields = get_piece_fields(row,col,board)
                    validate_move_file(row,col,move)
                    validate_move(row, col, move, board,player,sink,pervious_fields)
                    do_move(row, col, move, board, scores, gui_mode,sink)
                #print_board(board)
            stddraw.clear(stddraw.WHITE)
            if scores[0] >= 4 :
                winner = True
                stddraw.setPenColor(stddraw.BOOK_RED)
                stddraw.setFontSize(24)
                stddraw.text(0.5,0.9525,"Light wins!")
                stddraw.setPenColor()
                stddraw.setFontSize()
            elif scores[1] >= 4 : 
                winner = True
                stddraw.setPenColor(stddraw.BOOK_RED)
                stddraw.setFontSize(24)
                stddraw.text(0.5,0.9525,"Dark wins!")
                stddraw.setPenColor()
                stddraw.setFontSize()

        light_counter = 0
        drak_counter  = 0 
        for i in range(row_input):
            for j in range(col_input):
                if board[i][j] in [' a',' b',' c',' d']:
                    light_counter += 1
                if board[i][j] in [' A',' B',' C',' D']:
                    drak_counter += 1

        if move_count == 2 :
            move_count = 0
            if player == "Light" :
                player = 'Dark'
            else:   
                player = 'Light'
        if moved_d:
            move_count = 0
            if player == "Light" :
                player = 'Dark'
            else:   
                player = 'Light'

        if player == 'Light':
            if light_counter > 0:
                if not check_legal_moves(board,player,move_count) and not winner:
                    bDraw = True 
        else:
            if drak_counter > 0:
                if not check_legal_moves(board,player,move_count) and not winner:
                    bDraw = True    


        if bDraw:
            stddraw.setPenColor(stddraw.BOOK_RED)
            stddraw.setFontSize(24)
            stddraw.text(0.5,0.92,player +" loses") 
            stddraw.setPenColor()
            stddraw.setFontSize()




        draw_game(board)
        stddraw.show()


def place_bomb(board,row,col,move_counter):
    '''
    validates and places the bomb before move
    
    args:
        board (2D array of bool) : the game board
        row (int) : the value of the row being checked
        col (int) : the value of the column being checked 
    '''
    if board[row][col] != '  ':
        error_message('ERROR: Field ' + str(row) + ' ' + str(col)  + ' not free')
    
    if move_counter != 0 : 
        error_message('ERROR: Cannot place bomb after move')

    if bombs[row][col] :
        bombs[row][col] = False
    else:
        bombs[row][col] = True


def validate_arguments(row_input,col_input,gui_input):
    '''
    validates wheather the input is a valid input
    
    args:
        row_input(str): the amount of rows on the board
        col_input(str): the amount of columns on the board
        gui_input(str): if the game should be run in gui mode or not'''
    try:
        int(row_input)
    except ValueError:
        errors = 'ERROR: Illegal argument'
        error_message(errors,gui_input)
    try:
        int(col_input)
    except ValueError:
        errors = 'ERROR: Illegal argument'
        error_message(errors,gui_input)
    try:
        int(gui_input)
    except ValueError:
        errors = 'ERROR: Illegal argument'
        error_message(errors,gui_input)
    if not((8 <= int(row_input) <= 10) & (8 <= int(col_input) <= 10)):
         bValid = False
    
    if ((int(gui_input) != 0) & (int(gui_input) != 1)) :
        stdio.writeln("ERROR: Illegal argument")
        exit()
        

def check_row_col(row,col):
    try:
        row = int(row)
    except ValueError:
        errors = 'ERROR: Field '+ row + ' ' + col +' not on board'
        error_message(errors,gui_input)
    try:
        col = int(col)
    except ValueError:
        errors = 'ERROR: Field '+ row + ' ' + col +' not on board'
        error_message(errors,gui_input)
    if ((row) < 0) or ((row) > (row_input-1)) or ((col) < 0) or ((col) > (col_input-1)):
        errors = 'ERROR: Field '+ str(row)+' ' +str(col) + ' not on board'
        error_message(errors,gui_input)


def validate_argument_amount():
    '''
    validates wheather the amount of argument inputs is valid
    '''
    if (len(sys.argv) != 4):
       if (len(sys.argv) > 4) :
            stdio.writeln("ERROR: Too many arguments")
       else:
            stdio.writeln("ERROR: Too few arguments")
       exit()


def plot_piece(arrBoard,row,col,type,team):
    '''
    places the piece on the board

    args:
        arrboard(2D array of str): the game board
        row(int): the row where the piece will be placed
        col(int): the column where the piece will be placed

    returns:
        arrboard(2D array of str): the game board
    '''

    if type == 'a' :
        if team == 'l':
            arrBoard[row][col] = ' a'
        else:
            arrBoard[row][col] = ' A' 
    else:
        if type == 'b' :
            if team == 'l':
                arrBoard[row][col] = ' b'
            else:
                arrBoard[row][col] = ' B'
        else:
            if type == 'c' :
                if team == 'l':
                    arrBoard[row][col] = ' c'
                else:
                    arrBoard[row][col] = ' C'
            else:
                if type == 'd' :
                    if team == 'l':
                        arrBoard[row][col] = ' d'
                    else:
                        arrBoard[row][col] = ' D'
                    arrBoard[row+1][col] = str(row * col_input + col)
                    arrBoard[row][col+1] = str(row * col_input + col)
                    arrBoard[row+1][col+1] = str(row * col_input + col)
                else:
                    if type == "1" :
                        arrBoard[row][col] = ' s'
                    else:
                        if type == "2" :
                            arrBoard[row][col] = ' s'
                            arrBoard[row+1][col] = ' s'
                            arrBoard[row][col+1] = ' s'
                            arrBoard[row+1][col+1] = ' s'
                        else:
                            arrBoard[row][col] = ' x'

    return arrBoard


if __name__ == "__main__":
    # TODO: put logic here to check if the command-line arguments are correct,
    # and then call the game functions using these arguments. The following code
    # is a placeholder for this to give you an idea, and MUST be changed when
    # you start editing this file.
    ''''''
    #Commandline Inputs
    validate_argument_amount()
    row_input =sys.argv[1]
    col_input =sys.argv[2]
    gui_input =sys.argv[3]
    #validation of inputs
    validate_arguments(row_input,col_input,gui_input)
    row_input = int(row_input)
    col_input = int(col_input)
    gui_input = int(gui_input)

    #board setup
    board = read_board(row_input, col_input)
    #print_board(board)

    move_count = 0
    moved_d = False
    sink_move_dark = 0
    sink_move_light = 0
    stddraw.setPenRadius(0.001)
    stddraw.setCanvasSize(700,700)
    game_loop(board, gui_input)

    