print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
board = list(range(1, 10))
board_5 = list(range(1, 26))

def get_win_5():
    winning_combinations = []

    # Горизонтальные выигрышные комбинации
    horizontal_wins = [(row, col, col + 1, col + 2) for row in range(25) for col in range(23)]
    winning_combinations.extend(horizontal_wins)
    # Вертикальные выигрышные комбинации
    vertical_wins = [(row, col, row + 1, col, row + 2, col) for col in range(25) for row in range(23)]
    winning_combinations.extend(vertical_wins)

    # Диагональные комбинации (слева направо)
    diagonal_wins_lr = [(row, col, row + 1, col + 1, row + 2, col + 2) for row in range(23) for col in range(23)]
    winning_combinations.extend(diagonal_wins_lr)

    # Диагональные комбинации (справа налево)
    diagonal_wins_rl = [(row, col, row + 1, col - 1, row + 2, col - 2) for row in range(23) for col in range(2, 25)]
    winning_combinations.extend(diagonal_wins_rl)
    winning_combinations = horizontal_wins + vertical_wins + diagonal_wins_rl + diagonal_wins_lr
    print(winning_combinations)
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
            print("|", board[0 + i * 5], " |", board[1 + i * 5], " |", board[2 + i * 5], " |", board[3 + i * 5], " |", board[4 + i * 5], " |")
        elif i == 1:
            print("|", board[0 + i * 5], " |", board[1 + i * 5], " |", board[2 + i * 5], " |", board[3 + i * 5], " |",  board[4 + i * 5], "|")
        else:
            print("|", board[0 + i * 5], "|", board[1 + i * 5], "|", board[2 + i * 5], "|", board[3 + i * 5], "|", board[4 + i * 5], "|")
        print("-" * 26)

def take_input(player_token, board_,  n):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= n:
            if str(board_[player_answer - 1]) not in "XO":
                board_[player_answer - 1] = player_token
                valid = True
                return board_
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
    if len(board) == 9:
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    else:
        win_coord = win_5
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
def main(board_):
    n = max(board_)
    counter = 0
    win = False
    while not win:
        if n == 9:
            draw_board(board_)
        else:
            draw_board_5(board_)
        if counter % 2 == 0:
            take_input("X", board_, n)
        else:
            take_input("O", board_, n)
        counter += 1
        if counter > 4:
            tmp = check_win(board_)
            if tmp:
                print(tmp, "выиграл!")
                break
        if counter == n:
            print("Ничья!")
            break
    draw_board(board_)

command = input("Введаите режим a или b: ")
if command == "a":
    win_5 = get_win_5()
    main(board_5)
# main(board)
# input("Нажмите Enter для выхода!")