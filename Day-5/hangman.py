import random
#List of words to guess
words = ['alphabet','behaviour','calling', 'dinosaur','exciting']
guessed_word = []
#choose a random word from the list
word_to_guess = random.choice(words)
# replace letters with blanks
word_to_guess_len = len(word_to_guess)-1
for i in range(word_to_guess_len):
    guessed_word.append('_')
    print(guessed_word,end='', sep='')


