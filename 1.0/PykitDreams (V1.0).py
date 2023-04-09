from datetime import date
import numpy as np
import sys
import turtle
import random
import pygame
import turtle
import calendar

class Computer:
    def __init__(self, company, model):
        self.company = company
        self.model = model

def hello():
  
    name = str(input("Enter your name: "))
    
    print("Hello there " + str(name) + "! Welcome to PykitDreams - a CodeMaster7000 Studios Python module designed to revolutionise the way you use your computers!"))
    
def calendar(): 
    
    y = int(input("Enter year: "))  
    m = int(input("Enter month: "))  
    print(calendar.month(y,m))      
    
def datecalculator():
    
    fdate = date(a, b, c) #Enter first date here.
    ldate = date(d, e, f) #Enter last date here.
    delta = ldate - fdate
    print(delta.days)
    
def fourfunctionscalculator():  
    
    operation = input("Please enter the symbol for the operation you would like to complete: ")

    number_1 = int(input("Please enter your first number: "))
    number_2 = int(input("Please enter the second number: "))

    if operation == '+':
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print("{} / {} = ".format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("Invalid operator.")

def scientificcalculator():
    # Scientific Calculator by @SmashedFrenzy16
        
def typingtest():
    # Typing Test by @CodeMaster7000
    
    from time import time
    
    def typingErrors(prompt):
        global iwords

        words = prompt.split()
        errors = 0

        for i in range(len(iwords)):
            if i in (0, len(iwords)-1):
                if iwords[i] == words[i]:
                    continue
            else:
                errors +=1
                else:
                    if iwords[i] == words[i]:
                        if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                            continue
                        else:
                            errors += 1
                    else:
                        errors += 1
        return errors

    def typingSpeed(iprompt, stime, etime):
        global time
        global iwords

        iwords = iprompt.split()
        twords = len(iwords)
        speed = twords / time

        return speed

    def timeElapsed(stime, etime):
        time = etime - stime

        return time

    if __name__ == '__main__':
        prompt = "\n\nA turquoise-blue stream wound its merry way through the forest. Babbling and burbling, it sprung over the limestone rocks in its way. Pebbles whisked about in the under wash like pieces of glitter. Streams are the liquid soul of the forest, and this one was glowing. Chords of soft light speared down from above, bathing its surface in gold. It was glinting with little sparkles, like a thousand diamonds blessed with an inner fire. A galaxy of dragonflies fizzed through the beams of light, wings a-glitter in the sun."
        print("TYPE THIS: ", prompt,"")

        input("\nPress 'Enter' when you are ready!")

        stime = time()
        iprompt = input()
        etime = time()

        time = round(timeElapsed(stime, etime), 2)
        speed = typingSpeed(iprompt, stime, etime)
        errors = typingErrors(prompt)

        print("Total time elapsed:", time, "s")
        print("Mean typing speed:", speed, "words/minute")
        print("With a total of:", errors, "errors")

def tictactoe():
    
    # Tic Tac Toe game by CodeMaster7000
    
    pygame.init()

    WIDTH = 600
    HEIGHT = 600
    LINE_WIDTH = 15
    WIN_LINE_WIDTH = 15
    BOARD_ROWS = 3
    BOARD_COLS = 3
    SQUARE_SIZE = 200
    CIRCLE_RADIUS = 60
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25
    SPACE = 55
    RED = (255, 0, 0)
    BG_COLOR = (20, 200, 160)
    LINE_COLOR = (23, 145, 135)
    CIRCLE_COLOR = (239, 231, 200)
    CROSS_COLOR = (66, 66, 66)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill( BG_COLOR)

    board = np.zeros((BOARD_ROWS, BOARD_COLS))

    def draw_lines():
	
	    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
	
	    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

	    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)

	    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures():
	    for row in range(BOARD_ROWS):
		    for col in range(BOARD_COLS):
			    if board[row][col] == 1:
				    pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH)
			    elif board[row][col] == 2:
				    pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)	
				    pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

    def mark_square(row, col, player):
	    board[row][col] = player

    def available_square(row, col):
	    return board[row][col] == 0

    def is_board_full():
	    for row in range(BOARD_ROWS):
		    for col in range(BOARD_COLS):
			    if board[row][col] == 0:
				    return False

	    return True

    def check_win(player):
	    for col in range(BOARD_COLS):
		    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			    draw_vertical_winning_line(col, player)
			    return True

	    for row in range(BOARD_ROWS):
		    if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			    draw_horizontal_winning_line(row, player)
			    return True

	    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		    draw_asc_diagonal(player)
		    return True

	    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		    draw_desc_diagonal(player)
		    return True

	    return False

    def draw_vertical_winning_line(col, player):
	    posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	    if player == 1:
		    color = CIRCLE_COLOR
	    elif player == 2:
		    color = CROSS_COLOR

	    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)

    def draw_horizontal_winning_line(row, player):
	    posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	    if player == 1:
		    color = CIRCLE_COLOR
	    elif player == 2:
		    color = CROSS_COLOR

	    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)

    def draw_asc_diagonal(player):
	    if player == 1:
		    color = CIRCLE_COLOR
	    elif player == 2:
		    color = CROSS_COLOR

	    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)

    def draw_desc_diagonal(player):
	    if player == 1:
		    color = CIRCLE_COLOR
	    elif player == 2:
		    color = CROSS_COLOR

	    pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

    def restart():
	    screen.fill( BG_COLOR )
	    draw_lines()
	    for row in range(BOARD_ROWS):
		    for col in range(BOARD_COLS):
			    board[row][col] = 0

    draw_lines()

    player = 1
    game_over = False

    while True:
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    sys.exit()

		    if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			    mouseX = event.pos[0] 
			    mouseY = event.pos[1] 

			    clicked_row = int(mouseY // SQUARE_SIZE)
			    clicked_col = int(mouseX // SQUARE_SIZE)

			    if available_square(clicked_row, clicked_col):

				    mark_square(clicked_row, clicked_col, player)
				    if check_win(player):
					    game_over = True
				    player = player % 2 + 1

				    draw_figures()

		    if event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_r:
				    restart()
				    player = 1
				    game_over = False

	    pygame.display.update()

sampleInput = input("Sample input: ")

errorMessage = print("An unexpected error occurred.")

helloWorld = print("Hello world!")
