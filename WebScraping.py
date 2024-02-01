from collections import Counter
from bs4 import BeautifulSoup
import requests, string, sys, nltk, re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

sys.stdout.reconfigure(encoding='utf-8')

nltk.download('punkt')
nltk.download('stopwords')

url = "https://pt.wikipedia.org/wiki/Napole%C3%A3o_Bonaparte"
resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, 'html.parser')
text = soup.get_text()

##print(soup.prettify().encode('utf-8', errors='ignore'))

tabela = soup.find('table', class_='infobox infobox_v2')

#if tabela:
#    for linha in tabela.find_all('tr'):
#        dados_linha = []
#        for coluna in linha.find_all('td'):
#            dados_linha.append(coluna.text)
#        print(' '.join(dados_linha))
#else:
#    print('Tabela não encontrada')

##Usando a biblioteca NLKT
palavras = word_tokenize(text)
sentecas = sent_tokenize(text)
stop_words = set(stopwords.words('portuguese'))

palavras_limpas = []

for palavra in palavras:
    palavra = palavra.lower()
    if palavra not in string.punctuation and palavra not in stop_words:
        palavra = re.sub(r'[^a-zA-ZÀ-ú0-9]', '', palavra)
        if palavra:
            palavras_limpas.append(palavra)


with open('palavras_limpas.txt', 'w', encoding = 'utf-8') as file:
    file.write('/n'.join(palavras_limpas))

contador_de_palavras = Counter(palavras_limpas)
palavras_mais_frequentes = contador_de_palavras.most_common(10)

for palavra, frequencia in palavras_mais_frequentes:
    print(f"A palavra {palavra}, repetiu {frequencia} vezes")
