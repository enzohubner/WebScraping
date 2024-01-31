from bs4 import BeautifulSoup
import requests


url = "https://pt.wikipedia.org/wiki/Napole%C3%A3o_Bonaparte"
resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, 'html.parser')

##print(soup.prettify().encode('utf-8', errors='ignore'))

tabela = soup.find('table', class_='infobox infobox_v2')

if tabela:
    for linha in tabela.find_all('tr'):
        dados_linha = []
        for coluna in linha.find_all('td'):
            dados_linha.append(coluna.text)
        print(' '.join(dados_linha))
else:
    print('Tabela não encontrada')