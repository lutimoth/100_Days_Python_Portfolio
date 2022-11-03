from bs4 import BeautifulSoup
import requests

date = input('Which year do you want to travel to? Must in in format YYYY-MM-DD: ')

billboard = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')

soup = BeautifulSoup(billboard.text, 'html.parser')

songlist = soup.select("li ul li h3")

song_names = [song.get_text(strip=True) for song in songlist]
print(song_names)