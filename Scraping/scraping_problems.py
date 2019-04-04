# SCRAPING PROBLEM (12pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweets located on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

from bs4 import BeautifulSoup
import requests

url = 'https://twitter.com/BillSimmons?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

bs = soup.findAll(class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')


for i in range(5):
    print()
    print(bs[i].text)
