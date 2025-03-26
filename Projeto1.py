import os
import shutil

def criar_pastas(diretorio, extensoes):
    """Cria pastas para cada extensão se não existirem."""
    for extensao in extensoes:
        pasta = os.path.join(diretorio, extensao.lower())
        if not os.path.exists(pasta):
            os.makedirs(pasta)

def organizar_arquivos(diretorio):
    """Move arquivos para pastas baseado em sua extensão."""
    extensoes_unicas = set()

    # Identifica extensões únicas
    for arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            extensao = os.path.splitext(arquivo)[1][1:].lower()  # Remove o ponto (ex: '.pdf' -> 'pdf')
            if extensao:
                extensoes_unicas.add(extensao)

    # Cria pastas e organiza arquivos
    criar_pastas(diretorio, extensoes_unicas)

    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            extensao = os.path.splitext(arquivo)[1][1:].lower()
            if extensao:
                pasta_destino = os.path.join(diretorio, extensao)
                shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                print(f"Arquivo '{arquivo}' movido para '{pasta_destino}'.")

if __name__ == "__main__":
    diretorio_alvo = input("Digite o caminho do diretório a ser organizado: ")
    if os.path.isdir(diretorio_alvo):
        organizar_arquivos(diretorio_alvo)
        print("Organização concluída!")
    else:
        print("Diretório inválido. Verifique o caminho.")
