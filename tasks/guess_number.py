import random

random_number = random.randint(1, 100)
user_guess = 0

print("Я загадал число от 1 до 100, попробуй его угадать!")
while user_guess != random_number:
    user_guess = int(input(">"))
    if random_number > user_guess:
        print('Больше, чем {}!'.format(user_guess))
    elif random_number < user_guess:
        print('Меньше, чем {}!'.format(user_guess))
    else:
        print('Верно! Я загадал число {}'.format(random_number))