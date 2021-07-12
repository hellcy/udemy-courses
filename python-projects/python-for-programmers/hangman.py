def game_setup():
    lives = 3
    word = "apple"

    newgame(lives, word)


def temp_ans(guessed_letters, word):
    ans = ''
    for char in word:
        if char in guessed_letters:
            ans += char
        else:
            ans += '_'
    return ans


def scoreboard(guessed_letters, lives):
    print("You have {} lives now".format(lives))
    if len(guessed_letters) > 0:
        print("You have guessed these letters: ", end="")
        for letter in guessed_letters:
            print(letter, end=" ")
        print("")


def validation(guess, guessed_letters):
    guess = guess.lower()

    while len(guess) > 1:
        guess = input("Your letter cannot be longer than 1 character: ")

    while guess in guessed_letters:
        guess = input(
            "You have already guessed this letter, please guess a different letter: ")
        guess = guess.lower()


def newgame(lives, word):
    word = word.lower()
    guessed_letters = set()

    temp = ''
    for char in word:
        temp += '_'
    print(temp)

    while lives > 0:
        scoreboard(guessed_letters, lives)
        guess = input("Please guess a letter: ")

        validation(guess, guessed_letters)

        guessed_letters.add(guess)
        if guess in word:
            temp = temp_ans(guessed_letters, word)
            print("Corrent! This word now looks like: {}".format(temp))
            if temp.find('_') == -1:
                break
        else:
            lives -= 1

    if lives > 0:
        print("You won!")
    else:
        print("You lost!")


game_setup()
