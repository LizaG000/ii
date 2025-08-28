from random import randint
t = ["Камень", "Бумага", "Ножницы"]
computer = t[randint(0, 2)]
player = False
while player == False:
    player = input("Камень, Ножницы, Бумага? > ")
    if player == computer:
        print("Ничья!")
    elif player == "Камень":
        if computer == "Бумага":
            print("Ты проиграл!", computer, "накрывает", player)
        else:
            print("Ты выиграл!", player, "разбивает", computer)
    elif player == "Бумага":
        if computer == "Ножницы":
            print("Ты проиграл!", computer, "режет", player)
        else:
            print("Ты победил!", player, "накрывает", computer)
    elif player == "Ножницы":
        if computer == "Камень":
            print("Ты проиграл!", computer, "разбивает", player)
        else:
            print("Ты выиграл!", player, "режет", computer)
    else:
        print("Некорректный ход!")
    player = False
    computer = t[randint(0, 2)]