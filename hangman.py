'''
Make a text based version of hangman (25pts)
Use the sample run as an example.  Try to make it as close as possible to the example. (or better)
'''

# PSEUDOCODE
# make a word list for your game
# grab a random word from your list and store it as a variable
# display the hangman
# display the used letters
# display the length of the word to the user using blank spaces
# prompt the user to guess a letter
# if the guess is correct increment correct_guesses by 1
# if the guess is incorrect increment incorrect_guesses by 1 and draw the next part of the hangman
# don't allow the user to select the same letter twice
# if the incorrect_guesses is greater than 6, tell the user they lost and exit the program
# if correct_guesses is equal to the length of the word, tell the user they won
# ask if they want to play again


# Feel free to use this list of ascii art for your game
import random

pic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ['Goatfish',  'homeomorphic', 'whiggism', 'lumpily', 'calico', 'Unmaledictive', 'headnote', 'dragon', 'pickwick', 'assad', 'Garnishment', 'prebreathing', 'streamline', 'revers', 'righteous', 'Hyperhypocrisy', 'advantage', 'jingler', 'procne', 'tellurium', 'Socket', 'spencer', 'moly', 'propagandized', 'fantasy']

print('Welcome to hangman!')

done = False
wrong_letters = []
wrong_letters_num = [len(wrong_letters)]
word = word_list.pop(random.randrange(len(word_list)))
chosen = word.upper()
pic_num = 0



while done == False:
    print(pic[pic_num])
    print('Used letters:', end=' ')
    for i in wrong_letters:
        print(i, end=' ')
    print()
    for i in range (len(chosen)):
        print(end='_ ')
    print()
    print()
    q = input('Pick a letter: ')
    user_letter = q.upper()
    if user_letter not in chosen:
        wrong_letters.append(user_letter)
        pic_num += 1
















