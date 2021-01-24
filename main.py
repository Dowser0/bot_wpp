from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import _func_
#import dicionario_de_moedas
#import random


contato = ["Dowser Musicas"]
mensagem = 'top'
imagem = "C:/Users/gabri/Documents/bot_wpp/figura.png"
#dicionario_moedas = dicionario_de_moedas.dicionario_moedas()
run = True


time.sleep(10)
_func_.buscar_contato(contato)
time.sleep(0.5)

while run:
    try:

        ultima_mensagem = str(_func_.ler_ultima_mensagem())

#        if ultima_mensagem.lower().startswith('!money'):
#            nome_da_moeda = ultima_mensagem[6:]
#            valor_atual = _func_.request_valor_atual(nome_da_moeda)
#            valor_atual[0] = str(round(valor_atual[0], 2))
#            mensagem = valor_atual[1]+':R$'+valor_atual[0]
#            _func_.enviar_mensagem(mensagem)

#        if ultima_mensagem.lower().startswith('!mhistoric'):
#            nome_da_moeda = ultima_mensagem[10:]
#            moeda_com_dias = _func_.separa_moeda_e_dias(nome_da_moeda)
#            nome_da_moeda = moeda_com_dias[0].upper()
#            parametro_da_moeda = dicionario_moedas[nome_da_moeda][0]
#            dias = moeda_com_dias[1]
#            lista_historico_de_valores_e_dias = _func_.historico_de_valor_de_uma_moeda(parametro_da_moeda,dias)
#            lista_de_dias = lista_historico_de_valores_e_dias[0]
#            lista_de_valores = lista_historico_de_valores_e_dias[1]
#            _func_.gera_grafico(nome_da_moeda,lista_de_dias,lista_de_valores)
#            mensagem =  'seu gráfico :)'
#            _func_.enviar_mensagem(mensagem)
#            _func_.enviar_midia(imagem)

        if ultima_mensagem.lower().startswith('!md'):
            pesquisa = ultima_mensagem[3:]
            _func_.enviar_mensagem('Fazendo download de '+pesquisa)
            _func_.download_youtube(pesquisa)

        if ultima_mensagem.lower().startswith('!ms'):
            pesquisa = ultima_mensagem[3:]
            resultado = _func_.request_pesquisa(pesquisa)
            _func_.enviar_mensagem('Fazendo download de '+pesquisa)
            _func_.download_youtube(resultado)

        if ultima_mensagem.lower().startswith('!pd'):
            pesquisa = ultima_mensagem[3:]
            _func_.enviar_mensagem('Fazendo download de '+pesquisa)
            _func_.download_playlist_envia(pesquisa)

#        if ultima_mensagem.lower().startswith('!roll'):
#            num_sorteado = random.randint(1,6)
#            mensagem = num_sorteado
#            _func_.enviar_mensagem(mensagem)

#        if ultima_mensagem.lower().startswith('!rune'):
#            campeao = ultima_mensagem[5:]
#            runas = _func_.request_runas(campeao)
#            mensagem = '*'+runas[0]+'*\n'+runas[1]+'\n'+runas[2]+'\n'+runas[3]+'\n'+runas[4]+'\n*'+runas[5]+'*\n'+runas[6]+'\n'+runas[7]+'\n*'+runas[8]+'*\n*'+runas[9]+'*\n*'+runas[10]+'*\n'
#            _func_.enviar_mensagem(mensagem)

#        if ultima_mensagem.lower().startswith('!skill'):
#            campeao = ultima_mensagem[6:]
#            habilidade = _func_.request_habilidades(campeao)
#            mensagem = '*'+habilidade[0]+'* > *'+habilidade[1]+'* > *'+habilidade[2]+'*'
#            _func_.enviar_mensagem(mensagem)
        
#        if ultima_mensagem.lower().startswith('!build'):
#            campeao = ultima_mensagem[6:]
#            build = _func_.request_build(campeao)
#            mensagem = build[0]+'\n'+build[1]+'\n'+build[2]+'\n'+build[3]+'\n'+build[4]+'\n'+build[5]
#            _func_.enviar_mensagem(mensagem)

#        if ultima_mensagem.lower().startswith('!champ'):
#            campeao = ultima_mensagem[6:]
#            mensagem = '*'+runas[0]+'*\n'+runas[1]+'\n'+runas[2]+'\n'+runas[3]+'\n'+runas[4]+'\n*'+runas[5]+'*\n'+runas[6]+'\n'+runas[7]+'\n*'+runas[8]+'*\n*'+runas[9]+'*\n*'+runas[10]+'*\n'
#            _func_.enviar_mensagem(mensagem)
#            habilidade = _func_.request_habilidades(campeao)
#            mensagem = '*'+habilidade[0]+'* > *'+habilidade[1]+'* > *'+habilidade[2]+'*'
#            _func_.enviar_mensagem(mensagem)
#            build = _func_.request_build(campeao)
#            mensagem = build[0]+'\n'+build[1]+'\n'+build[2]+'\n'+build[3]+'\n'+build[4]+'\n'+build[5]
#            _func_.enviar_mensagem(mensagem)

#        if ultima_mensagem.lower().startswith('!counter'):
#            campeao = ultima_mensagem[8:]
#            counters = _func_.request_counter(campeao)
#            mensagem = '*Ban suggestions*\n'+counters[-1]+'\n'+counters[-2]+'\n'+counters[-3]+'\n*Counter picks*\n'+counters[-4]+'\n'+counters[-5]+'\n'+counters[-6]+'\n'
#            _func_.enviar_mensagem(mensagem)
        
        if ultima_mensagem.lower().startswith('!help'):
            mensagem = '!md (link)\n!ms (name)\n!pd (link)\n Discord > Dowser#5924'
            _func_.enviar_mensagem(mensagem)

    except:
        mensagem = 'Ocorreu um erro!'
        _func_.enviar_mensagem(mensagem)
        with open('ERROS_log.txt','a') as arquivo:
            arquivo.write(str(_func_.ler_ultima_mensagem()+'\n'))
        pass








