import pyautogui
import asyncio
from time import sleep
from pytube import YouTube,Playlist
import os
#abrir = pyautogui.confirm(text='Iniciar programa?', buttons=['Iniciar', 'Fechar'])
#icon_pos = pyautogui.locateOnScreen('figura.png')
#
#if abrir == 'Fechar' or abrir == None:
#   run = False
#if abrir == 'Iniciar':
#    run = True

#while run:
 #   if icon_pos :
  #      pyautogui.click(icon_pos[0],icon_pos[1]),pyautogui.click(icon_pos[0],icon_pos[1]),pyautogui.click(icon_pos[0],icon_pos[1])
#        print("este elemento existe na tela")
 #       run = False








    #else:
    #    print("este elemento nao existe na tela")
    #    run = False
#def download_playlist(url):
#    playlist = Playlist(url)
#    lista_download = []
#    for url in playlist:
#        yt = YouTube(url)
#        audio = yt.streams.filter(only_audio=True)[0]
#        music = audio.download()
#        os.rename(music,music[:-4]+'.mp3')
#        lista_download.append(music[:-4]+'.mp3')
#    return lista_download
#from pytube import YouTube

#VIDEO_URL = 'https://www.youtube.com/watch?v=-CrD1n1loXs&ab_channel=Djonga'
#yt = YouTube(VIDEO_URL)
#audio = yt.streams.filter(only_audio=True)[0]
#audio.download()
#from googlesearch import search

#pesquisa = 'anitta prepara'
#pesquisa = pesquisa + ' youtube'
#print(pesquisa)

#z = search(pesquisa, num_results=2)

#print(z)

#from google import search

#for resultado in search('"seila" youtube', stop=10):
#    print (resultado)

from bs4 import BeautifulSoup

import requests

#html = requests.get("https://rankedboost.com/league-of-legends/build/yasuo/").content

#soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

#elemento1 = soup.find_all("div", class_="rb-build-rune-text keystone-rb-text")
#elemento2 = soup.find_all("div", class_="rb-build-rune-text")
##lista_de_runas = []
#print(elemento1[0].string)
#for z in range(len(elemento2)):
##  lista_de_runas.append(elemento2[z].string)

###print(lista_de_runas)

#print(elemento2[1:].string)





#def request_counter(campeao):
#    html = requests.get("https://rankedboost.com/league-of-legends/build/"+campeao+"/").content
#    soup = BeautifulSoup(html, 'html.parser')
#    elemento1 = soup.find_all("span", class_="counters-sidebar-champ-name")
#    counters = []
#    for z in range(len(elemento1)):
#        counters.append(elemento1[z].string)
#    return counters
#z= request_counter('zed')
#print(z)
#from googleapi import google
#def request_pesquisa(pesquisa):
#    resultados = google.search(pesquisa+ ' youtube')
#    for z in range(len(resultados)):
#        pesquisa = [resultados[z].link,resultados[z].name]
#        if pesquisa[0].startswith('https://www.youtube.com/'):
#            return pesquisa

#z =  request_pesquisa('sidoka')
#print(z)
#for resultado in search('"legends never die" youtube', stop=10):
#  print(resultado)
from pytube import YouTube,Playlist
import os

#def download_youtube(url):
#    yt = YouTube(url)
#    audio = yt.streams.filter(only_audio=True)[0]
#    music = audio.download()
#    os.rename(music,music[:-4]+'.mp3')
#    return music[:-4]+'.mp3'

#z =  download_youtube('https://www.youtube.com/watch?v=B6_iQvaIjXw&ab_channel=ArianaGrandeVevo')

#print(z)

def download_playlist_envia(url_):                                                  
    playlist = Playlist(url_)
    print(playlist)
    for url in playlist:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True)[0]
        music = audio.download()
        os.rename(music,music[:-4]+'.mp3')
        
download_playlist_envia('https://youtube.com/playlist?list=PLEd-urvJlSm9PfBtTyK_IuslJstIBq7OF')





