def count_words():
    user_input = input("Введите строку: ")
    words = user_input.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    for word, count in word_count.items():
        print(f"{word}: {count}")

count_words()
