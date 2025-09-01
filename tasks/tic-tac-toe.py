import random
print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
board = list(range(1, 10))
board_5 = list(range(1, 26))

def get_win_5():
    winning_combinations = []
    for i in range(5):
        for j in range(3):
            n = i * 5 + j
            winning_combinations.append((n, n+1, n+2))
    for i in range(3):
        for j in range(5):
            n = i * 5 + j
            winning_combinations.append((n, n+5, n+10))
    for i in range(3):
        for j in range(5):
            if (i * 5 + j + 1) % 5 != 0 and (i * 5 + j + 1) % 5 != 4:
                n = i * 5 + j
                winning_combinations.append((n, n+6, n+12))
    for i in range(3):
        for j in range(5):
            if (i * 5 + j + 1) % 5 != 1 and (i * 5 + j + 1) % 5 != 2:
                n = i * 5 + j
                winning_combinations.append((n, n+4, n+8))
    return winning_combinations



def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)
def draw_board_5(board):
    print("-" * 30)
    for i in range(5):
        if i == 0:
            print("| ", board[0 + i * 5], "| ", board[1 + i * 5], "| ", board[2 + i * 5], "| ", board[3 + i * 5], "| ", board[4 + i * 5], "|")
        elif i == 1:
            print("| ", board[0 + i * 5], "| ", board[1 + i * 5], "| ", board[2 + i * 5], "| ", board[3 + i * 5], "|",  board[4 + i * 5], "|")
        else:
            print("|", board[0 + i * 5], "|", board[1 + i * 5], "|", board[2 + i * 5], "|", board[3 + i * 5], "|", board[4 + i * 5], "|")
        print("-" * 26)

def take_input(player_token, board_,  n):
    while True:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= n:
            if player_answer > 9:
                player_token = " " + player_token
            if str(board_[player_answer - 1]) not in "XO":
                board_[player_answer - 1] = player_token
                return board_
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до {}.".format(n))

def take_computer(computer_token: str, board_: list):
    computer_answer = None
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    if computer_token == "O":
        player_token = "X"
    else:
        player_token = "O"
    if board_.count(player_token) < 1:
        if board_.count(computer_token) == 0:
            computer_answer = random.randint(1, 8)
        else:
            i = board_.index(computer_token)
            for each in win_coord:
                if i in each:
                    if i == each[0]:
                        computer_answer = each[2]
                    elif i == each[1]:
                        computer_answer = each[0]
                    else:
                        computer_answer = each[1]
    else:
        i = random.randint(1, 100)
        if i > 70:
            for each in win_coord:
                if each[0] == player_token and each[1] == player_token:
                    computer_answer = each[2] + 1
                elif each[0] == player_token and each[2] == player_token:
                    computer_answer = each[1] + 1
                elif each[1] == player_token and each[2] == player_token:
                    computer_answer = each[0] + 1
        if i <= 70 or computer_answer is None:
            computer_answer = random.randint(0, 8)
            while str(board_[computer_answer]) == "X" or str(board_[computer_answer]) == "O":
                computer_answer = random.randint(0, 8)
    print(f"Компьютер поставил {computer_token} на {computer_answer}")
    board_[computer_answer] = computer_token
    return board_

def check_win(board, symb):
    if len(board) == 9:
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    else:
        win_coord = win_5
    for each in win_coord:
        if symb in str(board[each[0]]) and  symb in str(board[each[1]] )and  symb in str(board[each[2]]):
            return board[each[0]]
    return False

def main_a(board_):
    n = max(board_)
    counter = 0
    while True:
        draw_board_5(board_)
        if counter % 2 == 0:
            symb = "X"
        else:
            symb = "O"
        take_input(symb, board_, n)
        counter += 1
        if counter > 4:
            tmp = check_win(board_, symb)
            if tmp:
                print(tmp, "выиграл!")
                break
        if counter == n:
            print("Ничья!")
            break
    draw_board_5(board_)

def main_b(board_, user):
    n = max(board_)
    counter = 0
    while True:
        draw_board(board_)
        if counter % 2 == 0:
            symb = "X"
        else:
            symb = "O"
        if user:
            take_input(symb, board_, n)
        else:
            take_computer(symb, board_)
        counter += 1
        if counter > 4:
            tmp = check_win(board_, symb)
            if tmp and user:
                print("Вы победили!")
                break
            if tmp and not user:
                print("Выиграл компьютер!")
                break
        if counter == n:
            print("Ничья!")
            break
        user = not user
    draw_board(board_)




command = input("Введаите режим a или b: ")
while command != "a" and command != "b":
    command = input("Введаите режим a или b: ")
if command == "a":
    win_5 = get_win_5()
    main_a(board_5)
else:
    user = random.randint(0, 1)
    if user:
        user = True
    else:
        user = False
    main_b(board, user)


input("Нажмите Enter для выхода!")