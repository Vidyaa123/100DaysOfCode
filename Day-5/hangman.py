import random
import hangman_art


def print_blank(word_to_guess_len, guessed_word):
    for i in range(word_to_guess_len):
        guessed_word.append('_')
    

#List of words to guess
words = ['alphabet','behaviour','calling', 'dinosaur','exciting']
guessed_word = []
print(hangman_art.logo)
#choose a random word from the list
word_to_guess = random.choice(words)
print(word_to_guess)
# replace letters with blanks
word_to_guess_len = len(word_to_guess)
print_blank(word_to_guess_len, guessed_word)

lives = 6
end_of_game=False

while "_" in guessed_word and end_of_game==False:
    guess = str(input("Guess a letter:- ").lower())
    if guess not in word_to_guess:
        print(hangman_art.stages[lives])
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lost")


    for position in range(word_to_guess_len):
        letter = word_to_guess[position]
        if letter == guess:
            guessed_word[position] = letter
    print(guessed_word)
        
if '_' not in guessed_word:
        end_of_game = True
        print("You WON")