word = input("Enter a word: ")

number_of_vowels = 0

char_word = list(word)

for i in range(len(char_word)):
    if char_word[i].__contains__("a") or char_word[i].__contains__("e") or char_word[i].__contains__("i") or char_word[i].__contains__("o") or char_word[i].__contains__("u"):  
        number_of_vowels +=1
        
print(f"Number of vowels: {number_of_vowels}")