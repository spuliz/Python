# Write a Python program to play the game Hangman. The user needs to guess a secret word
# by guessing its letters.

print("Welcome to the Hangman game!")

secret_word = ['D','U','B','L','I','N']
blanks = '_' * len(secret_word)
mistakes = 0
while True:
    letter = input("Enter an uppercase letter ")
    mistakes += 1
    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            new_word = blanks[:i] + secret_word[i] + blanks[i+1:]
            blanks = new_word
    if mistakes == 10:
            print("Game Over")
            break
    if list(blanks) == secret_word:
        print("You won Sanja!!!!!!!!!!!!")
        break
    print(blanks)

