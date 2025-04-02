#EXTRAÇÃO E MANIPULAÇÃO

import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for artigo_tag in extracao.find_all('article'):
    livro = {}
    titulo_tag = artigo_tag.find('h3')
    preco_tag = artigo_tag.find('p', class_='price_color')

    if titulo_tag:
        titulo = titulo_tag.get_text().strip()
        livro['Título'] = titulo

    if preco_tag:
        preco_texto = preco_tag.get_text().strip()
        livro['Preço'] = preco_texto

    if livro:
        catalogo.append(livro)

contar_livros = len(catalogo) # Atualiza a contagem com o número de livros no catálogo

print('Livros encontrados:')
for i, livro in enumerate(catalogo):
    if 'Título' in livro and 'Preço' in livro:
        print(f'Livro #{i + 1}:')
        print('Título: \n', livro['Título'])
        print('Preço: \n', livro['Preço'])
        print('\n---')

print('\nTotal livros:', contar_livros)