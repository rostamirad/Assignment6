import pyfiglet
import random
import time
from colorama import Fore

game_board = [ ["_", "_", "_"] ,
               ["_", "_", "_"] ,
               ["_", "_", "_"] ]

def show_borad(): # Color adjustment
    for row in game_board:
        for cell in row:
            if cell == "X":
                print(Fore.RED + "X", end= " ")
            elif cell == "O":
                print(Fore.BLUE + "O", end=" ")
            else:
                print(Fore.RESET + cell, end= " ")
        print(Fore.RESET)

def player(number: int, sign: str):
    while True:
        print()
        print("Player unmber: ", number)
        print()
        row = int(input("Enter the row number: "))
        col = int(input("Enter the column number: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "_":
                game_board[row][col] = sign
                show_borad()
                print()
                break
            else :
                print("Select another cell that is empty:) ")
        else:
            print("Just enter a number between 0 and 2 for row and column: ")
            show_borad()

start = time.time()

def game_1():
    counter = 0
    while True:
        row = random.randint(0,2) 
        col = random.randint(0,2)
        if game_board[row][col] == "_":
            game_board[row][col] = "O"
            print("💻: ") 
            print()
            show_borad() 
            counter += 1
            if counter == 9 and check_game("O") == False and check_game("X") == False:
                print("mosavi! ")
                break
            if check_game("O") == True:
                end_time = time.time()
                print("💻 is winner! ")
                print("Game end ⏱ is: ", end_time - start, "seconds")
                break
            else:
                player(1, "X")
                counter += 1
                if counter == 9 and check_game("X") == False and check_game("O") == False:
                    print("mosavi! ")
                    break
                if check_game("X") == True:
                    end_time = time.time()
                    print("Player1 is winner! ")
                    print("Game end ⏱ is: ", end_time - start, "seconds")
                    break
                else:
                    continue
            
def game_2():
    counter = 0
    while True:
        player(1, "X")
        counter += 1
        if counter == 9 and check_game("X") == False and check_game("O") == False:
            print("mosavi! ")
            break
        if check_game("X") == True:
            end_time = time.time()
            print("Player1 is winner! ")
            print("Game end ⏱ is: ", end_time - start, "seconds")
            break
        else:
            player(2, "O")
            if counter == 9 and check_game("X") == False and check_game("O") == False:
                print("mosavi! ")
                break
            if check_game("O") == True:
                print("Player2 is winner! ")
                break
            else:
                continue
        

def check_game(sign):
    win = False
    for i in range(3):
        if game_board[0][i] == game_board[1][i] == game_board[2][i] == sign or game_board[i][0] == game_board[i][1] == game_board[i][2] == sign:
            win = True
            break
    if game_board[0][0] ==  game_board[1][1] == game_board[2][2] == sign or game_board[0][2] == game_board[1][1] == game_board[2][0] == sign:
        win = True
    return win

title = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
print("Welcome to: ")
print(title)
print("Menu: ")
print()
Player_Choice = int(input("1: single player, 2: for double player: "))
print()
if Player_Choice == 1:
    print("Player1️⃣  vs 💻") #player vs cpu
    print()
    game_1()
elif Player_Choice == 2:
    print("Player1️⃣  vs Player2️⃣") #player vs player
    print()
    game_2()
