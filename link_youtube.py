import os
from googleapiclient.discovery import build
from mp3 import url

# AIzaSyCnNDGqkarGdrijCTf4onj606LPrkmQQmU YOUR_API_KEY
api_key = 'AIzaSyCnNDGqkarGdrijCTf4onj606LPrkmQQmU' # Substitua 'YOUR_API_KEY' pelo seu próprio chave de API

# Inicialize o serviço da API do YouTube
youtube = build('youtube', 'v3', developerKey=api_key)

# Nome da música para pesquisar

def link(name, name_music):
    nome_da_musica = f"{name} music" # como será pesquisado

    # Realize a pesquisa no YouTube 
    search_response = youtube.search().list(
        q=nome_da_musica,
        type='video',
        part='id',
        maxResults=1  # Número máximo de resultados (vídeos) a serem exibidos
o     ).execute()

    # Recupere o ID do vídeo do resultado da pesquisa
    video_id = search_response['items'][0]['id']['videoId']

    # Construa o link do vídeo do YouTube
    video_url = f'https://www.youtube.com/watch?v={video_id}'

    url(video_url, name_music)