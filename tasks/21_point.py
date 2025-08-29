import random
import time
def last_bot(score_carts, score_bota):
    if random.uniform(0, 1) < k:
        score_carts = 21 - score_bota
        if score_bota > 11:
            if score_bota - 11 < 2:
                n = 10
            else:
                n = 11
            print("Боту выпало", n, "очков.")
            score_bota += n
            print("У бота ", score_bota, "очков.")
            print("Бот берет карту")
            score_carts = score_carts - n
            return score_carts, score_bota
    return score_carts, score_bota
# Счет
score_playera = 0
score_bota = 0
# Начальное сообщение
all_carts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Поиграем в 21? \nЕсли хотите играть нажмите Enter, если хотите выйти, то нажмите Ctrl+C")
input()
k = random.uniform(0, 1)
# Цикл
while True:
    if score_playera == 21:
        print("Больше карт не надо, у вас 21")
        print("Вы автоматически победили бота, так как у вас 21.")
        input("Нажмите Enter, чтобы закрыть окно.");
        break
    if score_playera > 21:
        print("Вы проиграли, так как набрали больше 21")
        print("Попытайте свою попытку в другой раз.")
        input("Нажмите Enter, чтобы закрыть окно.");
        break
    yes_or_no = input(
        "Будете ли вы брать карту?\nВведите yes, если хотите брать карту или введите no, если не берете карту.\n")
    if yes_or_no == 'yes':
        score_carts = random.choice(all_carts)
        print("Вы взяли карту выпало:", score_carts)
        score_playera += score_carts
        print("Сейчас у вас ", score_playera)
    if yes_or_no == 'no':
        print("У вас ", score_playera, "очков.")
        print("Ход бота")
        time.sleep(3)
        while True:
            if score_bota < 15:
                print("Бот берет карту")
                score_carts = random.choice(all_carts)
                if score_bota + score_carts > 21 or score_bota + score_carts == 20:
                    score_carts, score_bota = last_bot(score_carts, score_bota)
                print("Боту выпало", score_carts, "очков.")
                score_bota += score_carts
                print("У бота ", score_bota, "очков.")
                time.sleep(3)
            if score_bota > 21:
                print("Бот проиграл.\nТак как у него", score_bota, "очков, а у вас ", score_playera)
                input("Нажмите Enter, чтобы закрыть");
                exit(0)
            if score_bota < score_playera:
                print("Бот берет карту")
                score_carts = random.choice(all_carts)
                score_carts, score_bota = last_bot(score_carts, score_bota)
                print("Боту выпало", score_carts, "очков.")
                score_bota += score_carts
                print("У бота ", score_bota, "очков.")
                time.sleep(3)
            if score_bota > 21:
                print("Вы автоматически победили бота, так как у него {} очков.".format(score_bota))
                input("Нажмите Enter, чтобы закрыть окно.");
                exit(0)
            if score_bota > score_playera:
                print("Бот победил.\nТак как у него", score_bota, "очков, а у вас ", score_playera,
                      "\nНе растраивайтесь. Попробуйте ещё раз.")
                input("Нажмите Enter, чтобы закрыть");
                exit(0)
            if score_bota == score_playera:
                print("Вы набрали равное количество очков и у вас ничья")
                input("Нажмите Enter, чтобы закрыть");
                exit(0)