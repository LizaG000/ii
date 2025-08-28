import random
import io, sys
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
list_of_words =  [
    'яблоко',  'победа',  'программирование', 'терминал',  'ноутбук'
]
random_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
set_of_symbols = set(random_word)
discovered_symbols = set()
health = 5
print('_ '*len(random_word))
while discovered_symbols != set_of_symbols and health > 0:
    user_symbol = input('> ')
    print(user_symbol)
    assert len(user_symbol) == 1
    if user_symbol in discovered_symbols:
        print('Вы уже вводили эту букву, попробуйте что-нибудь другое')
    elif user_symbol not in set_of_symbols:
        health -= 1
        print('Этой буквы нет в слове. Текущее кол-во жизней: {}'.format(health))
    elif user_symbol in set_of_symbols:
        print('Буква есть в слове!')
        discovered_symbols.add(user_symbol)
    current_word_progress = ''
    for ch in random_word:
        current_word_progress += '_ ' if ch not in discovered_symbols else ch + ' '
    print(current_word_progress)
if health == 0:
    print('Жизни закончились :(')
else:
    print('Поздравляю, вы правильно набрали слово {}'.format(random_word))