import spotipy
from spotipy.oauth2 import SpotifyOAuth
from link_youtube import link

# Defina as credenciais do seu aplicativo

# 5iaqSc0YTY036I29JOHf8r
playlist_id = '5iaqSc0YTY036I29JOHf8r'  # coloque o id de sua playlist

def main_spotify():
    client_id = 'ef52b0328898445488c15ee290b6cbcf'
    client_secret = '86f9e23d785641eabd6053fa6db22966'
    redirect_uri = 'https://open.spotify.com/playlist/0hWWlQYFl0EYijcPtzKlrc?si=56d45e51c0784dc2&nd=1'  # Redirecione para este URL após a autorização

    # Inicialize o objeto Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read'))

    # Obtenha informações sobre a playlist
    playlist = sp.playlist(playlist_id)

    # Percorra as faixas da playlist e obtenha os nomes das músicas e artistas
    for track in playlist['tracks']['items']:
        track_name = track['track']['name']
        artists = [artist['name'] for artist in track['track']['artists']]
        
        # Combine o nome da música e os nomes dos artistas
        artist_names = ', '.join(artists)
        
        link(f"{track_name} - {artist_names}", track_name)