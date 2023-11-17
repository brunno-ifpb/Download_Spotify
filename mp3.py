from pytube import YouTube
from moviepy.editor import VideoFileClip
import time


# URL do vídeo do YouTube
# Caminho Videos
# Caminho Musica
local_pasta_videos = "music/videos"  # coloque o caminho da pasta onde deve ir os videos
local_pasta_musicas = "music/musicas" # coloque o caminho da pasta onde deve ir as musicas

import os
if not os.path.exists(f'{local_pasta_videos}'):  # coloque o caminho da pasta onde deve ir os videos
    os.makedirs(f'{local_pasta_videos}')

if not os.path.exists(f'{local_pasta_musicas}'): # coloque o caminho da pasta onde deve ir as musicas
    os.makedirs(f'{local_pasta_musicas}')

def url(url_video, name):
    a = time.time()
    video_url = f'{url_video}'

    # Defina o local para salvar o vídeo
    save_path = f'{local_pasta_videos}/{name}'
    

    # Crie um objeto YouTube
    yt = YouTube(video_url)

    # Selecione a melhor qualidade de vídeo disponível
    ys = yt.streams.get_highest_resolution()

    # Verifique se o diretório de saída existe ou crie-o, se necessário
    

    # Baixe o vídeo
    ys.download(output_path=save_path)

    downloaded_file_name = os.listdir(save_path)

    # Converta o vídeo para MP3
    video = VideoFileClip(f"{save_path}/{downloaded_file_name[0]}")
    audio = video.audio
    audio.write_audiofile(f'{local_pasta_musicas}/{name}.mp3')

    

    # Limpeza: exclua o arquivo de vídeo original
    video.close()
    audio.close()
  # tem que dar permição para apagar arquivo

    print(f'Download de {name} concluídos com sucesso!')
    print(time.time() - a)



