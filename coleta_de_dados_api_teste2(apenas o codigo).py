import requests

def enviar_arquivos():
    # Caminho do arquivo para upload
    caminho = 'D:\ebac\produtos_informatica (1).xlsx'

    try:
        with open(caminho, 'rb') as arquivo:
            requisicao = requests.post('https://file.io', files={'file': arquivo})

        print("Status Code:", requisicao.status_code)
        print("Resposta do Servidor:", requisicao.text)

        try:
            saida_requisicao = requisicao.json()
            print(saida_requisicao)
            url = saida_requisicao.get('link')
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
    # Esta função não será chamada neste exemplo sem chave
    print("Função enviar_arquivo_chave não utilizada neste exemplo.")

def receber_arquivo(file_url):
    requisicao = requests.get(file_url)

    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as files:
            files.write(requisicao.content)
        print("arquivo baixado com sucesso")
    else:
        print("Erro ao baixar arquivo", requisicao.json())

enviar_arquivos()