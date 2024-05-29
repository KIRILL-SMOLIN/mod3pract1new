  # Домашняя работа по уроку "Пространство имен и способы вызова функции"
def single_root_words(root_word, *other_words):
    same_words = list()
    root_word_l = root_word.lower()
    other_words_l = list()
    for i in range(len(other_words)):
        other_words_l.append(other_words[i].lower())

    for i in range(len(other_words)):
        if (root_word_l.find(other_words_l[i]) >= 0) or (other_words_l[i].find(root_word_l) >= 0):
            same_words.append(other_words[i])

    return same_words


result1 = single_root_words('Rich', 'richiest', 'Orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(*result1)
print(*result2)
