import requests

def enviar_arquivos():
    caminho = 'D:/ebac/produtos_informatica (1).xlsx'

    headers = {
        'Authorization': f'Bearer '
    }

    try:
        with open(caminho, 'rb') as arquivo:
            requisicao = requests.post('https://www.file.io/upload', files={'file': arquivo}, headers=headers)

        print("Status Code:", requisicao.status_code)
        print("Resposta do Servidor:", requisicao.text)

        try:
            saida_requisicao = requisicao.json()
            print(saida_requisicao)
            url = saida_requisicao.get('link') or saida_requisicao.get('Link') # Verifique as chaves corretas
            if url:
                print("Arquivo enviado. Link para acesso:", url)
            else:
                print("Link para acesso não encontrado na resposta.")
        except requests.exceptions.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {caminho}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def enviar_arquivo_chave():
    caminho = 'D:/ebac/produtos_informatica (1).xlsx'

    requisicao = requests.post(
       'https://www.file.io/upload',
        files={'file': open(caminho, 'rb')},
        headers={'Authorization': chave_acesso}
    )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado com chave. Link para acesso:", url)

def receber_arquivo(file_url):
    requisicao = requests.get(file_url)

    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as files:
            file.write(requisicao.content)
        print("arquivo baixado com sucesso")
    else:
        print("Erro ao baixar arquivo", requisicao.json())

enviar_arquivos()