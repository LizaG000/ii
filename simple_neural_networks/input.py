from attr.validators import min_len
from pygments.lexer import words


# получение словоря русских слов
def get_dictionary_dataset() -> list[str]:
    with open("dictionary_dataset.txt", 'r', encoding='utf-8') as file:
        content = file.read()
        return content.split("\n")

dictionary = get_dictionary_dataset()

def filter_dictionary(input_words: str) -> tuple[str, float]:
    _min = 100
    find_word = input_words
    max_len = len(input_words) + 2
    if max_len - 4> 0:
        min_len = max_len - 4
    else:
        min_len = 1
    for word in dictionary:
        if len(word) >= min_len and len(word) <= max_len:
            if word == input_words:
                return word, 0
            if len(set(word) & set(input_words)) < max(len(word), len(input_words)) // 2:
                # print(len(set(word) & set(input_words)), input_words, word, set(word) & set(input_words))
                continue
            if len(word) < 3 or len(input_words) < 3:
                changes = levenshtein_algorithm(input_words, word)
                # print(changes)
                if changes < _min:
                    _min = changes
                    find_word = word
            elif word[0] in input_words[0:3] or word[1] in input_words[0:3] or word[2] in input_words[0:3]:
                # print(word, input_words[0:3], word[0] in input_words[0:3], word[1] in input_words[0:3],
                #       word[2] in input_words[0:3],
                #       word[0] in input_words[0:3] or word[1] in input_words[0:3] or word[2] in input_words[0:3])
                changes = levenshtein_algorithm(input_words, word)
            else:
                changes = 100
            if changes < _min and not ( (len(input_words) - len(word) == 1) and not input_words[-1] in "смить"):
                _min = changes
                find_word = word
    return  find_word, _min

def levenshtein_algorithm(input_word, word) -> float:
    k_array = []
    replacement = [("и", "е"), ("а", "о"), ("д", "т"), ("з", "с"), ("г", "к"), ("б", "п"), ("в", "ф"), ("ж", "ш")]
    for i in range(len(input_word)+1):
        k_array.append([i] + [0] * len(word))
    for i in range(len(word)+1):
        k_array[0][i] = i
    for i in range(1, len(input_word)+1):
        for j in range(1, len(word)+1):
            k = 1
            if input_word[i-1] == word[j-1]:
                k = 0
            elif (input_word[i-1], word[j-1]) in replacement or (word[j-1], input_word[i-1]) in replacement:
                k = 0.2
            # print((input_word[i-1], word[j-1]) in replacement, (word[j-1], input_word[i-1]) in replacement)
            # print(input_word, word, input_word[i-1], word[j-1],i, j, k)
            # print(k_array[i][j-1]+1, k_array[i-1][j]+1, k_array[i-1][j-1]+k)
            k = min(k_array[i][j-1]+1, k_array[i-1][j]+1, k_array[i-1][j-1]+k)
            if k > 3 and i == j:
                return 100
            else:
                k_array[i][j] = k
    print(input_word,word)
    for i in k_array:
        for j in i:
            print(j, end=" ")
        print()
    print()
    return k_array[-1][-1]

def clearing_input(_input: str):
    punctuation_marks = ".,/?!*\"_+&=-\\\n"
    # Очистка двойных и более пробелов
    _input.strip()
    _input = ' '.join((_input.split()))
    _input = _input.split(" ")
    clean_input = len(_input) * ["_"]
    i = 0
    while i < len(_input):
        if _input[i][-1] in punctuation_marks:
            _input.insert(i+1, _input[i][-1])
            clean_input.insert(i+1, _input[i][-1])
            _input[i] = _input[i][:-1]
        if len(_input) - i > 1:
            input_word, _min = filter_dictionary("".join([_input[i], _input[i+1]]))
            if _min <= 3:
                _input[i], clean_input[i] = "_", input_word
                _input.pop(i+1)
                clean_input.pop(i+1)
                i += 1
                continue
        input_word, _min = filter_dictionary(_input[i])
        print(input_word, _min)
        if _min <= 3:
            _input[i], clean_input[i] = "_", input_word
            i += 1
            continue
        print("Ошибка")
        break
    return clean_input




#прив хочу красное кресло
print(("ж", "ш") == ("ж", "ш"))
s = input()
# clearing_input(s)
print(clearing_input(s))

