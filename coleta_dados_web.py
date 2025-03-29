import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, features='html.parser')

#exibir o texto
print(extracao.text.strip())

#Filtrar a exibição pela tag

for linha_texto in extracao.find_all('h2'):
        titulo = linha_texto.name
        print('Titulo ', titulo)

#contar paragrafos e titulos
contar_titulos = 0
contar_paragrafos = 0
for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1

print('total de titulos', contar_titulos)
print('total de paragrafos', contar_paragrafos)

# Exibir somentos textos das tags h2 e p
for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        titulos = linha_texto.text.strip()
        print('Titulos:  \n', titulos)
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('paragrafo: \n', paragrafo)

#exibir tags aninhadas
for titulo in extracao.find_all('h2'):
    print('\n Titulo:', titulo.text.strip())
    for link in titulo.find_next_sibling('p'):
        for a in link.find_all('a' , href=True):
            print('texto link:', a.text.strip(), 'URL:', a["href"] )

