import random

print("Let's play hangman")

#Predefined words and random picking of one
all_words= ["gray","wish","bone","found","heaven"]
word = random.choice(all_words)

word_length = len(word)
print("Word has",word_length,"letters")
display = ["_"] * word_length
guessed_letters = []
wrong = 0
max_wrong = 6


while wrong < max_wrong and "_" in display:

    print(" ".join(display))
    guess = input("Guess: ").lower()
    
    if guess in guessed_letters:
        print("Already guessed")
        continue

    guessed_letters.append(guess)
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess: 
                display[i] = guess
    else:
        wrong += 1
        guesses_left = max_wrong - wrong
        print("Incorrect.You have",guesses_left,"guesses left")

if "_" not in display:
    print("Good job. You got it!")
else:
    print("You lose.Word was",word)           