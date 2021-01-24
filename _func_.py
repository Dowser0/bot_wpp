import requests
import dicionario_de_moedas
#import matplotlib.pyplot as plt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from pytube import YouTube,Playlist
import os
#from googleapi import google
from googlesearch import search
#from bs4 import BeautifulSoup


imagem = "C:/Users/gabri/Documents/bot_wpp/figura.png"

dicionario_moedas = dicionario_de_moedas.dicionario_moedas()

motorista = webdriver.Chrome(ChromeDriverManager().install())

motorista.get('https://web.whatsapp.com')

def buscar_contato(contato):

    campo_pesquisa = motorista.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')

    campo_pesquisa[0].click()

    campo_pesquisa[0].send_keys(contato)

    campo_pesquisa[0].send_keys(Keys.ENTER)

def ler_ultima_mensagem():

    caixa_de_mensagem =  motorista.find_elements_by_xpath('//span[contains(@class,"selectable-text invisible-space copyable-text")]')

    ultima_mensagem = caixa_de_mensagem[-1].text

    return ultima_mensagem

def enviar_mensagem(mensagem):

    mensagem = str(mensagem)

    campo_mensagem = motorista.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')

    campo_mensagem[1].click()

    campo_mensagem[1].send_keys(mensagem)

    campo_mensagem[1].send_keys(Keys.ENTER)

def enviar_midia(midia):

    motorista.find_element_by_xpath ('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span').click()

    time.sleep(0.5)

    motorista.find_element_by_xpath("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']").send_keys(midia)

    time.sleep(3)

    campo_de_envio = motorista.find_elements_by_xpath('//div[contains(@class,"q2PP6 _3Git-")]')

    campo_de_envio[0].click()

#def _request_atual(nome_da_moeda):
    #Request money
#    r_get = requests.get('https://economia.awesomeapi.com.br/json/all/'+nome_da_moeda)
#    if r_get.status_code == 200:
#        return r_get.json()
#    else:
#        r_get.status_code

#def _request_dias(nome_da_moeda,dias):
#    #Requset money
#    r_get = requests.get('https://economia.awesomeapi.com.br/json/daily/'+nome_da_moeda+'/'+dias)
#    if r_get.status_code == 200:
#        return r_get.json()
#    else:
#        r_get.status_code

#def request_valor_atual(nome_da_moeda):
#    nome_da_moeda = nome_da_moeda.upper()
#    if nome_da_moeda in dicionario_moedas:
#        r_1 = _request_atual(dicionario_moedas[nome_da_moeda][0])
#        parametro_da_moeda = dicionario_moedas[nome_da_moeda][1]
#        valor = float(r_1[parametro_da_moeda]['bid'])
#        return [valor,nome_da_moeda]
#    else:
#        None

#def historico_de_valor_de_uma_moeda(nome_do_dinheiro,dias):
#    r_1 = _request_dias(nome_do_dinheiro,dias)
#    lista_de_valores = []
#    lista_de_dias = []
#    contador = 1

#    for i in range(0,int(dias)):
#        resposta_bid = r_1[i]['bid']
        #resposta_date = r[i]['timestamp']
        #resposta_date_convert = datetime.datetime.fromtimestamp(int(resposta_date))
#        lista_de_valores.append(float(resposta_bid))
#        lista_de_dias.append(contador)
#        contador +=1

#    return [lista_de_dias,lista_de_valores]


#def separa_moeda_e_dias(nome_da_moeda_com_dias):
#    lista_moeda_dias = nome_da_moeda_com_dias.split('-')
#    if isinstance(lista_moeda_dias,list):
#        return lista_moeda_dias
#    else:
#        return None

#def gera_grafico(nome_da_moeda,lista_de_dias,lista_de_valores):
#    plt.clf()
#    plt.title(nome_da_moeda)
#    plt.xlabel('Dias atrás')
#    plt.ylabel('Preço de venda') 

#    plt.scatter(lista_de_dias,lista_de_valores)
#    plt.plot(lista_de_dias,lista_de_valores)
    #plt.legend()

#    plt.savefig('figura.png')
#    return 'figura.png'

def download_youtube(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True)[0]
    music = audio.download()
    os.rename(music,music[:-4]+'.mp3')
    return music[:-4]+'.mp3'
    

def download_playlist_envia(url_):                                                  
    playlist = Playlist(url_)
    for url in playlist:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True)[0]
        music = audio.download()
        os.rename(music,music[:-4]+'.mp3')
        enviar_midia(music[:-4]+'.mp3')
        deleta_arquivo(music[:-4]+'.mp3')
        time.sleep(1)
    
def deleta_arquivo(arquivo):
    os.remove(arquivo)

def request_pesquisa(pesquisa):
    resultados = search(pesquisa+ 'youtube', num_results=10)
    for link in resultados:
        if link.startswith('https://www.youtube.com/'):
            return link