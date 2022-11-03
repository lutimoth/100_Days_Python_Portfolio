from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']

scope="user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


# date = input('Which year do you want to travel to? Must in in format YYYY-MM-DD: ')

# billboard = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')

# soup = BeautifulSoup(billboard.text, 'html.parser')

# songlist = soup.select("li ul li h3")

# song_names = [song.get_text(strip=True) for song in songlist]
# print(song_names)