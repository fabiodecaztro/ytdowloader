from webbrowser import get
from pytube import exceptions as error
import pytube
import os


os.system('cls')

pesquisar = pytube




local = input(
    'Local de armazenamento (deixe sem para salvar na pasta do projeto): ')

pronto_para_download.download(local)


class DownloadYouTube:
    def __init__(self) -> None:
        pass

    def url_yt(self):
        url = input('Digite a URL: ')
        try:
            video_localizado = pesquisar.YouTube(url)
            if video_localizado:
                print(f'Video selecionado: {video_localizado.title}')
        except error.VideoUnavailable:
            print('Vídeo não localizado')
    
    def formato_download(self):
        formato = input('Qual o formato\n[1] WEBM - [2] MP4: ')
        if formato == '1':
            video_localizado.streams.filter(only_audio=True)
            pronto_para_download = video_localizado.streams.get_by_itag(250)
        elif formato == '2':
            pronto_para_download = video_localizado.streams.get_highest_resolution()
        else:
            print('Formato Invalido')

