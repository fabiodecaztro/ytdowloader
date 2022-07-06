import pytube
from pytube import exceptions as error

import os

os.system('cls')


validador = True
try:
    url = input('Coloque a URL: ')
    # caminho_processado = pytube.YouTube(url).streams.get_highest_resolution()
    caminho_processado = pytube.YouTube(url).streams.filter(only_audio=True)
    # print(f'Vídeo solicitado: {pytube.YouTube.title}')
except error.VideoUnavailable:
    print(f'Esta URL ({url}) não foi localizada')
    validador = False
except error.RegexMatchError:
    print(f'Esta URL ({url}) não foi localizada')
    validador=False

if validador:
    path = input('Coloque o local de salvamento: ')
# print(f'Video copiado para: {caminho_processado.download(path)}')
print(f'Video copiado para: {caminho_processado. download(path)}')

# C:\Users\fabio\Downloads