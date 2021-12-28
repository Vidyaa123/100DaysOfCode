import random

def print_filled_blank(guessed_word):
    for i in guessed_word:
        print(i,end='')

#List of words to guess
words = ['alphabet','behaviour','calling', 'dinosaur','exciting']
guessed_word = []
#choose a random word from the list
word_to_guess = random.choice(words)
print(word_to_guess)
# replace letters with blanks
word_to_guess_len = len(word_to_guess)-1
for i in range(word_to_guess_len):
    guessed_word.append('_')

print(guessed_word)   
while guessed_word == "_":
    guess = str(input("Guess a letter:- ").lower())
    for position in range(word_to_guess_len):
        letter = word_to_guess[position]
        if letter == guess:
            guessed_word[position] = letter

    print(guessed_word)
        
