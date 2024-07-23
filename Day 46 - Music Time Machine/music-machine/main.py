from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import requests
import spotipy
import os

load_dotenv()
date = input("Which date do you want to travel to (YYYY-MM-DD)? ")
link = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")

musics = [music.getText().strip() for music in soup.select("li ul li h3")]
print(musics)

with open("musics.txt", "w") as file:
    for title in musics:
        file.write(f"{title}\n")

# ------------------------------ Spotify ------------------------------

# authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
        username=os.environ["USERNAME"]
    )
)
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]

# searching songs by title
for song in musics:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# adding the new songs into the playlist created
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
