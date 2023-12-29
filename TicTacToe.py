import random, os

winning_combos = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

def check_winner(board):

    for combo in winning_combos:
        symbols = [board[row][col] for row, col in combo]
        if len(set(symbols)) == 1 and symbols[0] != ' ':
            return symbols[0]
    if ' ' not in board[0] + board[1] + board[2]:
        return 'Draw'
    return None

def computer():
    computer_row = random.randint(0,2);computer_rows.append(computer_row)
    computer_column = random.randint(0,2);computer_columns.append(computer_column)
    return computer_row, computer_column

all = [[' ' for i in range(3)] for i in range(3)]

u_shape = input("Which one do you want? ['X' or 'O']? ").upper()
if u_shape == 'X':
    c_shape = 'O'
else:
    c_shape = 'X' 

while True:
    os.system('cls')
    for row in all:
        print(row) 

    computer_row = random.randint(0,2)
    computer_column = random.randint(0,2)

    user_row = int(input("Enter the row[1,2,3]: "))
    user_column = int(input("Enter the column[1,2,3]: "))
    
    if (user_column and user_row) >= 1 and (user_column and user_row) <= 3 and (all[user_row-1][user_column-1]) != c_shape:
        all[user_row-1][user_column-1] = u_shape
    else:
        print("Please chose between 1 and 3!");input("press enter to continue..")  
    
    while (all[computer_row][computer_column]) != ' ':
        computer_row, computer_column = computer()
    else:
        all[computer_row][computer_column] = c_shape
        
    status = check_winner(all)
    if status is not None:
        for row in all:
            print(row)
        if status == 'Draw':
            print('The game is a draw.')
        else:
            print(f'The winner is {status}.')
        input("press enter to exit!")
        break
