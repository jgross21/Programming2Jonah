#LISTS (29PTS TOTAL)
#In these exercises you should should use functions as needed.  All functions should have comments to describe their purpose.



# PROBLEM 1 (Using List Comprehensions - 6pts)
# Use the list comprehension method to do the following:
# a) Make a list of numbers from 1 to 100
# b) Make a list of even numbers from 20 to 40
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
import random
# a)
my_list = []
for i in range(1, 101):
    my_list.append(i)
print(my_list)

# b)
my_list = []
for i in range (20, 41):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)

# c)
my_list = []
for i in range (1, 101):
    my_list.append(i ** 2)
print(my_list)

#PROBLEM 2 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don't \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

def magic_8_ball():
    answer = input('Ask me a yes or no question: ')
    print(answer_list[random.randrange(len(answer_list))])
magic_8_ball()
# PROBLEM 3 (Shuffle - 8pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order. Print the random deck. 
# Then deal yourself a hand of 5 cards off the top.  Print the hand.  Print the remaining deck.

suits = [' of spades', ' of clubs', ' of diamonds', ' of hearts']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
deck = []
for i in suits:
    for j in values:
        deck.append(j + i)

def shuffle(deck):
    new_deck = []
    while len(deck)> 0:
        card = deck.pop(random.randrange(len(deck)))
        new_deck.append(card)
    return new_deck
new_deck = shuffle(deck)

print(new_deck)
print(new_deck[0:5])

# PROBLEM 4 (Illinois Pick 4 - 10pts)
# Lotteries are known to give awful odds of winning, and incredibly low expected returns on your invevestment.
# You will buy 10000 Illinois Pick 4 tickets in a simulation.
# Make a 2d lists of your picks.  Each number is a random 0 to 9.
# After you have made a list of 10000 lists (each 4 long), you will draw the official numbers
# After drawing the official numbers, you will go back through your list and check to see how many wins you got.
# The numbers must be an exact match in the exact position.
# Each ticket is $1.  If you win, you get $5000.  Simulate spending $10,000 on Pick 4 tickets, and see your return.

my_picks = []
draw_num = 10000
for i in range(draw_num):
    spot_1 = str(random.randrange(10))
    spot_2 = str(random.randrange(10))
    spot_3 = str(random.randrange(10))
    spot_4 = str(random.randrange(10))
    little_list = []
    little_list.append(spot_1 + spot_2 + spot_3 + spot_4)
    my_picks.append(little_list)

real_num = []
spot_1 = str(random.randrange(10))
spot_2 = str(random.randrange(10))
spot_3 = str(random.randrange(10))
spot_4 = str(random.randrange(10))
real_num.append(spot_1 + spot_2 + spot_3 + spot_4)

profit = -draw_num
prize = 5000
for i in my_picks:
    if real_num == i:
        profit += prize
print(profit)
