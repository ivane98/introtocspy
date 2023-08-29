def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    printStr = ""
    for char in secret_word:
        if char in letters_guessed:
            printStr += char
        else:
            printStr += "_ "
    return printStr


def hangman(secret_word):
    guesses = 6
    lettersGuessed = []

    print('secret word contains', len(secret_word), 'letters')

    while guesses:
        print(guesses, "guesses left.")
        print('letters left to guess', len(secret_word) - len(lettersGuessed))
        guess = str.lower(input("Please guess a letter: "))

        if guess in secret_word:
            print("Good guess:")
            lettersGuessed.append(guess)
            print(get_guessed_word(secret_word, lettersGuessed))
        else:
            print("Oops! That letter is not in my word:")
            print(get_guessed_word(secret_word, lettersGuessed))
            guesses -= 1

        if len(lettersGuessed) == len(secret_word):
            print('you have won')
            return

    print("Sorry, you ran out of guesses. The word was " + secret_word + ".")


print(hangman('cat'))
