# Scraping with Beautiful Soup

from bs4 import BeautifulSoup
import requests

url = 'http://quotes.toscrape.com'

page = requests.get(url)
print(page)
# print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())

#findAll function to grab a list
# search for tagnames, attributes(kwargs), css class, text strings

titles = soup.findAll(name='title')
print(titles[0]) # just the tag
print(titles[0].text) # text inside the tag

# By attribute
keywords = soup.findAll(itemprop='keywords')
for word in keywords:
    print(word)

print('\n' * 10)
# By CSS class
quotes = soup.findAll(class_='quote')
for quote in quotes:
    print(quote)

print('\n' * 10)
print(quotes[0].prettify)

# By Combinations
quotes = soup.findAll('span', class_='text')

print('\n' * 10)

for quote in quotes:
    print(quote.text)


quote_list = [x.text for x in quotes]
print(quote_list)

# By text
einsteins = soup.findAll(text='Albert Einstein')
for e in einsteins:
    print(e)

# By authors
authors = soup.findAll('small', class_= 'author')
print(authors[0].text)
authors_list = [x.text.strip() for x in authors]

# print all quotes
for i in range(len(quote_list)):
    print()
    print(quote_list[i])
    print('\t', authors_list[i])