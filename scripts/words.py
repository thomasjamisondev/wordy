def get_words():
    words = []
    with open('words.txt') as words_file:
        for word in words_file:
            words.append(word)
    return words
