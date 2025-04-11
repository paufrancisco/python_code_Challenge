input_word = input("Enter a word: ")

char_list = list(input_word)

reversed_word = ""

length_input_word = len(char_list)

for i in range(length_input_word-1,-1,-1):
    reversed_word += char_list[i]

if input_word == reversed_word:
    print("palindrome")
else:
    print("not palindrome")

