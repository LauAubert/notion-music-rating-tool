import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import os
import config


client_credentials_manager = SpotifyClientCredentials(
    client_id=config.SPOTIFY_CLIENT_ID, 
    client_secret=config.SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_songs_info(id_list):
    song_list = []
    for song_id in id_list:
        song_info = sp.track(song_id)
        secs = int(song_info["duration_ms"] / 1000)
        mins = int(secs / 60)
        secs = f"{secs % 60}"
        while len(secs)<2:secs = "0"+ f"{secs}"
        
        song_dict = {
        "title": song_info["name"],
        "duration": f"{mins}:{secs}"
        }
        song_list.append(song_dict)

    return song_list


def get_album_info(album_url):
    album_id = album_url.split("/")[-1]
    if "?" in album_id:
        album_id = album_id.split("?")[0]
    album_info = sp.album(album_id)

    album_data = {
        "title": album_info["name"],
        "year": album_info["release_date"][:4],
        "cover_url": album_info["images"][0]["url"],
        "tracks": get_songs_info([track["id"] for track in album_info["tracks"]["items"]]),
        "band": album_info["artists"][0]["name"]
    }
    
    return album_data

# ----------------------------------------------------------------------------------------------------------------
# album_url = "https://open.spotify.com/album/6IYPmM3xsOPL2XPSvf1ZAz?si=Tpu53cj6TG-k1egnCo7v7A"

def send(album_data):
  response = requests.post(
    config.INTEGROMAT_URL, 
    json=album_data)
  # Verifica que la solicitud haya tenido éxito
  if response.status_code == 200:
        print("Solicitud enviada con éxito")
  else:
        print("Error al enviar la solicitud")
        print(response.status_code)
        print(response.text)
