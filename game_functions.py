separator = "=" * 40
player1 = "X"
player2 = "O"
current_player = player1
empty_fields = list(range(1,10))
line = "+---"*3 + "+"
board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" ",
         }

def welcome():
    print(f"""""
Welcome to Tic Tac Toe
{separator}
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
{separator}
Let's start the game
""")

def print_board():
    print(line)
    print(f"| {board[1]} | {board[2]} | {board[3]} |")
    print(line)
    print(f"| {board[4]} | {board[5]} | {board[6]} |")
    print(line)
    print(f"| {board[7]} | {board[8]} | {board[9]} |")
    print(line)

def player_move(stone):
    while True:
        move = int(input(f"Player {stone} | Please enter your move number: "))
        if move in empty_fields:
            empty_fields.remove(move)
            board[move] = stone
            print_board()
            change_player(stone)
            break
        elif move in range(1,10):
            print("This field is already taken")
        else:
            print("Please choose number 1-9")

def change_player(stone):
    global current_player
    if stone == "X":
        current_player = player2
    else:
        current_player = player1

def check_win():
    if board[1] == board[2] == board[3] != " ":
        print(f"Congratulations, the player {board[1]} WON!")
        exit()
    elif board[4] == board[5] == board[6] != " ":
        print(f"Congratulations, the player {board[4]} WON!")
        exit()
    elif board[7] == board[8] == board[9] != " ":
        print(f"Congratulations, the player {board[7]} WON!")
        exit()
    elif board[1] == board[4] == board[7] != " ":
        print(f"Congratulations, the player {board[1]} WON!")
        exit()
    elif board[2] == board[5] == board[8] != " ":
        print(f"Congratulations, the player {board[2]} WON!")
        exit()
    elif board[3] == board[6] == board[9] != " ":
        print(f"Congratulations, the player {board[3]} WON!")
        exit()
    elif board[1] == board[5] == board[9] != " ":
        print(f"Congratulations, the player {board[1]} WON!")
        exit()
    elif board[3] == board[5] == board[7] != " ":
        print(f"Congratulations, the player {board[3]} WON!")
        exit()

def check_tie():
    if len(empty_fields) == 0:
        print(f"No one wins the game.")
        exit()

def game():
    global current_player
    print_board()
    while True:
        player_move(current_player)
        check_win()
        check_tie()