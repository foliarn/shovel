from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
# Charger les variables d'environnement
load_dotenv()

scope = (
    "user-library-read "          # likes
    "playlist-read-private "      # playlists
    "playlist-modify-private "    # créer/ajouter à des playlists
    "user-top-read "              # stats
    "user-read-recently-played"  # historique
)

sp = Spotify(auth_manager=SpotifyOAuth(
    scope=scope
))

# Prints users' playlists, asks what playlist to choose then returns the selected playlists' id
def fetch_playlist():
    playlists = sp.current_user_playlists()
    i = 1

    for item in playlists['items']:
        playlist_name = item['name']
        print(f"{i}. {playlist_name}")
        i += 1

    choice = int(input("Choose a playlist (enter its number)")) - 1
    return(playlists['items'][choice]['id']) # Return the selected playlist's id
