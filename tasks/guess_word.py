import random

list_of_words =  [
    'яблоко',  'победа',  'программирование', 'терминал',  'ноутбук', 'паук', 'грифон', 'ключник', 'перец', 'работа',
]
random_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
set_of_symbols = set(random_word)
discovered_symbols = set()
input_symbols = set()
health_p = 5
health_c = 5
c_p = 0
print('_ '*len(random_word))
cyrillic_lowercase = ''.join(chr(code) for code in range(ord('а'), ord('я') + 1))
while health_p > 0 or health_c > 0:
    if c_p == 0:
        user_symbol = input('игрок: ')
    else:
        user_symbol = random.choice(cyrillic_lowercase)
        print('компьютер: {}'.format(user_symbol))

    assert len(user_symbol) == 1
    if user_symbol in input_symbols:
        print('Эта буква уже пробовалась, попробуйте что-нибудь другое')
        continue
    elif user_symbol not in set_of_symbols:
        if c_p == 0:
            health_p -= 1
            print('Этой буквы нет в слове. Текущее кол-во жизней у вас: {}'.format(health_p))
        else:
            health_c -= 1
            print('Этой буквы нет в слове. Текущее кол-во жизней у компьютера: {}'.format(health_c))
    elif user_symbol in set_of_symbols:
        print('Буква есть в слове!')
        discovered_symbols.add(user_symbol)
        if discovered_symbols == set_of_symbols:
            break
    input_symbols.add(user_symbol)
    current_word_progress = ''
    if health_p > 0 and c_p == 1:
        c_p = 0
    elif health_c > 0 and c_p == 0:
        c_p = 1
    for ch in random_word:
        current_word_progress += '_ ' if ch not in discovered_symbols else ch + ' '
    print()
    print(current_word_progress)


if health_p == 0:
    print('Жизни игрока закончились :(')
else:
    if c_p == 0:
        print('Поздравляю, вы правильно набрали слово {}'.format(random_word))
    else:
        if health_p == 0:
            print('Жизни компьютера закончились :(')
        else:
            print('Вы проиграли. Победа за компьютером! Правильное слово {}'.format(random_word))