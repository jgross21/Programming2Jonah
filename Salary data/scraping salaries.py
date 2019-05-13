from bs4 import BeautifulSoup
import requests

url = 'https://www.spotrac.com/nfl/philadelphia-eagles/cap/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
twenty_ninteen_eagles_caphits = soup.findAll(title= 'Cap Hit')
eagles_player_names = soup.findAll(class_= 'player')


for i in range(1, int(eagles_player_names[0].text[16:18])):
    print(twenty_ninteen_eagles_caphits[i].text)
    print(eagles_player_names[i].text)

#for i in range(int(eagles_player_names[0].text[16:18])):
