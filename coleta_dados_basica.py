import requests
from bs4 import BeautifulSoup
import pandas

print('Request: ')
response = requests.get('https://pt.wikipedia.org/wiki/Yahoo!_Finance')
print(response.text[:600])

soup = BeautifulSoup(response.text, features='html.parser')
print(soup.prettify()[:10000])


print('pandas: ')
url_dados = pandas.read_html('https://pt.wikipedia.org/wiki/Yahoo!_Finance')
print(url_dados[0].head(30))