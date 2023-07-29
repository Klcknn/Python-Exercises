# 1. Method
""" 

def replace_world():
    main_word = "The world you are trying to connect to is already in use by another user."
    word_to_replace = input("Please enter a word to replace: ")
    word_to_replacement = input("Please enter a replacement: ")

    if word_to_replace.isalpha() == True and word_to_replace.isalpha()== True:
        result_word= main_word.replace(word_to_replace, word_to_replacement)
        print(result_word)
    else:
        print("Error..")

replace_world()
 
"""
""" 
# 2. Method

def replace_world(main_word):
    word_to_replace = input("Please enter a word to replace: ")
    word_to_replacement = input("Please enter a replacement: ")

    if word_to_replace.isalpha() == True and word_to_replace.isalpha()== True:
        result_word= main_word.replace(word_to_replace, word_to_replacement)
        print(result_word)
    else:
        print("Error..")

entered_word = "Feel The Heat With This Quiz On Worldwide Words For Summer And Winter"
replace_world(entered_word)

 """
# 3. Method

def replace_world(main_word):
    word_to_replace = input("Please enter a word to replace: ")
    word_to_replacement = input("Please enter a replacement: ")

    if word_to_replace.isalpha() == True and word_to_replace.isalpha()== True:
        result_word= main_word.replace(word_to_replace, word_to_replacement)
        print(result_word)
    else:
        print("Error..")

entered_word = input("Enter any of the following words: ")
replace_world(entered_word)
