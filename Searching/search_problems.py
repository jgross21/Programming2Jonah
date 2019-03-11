'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

# This function takes in a line of text and returns
# a list of words in the line.
import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary = open('dictionary.txt')

word_list = []

for line in dictionary:
    line = line.strip()
    words = split_line(line)
    for word in words:
        word_list.append(word)

word_lens_list = []
for word in word_list:
    word_lens = len(word)
    word_lens_list.append(word_lens)

highest = max(word_lens_list)
spot = word_lens_list.index(highest)

print(word_list[spot])
#2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

alice_story = open('AliceInWonderLand.txt')

alice_word_list = []
for line in alice_story:
    line = line.strip()
    words = split_line(line)
    for word in words:
        alice_word_list.append(word)

total_chars = 0
total_words = len(alice_word_list)
for word in alice_word_list:
    length = len(word)
    total_chars += length
    avg = total_chars/total_words
print(avg)

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?


#### OR #####

#3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"
seven = []
for i in alice_word_list:
    if len(i) == 6:
        seven.append(i)
seven_counts = []
for i in seven:
    seven_counts.append(seven.count(i))

most = seven[seven_counts.index(max(seven_counts))]
print(most)
# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



