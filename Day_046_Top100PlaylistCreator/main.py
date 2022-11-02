from bs4 import BeautifulSoup
import requests

date = input('Which year do you want to travel to? Must in in format YYYY-MM-DD: ')

billboard = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')

soup = BeautifulSoup(billboard.text, 'html.parser')

songlist = soup.find_all(class_="o-chart-results-list-row-container")
print(songlist)