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
