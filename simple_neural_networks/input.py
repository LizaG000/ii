from natasha import MorphVocab

def get_dictionary_dataset() -> list[str]:
    with open("dictionary_dataset.txt", 'r', encoding='utf-8') as file:
        content = file.read()
        return content.split("\n")

def get_token_dataset() -> list[str]:
    with open("token_dataset.txt", 'r', encoding='utf-8') as file:
        content = file.read()
        return content.split("\n")

def get_data(title: str) -> tuple[list[str], list[str]]:
    with open(title, 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.split("\n")
        x = [content[i] for i in range(0, len(content), 2)]
        y = [content[i] for i in range(1, len(content), 2)]
        return x, y


def filter_dictionary(input_words: str) -> tuple[str, float]:
    _min = 100
    find_word = input_words
    vocab = MorphVocab()
    normal_forms = vocab.normal_forms(input_words)[0]
    if normal_forms in dictionary:
        return input_words, 0
    len_max = len(input_words) + 2
    len_min = len_max - 4
    for word in dictionary:
        if len_min < len(word) and len_max > len(word):
            if len(set(word) & set(input_words)) < max(len(set(word)), len(set(input_words)))-4:
                continue
            if len(word) < 3 or len(input_words) < 3:
                changes = levenshtein_algorithm(input_words, word)
            elif word[0] in input_words[0:3] or word[1] in input_words[0:3] or word[2] in input_words[0:3]:
                changes = levenshtein_algorithm(input_words, word)
            else:
                changes = 100
            if changes < _min:
                _min = changes
                find_word = word
    return  find_word, _min


def levenshtein_algorithm(input_word, word) -> float:
    k_array = []
    keyboard = [["й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ",], ["ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э"], ["я", "ч", "с", "м", "и", "т", "ь", "б", "ю"]]
    replacement = [("и", "е"), ("а", "о"), ("д", "т"), ("з", "с"), ("г", "к"), ("б", "п"), ("в", "ф"), ("ж", "ш")]
    for i in range(len(input_word)+1):
        k_array.append([i] + [0] * len(word))
    for i in range(len(word)+1):
        k_array[0][i] = i
    for i in range(1, len(input_word)+1):
        for j in range(1, len(word)+1):
            k_insert = 1
            k_pop = 1
            if i == len(input_word) and input_word[i-1] in "смить":
                k_pop = 0.8
            k_equals = 1
            if input_word[i-1] == word[j-1]:
                k_equals = 0
            elif (input_word[i-1], word[j-1]) in replacement or (word[j-1], input_word[i-1]) in replacement:
                k_equals = 0.2
            else:
                i_word = 0
                j_word = 0
                for _i in range(3):
                    if word[j-1] in keyboard[_i]:
                        i_word = _i
                        j_word = keyboard[_i].index(word[j-1])
                for _i in range(3):
                    for _j in range(1, 3):
                        try:
                            if keyboard[i_word+1-_i][j_word+1-_j] == input_word[i]:
                                k_equals = 0.8
                                break
                        except:
                            continue
            k = min(k_array[i][j-1]+k_pop, k_array[i-1][j]+1, k_array[i-1][j-1]+k_equals)
            if k > 30 and i == j:
                return 100
            else:
                k_array[i][j] = k
    distance = k_array[-1][-1]
    length_diff = abs(len(input_word)-len(word))
    normalized_distance = distance + length_diff * 0.5
    prefix_len = 0
    for i in range(min(len(input_word), len(word))):
        if input_word[i] == word[i]:
            prefix_len += 1
        else:
            break
    prefix_bonus = 0
    # Бонус зависит от доли совпадающего префикса относительно длины входного слова
    if len(input_word) > 0:
        prefix_bonus += (prefix_len / len(input_word)) * 2.5
    # Дополнительный штраф, если слово короче входного
    if len(word) < len(input_word):
        normalized_distance += 1.0  # Штраф за слишком короткое слово
    normalized_distance = max(0, normalized_distance - prefix_bonus)
    return normalized_distance

def clearing_input(_input: str):
    punctuation_marks = ".,/?!*\"_+&=-\\\n"
    _input.strip()
    _input = _input.lower()
    _input = ' '.join((_input.split()))
    _input = _input.split(" ")
    clean_input = len(_input) * ["_"]
    i = 0
    while i < len(_input):
        double_min = 100
        if _input[i] == "_":
            i += 1
            continue
        if _input[i][-1] in punctuation_marks:
            _input.insert(i+1, _input[i][-1])
            clean_input.insert(i+1, _input[i][-1])
            _input[i] = _input[i][:-1]
            _input[i+1] = "_"
            continue
        if len(_input) - i > 1 and len(_input[i+1]) > 2 and len(_input[i]) > 2:
            double_input_word, double_min = filter_dictionary("".join([_input[i], _input[i+1]]))
        input_word, _min = filter_dictionary(_input[i])
        if _min <= 30 and _min < double_min:
            _input[i], clean_input[i] = "_", input_word
            i += 1
            continue
        elif double_min <= 30:
            _input[i], clean_input[i] = "_", double_input_word
            _input.pop(i+1)
            clean_input.pop(i+1)
            i += 1
            continue

        print("Ошибка")
        break
    return clean_input

def transfer_to_token(_input: list[str]) -> list[int]:
    token_input = []
    vocab = MorphVocab()
    for i in range(len(_input)):
        normal_forms = vocab.normal_forms(_input[i])[0]
        if normal_forms in token_dataset:
            token_input.append(token_dataset.index(normal_forms)+1)
        else:
            token_input.append(0)
    return token_input

dictionary = get_dictionary_dataset()
token_dataset = get_token_dataset()

x_train, y_train = get_data("training.txt")
x_test, y_test = get_data("test.txt")

for i in range(len(x_train)):
    print(i, x_train[i])
    x_train[i] = clearing_input(x_train[i])
    print(i, y_train[i])
    y_train[i] = clearing_input(y_train[i])
    print()
# w = "нем"
# m = MorphVocab()
# p = m(w)
# l = m.normal_forms(w)
# print(l)
# print(clearing_input("приветсвую"))
# s = "Привет. Хачу уточнить, есть ли у вас"
# clean_input = clearing_input(s)
# token_input = transfer_to_token(clean_input)
# print(token_input)

