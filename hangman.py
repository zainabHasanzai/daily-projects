# zainab
import random
words = ["python", "game", "zainab", "hello"]
word = random.choice(words)
guessed = []
tries = 6
print("The word has", len(word), "letters")

while tries > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        print("You won")
        break
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Enter only one letter")
        continue

    if guess in guessed:
        print("You already guessed that!")
        continue
    guessed.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong")
        print("tries left:", tries)

    

if tries == 0:
    print("You lost the word was:", word)
    