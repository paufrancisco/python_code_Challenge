def freq_words():
    input_str = input("Enter a sentence: ")
    list_words = input_str.split()  # split the sentence into words
    dictionary = {}  # container for the stored words

    for i in list_words:
        if i not in dictionary:
            dictionary[i] = 0  # check if the word exists else equate to 0
        dictionary[i] += 1  # if exists add 1 so that we can count the freq of words
    print(dictionary)


freq_words()
