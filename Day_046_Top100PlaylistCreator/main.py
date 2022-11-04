from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

### ==== SPOTIPY CLIENT ==== ###
SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]

scope="playlist-modify-public"
auth_manager = SpotifyOAuth(scope=scope, 
                            redirect_uri=SPOTIPY_REDIRECT_URI, 
                            client_id=SPOTIPY_CLIENT_ID, 
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            show_dialog=True,
                            cache_path="token.txt"
                            )

sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()["id"]

### ==== BILLBOARD SONG LIST AND URI LIST ==== ###

date = input('Which year do you want to travel to? Must in in format YYYY-MM-DD: ')  # Ask date
billboard = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/') # Request info from Billboard for date

soup = BeautifulSoup(billboard.text, 'html.parser') # Parse with Beautiful Soup
 
songlist = soup.select("li ul li h3")  # Get songlist from class hierarchy
song_names = [song.get_text(strip=True) for song in songlist]  # Get song names only

song_info = [sp.search(q='track:'+song, type='track') for song in song_names]  # Use spotipy to search for songs

new_playlist_name = f"Billboard {date} Top 100 Songs"
playlists = sp.user_playlists(user=user_id)

### === PLAYLIST CREATION === ###

old_playlists = [playlist['name'] for playlist in playlists['items']]

if new_playlist_name in old_playlists:
    print("Playlist already exists!")
else:
    sp.user_playlist_create(user=user_id, name=new_playlist_name, public=True)
    new_playlists = sp.user_playlists(user=user_id)
    playlist_id = new_playlists['items'][0]['id']
    
    song_uri = []  # Empty list for track URIs
    for song in song_info:
        try:  
            song_uri.append(song['tracks']['items'][0]['uri']) 
        except IndexError:  # Some songs may not exist, skip these
            continue 
    
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_uri)

# print(song_uri)
# print(song_uri[0])
# print(sp.track('spotify:track:7A0apkTSTvMbSI7yplcmlh')['name'])




