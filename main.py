from pprint import pprint
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

header = { "USER-AGENT": "	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/138.0.0.0 Safari/537.36"}
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
USERNAME = os.getenv("USERNAME")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=USERNAME))

user_id = sp.current_user()["id"]
# print(user_id)

date = input("Which year you would like to go? Please write in YYYY-MM-DD format: ")

URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
all_songs = soup.select("li ul li h3")

song_titles = [song.getText().strip() for song in all_songs]

songs = song_titles
with open("song.txt", mode="w", encoding="utf-8") as file:
    for song in songs:
        file.write(f"{song}\n")

song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pprint(f"{song} is skipped because it doesn't exist on Spotify.")

playlist = sp.user_playlist_create(user=user_id, name=f"Billboard 100 of {date}", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
