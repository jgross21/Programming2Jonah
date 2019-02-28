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
word_list = ['Bears',  'Vikings', 'Lions', 'Packers', 'Falcons', 'Panthers', 'Saints', 'Buccaneers', 'Eagles', 'Cowboys', 'Redskins', '49ers', 'Seahawks', 'Rams', 'Cardinals', 'Jaguars', 'Colts', 'Texans', 'Titans', 'Patriots', 'Dolphins', 'Jets', 'Bills', 'Giants', 'Browns', 'Ravens', 'Steelers', 'Bengals', 'Broncos', 'Raiders', 'Chargers', 'Chiefs', 'Yankees', 'Phillies', 'Redsox', 'Dodgers', 'Cubs', 'Mets', 'Padres', 'Braves', 'Cardinals', 'Astros', 'Bluejays', 'Whitesox', 'Angels', 'Mariners', 'Brewers', 'Reds', 'Tigers', 'Indians', 'Orioles', 'Twins', 'Athletics', 'Nationals', 'Pirates', 'Rangers', 'Marlins', 'Rays', 'Diamondbacks', 'Rockies', 'Royals']

print('Welcome to NFL/MLB hangman! All words are NFL/MLB teams')

done = False
used_letters = []
word = word_list.pop(random.randrange(len(word_list)))
chosen = word.upper()
pic_num = 0
correct = 0

while done == False:
    print(pic[pic_num])
    print('Used letters:', end=' ')
    for i in used_letters:
        print(i, end=' ')
    print()
    print()
    for letter in chosen:
        if letter in used_letters:
            print(end=letter + ' ')
        else:
            print(end="_ ")
    print()
    print()
    q = input('Pick a letter: ')
    user_letter = q.upper()
    used_letters.append(user_letter)
    if used_letters.count(user_letter) >= 2:
        user_letter = used_letters.pop()
        print('You already used that letter')
        correct -= 1
        if user_letter not in chosen:
            pic_num -= 1
    if user_letter not in chosen:
        pic_num += 1
    elif user_letter in chosen:
        for i in range (chosen.count(user_letter)):
            correct += 1
    if pic_num == 6:
        print(pic[6])
        #done = True
        print('You Lose!')
        ask = input("Do you want to play again?")
        if ask.upper() == 'NO':
            done = True
        if ask.upper() == 'YES':
            print('Welcome to NFL/MLB hangman! All words are NFL/MLB tams')
            done = False
            used_letters = []
            word = word_list.pop(random.randrange(len(word_list)))
            chosen = word.upper()
            pic_num = 0
            correct = 0
        else:
            print('That\'s not an answer, so I guess you\'re done!')
    if correct == len(chosen):
        for letter in chosen:
            print(letter, end=' ')
        #done = True
        print()
        print()
        print('You win!')
        ask = input("Do you want to play again?")
        if ask.upper() == 'NO':
            done = True
        if ask.upper() == 'YES':
            print('Welcome to NFL/MLB hangman! All words are NFL/MLB tams')
            done = False
            used_letters = []
            word = word_list.pop(random.randrange(len(word_list)))
            chosen = word.upper()
            pic_num = 0
            correct = 0
        else:
            print('That\'s not an answer, so I guess you\'re done!')