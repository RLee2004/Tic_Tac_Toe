from operator import truediv
from turtle import Screen, color
import pygame, sys
import numpy as np
 
pygame.init()
 
Height = 525
Width = 525
Row = 3
Column = 3
Circle_Radius = 50
Circle_Width = 10
 
Player = 1
Game_over = False
 
Background = (64, 191, 189) #40BFBD
Line = (64, 130, 191) ##4082bf
Display = pygame.display.set_mode((Height, Width))
Title = pygame.display.set_caption('Tic Tac Toe')
Display.fill(Background)
 
board = np.zeros((Row, Column))
print(board)
 
# Draws the 3x3 grid
def line():
    #Horizontal 1
    pygame.draw.line(Display, Line, (0, 175), (525, 175), 10)
    #Horizontal 2
    pygame.draw.line(Display, Line, (0, 350), (525, 350), 10)
    #Vertical 1
    pygame.draw.line(Display, Line, (175, 0), (175, 525), 10)
    #Vertical 2
    pygame.draw.line(Display, Line, (350, 0), (350, 525), 10)
 
line()
 
# Assigns a mark on the square's coordinates.
def mark_square(row, column, player):
    board[row][column] = player
 
# Checks if there is a mark in the square. 
def check_square(row,column):
    return board[row][column] == 0
 
# Checks to see if the board is full or not.
def board_full():
    for row in range(Row):
        for column in range(Column):
            if board[row][column] == 0:
                return False
        return True
 
# Draws either an X or O on the position clicked.
def shapes():
    for row in range(Row):
        for column in range(Column):
            if board[row][column] == 1:
                pygame.draw.circle(Display, (0, 0, 128), (int( column * 175 + 175/2), int ( row * 175 + 175/2)), Circle_Radius, Circle_Width)
            elif board[row][column] == 2:
                pygame.draw.line(Display, (128, 128, 0), (column * 175 + 50, row * 175 + 50), (column * 175 + 175 - 50, row * 175 + 175 - 50), 15)
                pygame.draw.line(Display, (128, 128, 0), (column * 175 + 50, row * 175 + 175 - 50), (column * 175 + 175 - 50, row * 175 + 50), 15)
 
# Win Conditions
def check_win(player):
    for col in range(Column):
       if board[0][col] == player and board[1][col] == player and board[2][col] == player:
           y_win(col,player)
           return True
  
    for row in range(Row):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            x_win(row,player)
            return True
    
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        diagonal1(player)
        return True
 
    if board[0][0] == player and board[1][1] == player and board [2][2] == player:
        diagonal2(player)
        return True
 
    return False 
    
def y_win(col,player):
    XPos = col * 175 + 175/2
    if player == 1:
        color = (0, 0, 128)
    elif player == 2:
        color = (128, 128, 0)
 
    pygame.draw.line(Display, color, (XPos, 15), (XPos, Height - 15), 15)
    
 
def x_win(row,player):
    YPos = row * 175 + 175/2
    if player == 1:
        color = (0, 0, 128)
    elif player == 2:
        color = (128, 128, 0)
    
    pygame.draw.line(Display, color, (15, YPos), (Width - 15, YPos), 15)
 
 
def diagonal1(player):
    if player == 1:
        color = (0, 0, 128)
    elif player == 2:
        color = (128, 128, 0)
    
    pygame.draw.line(Display, color, (15, Height - 15), (Width - 15, 15),15)
 
 
def diagonal2(player):
    if player == 1:
        color = (0, 0, 128)
    elif player == 2:
        color = (128, 128, 0)
    
    pygame.draw.line(Display, color, (15,15),(Width-15,Height-15),15)
 
def restart():
    Display.fill(Background)
    line()
    player = 1
    for row in range(Row):
        for col in range (Column):
            board[row][col] = 0
 
# A constant loop of code that makes the window work.
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.MOUSEBUTTONDOWN and not Game_over:
 
            YPos = event.pos[0]
            XPos = event.pos[1]
 
            click_col = int(YPos // 175)
            click_row = int(XPos // 175)
 
            if check_square(click_row, click_col):
                if Player == 1:
                    mark_square(click_row,click_col, 1)
                    if check_win(Player):
                        Game_over = True
                    Player = 2
 
                elif Player == 2:
                    mark_square(click_row,click_col, 2)
                    if check_win(Player):
                        Game_over = True
                    Player = 1
                shapes()
                print(board)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                restart()
                Player = 1
                Game_over = False
            
    pygame.display.update()