import os
import shutil

caminho = '/home/nasser/Área de Trabalho/'
caminho_de_destino_imagens = 'pasta_para_testes/imagens/'
caminho_de_destino_arquivos = 'pasta_para_testes/arquivos/'
caminho_de_destino_zipados = 'pasta_para_testes/zipados/'

def verifica_tipo(dest):
    if os.path.isdir(caminho + dest) == True:
        src = caminho + file + f'/{item}'
        dst = caminho + dest + item
        shutil.copyfile(src, dst)
    else:
        os.mkdir(caminho + dest)
        src = caminho + file + f'/{item}'
        dst = caminho + dest + item
        shutil.copyfile(src, dst)


for file in os.listdir(caminho):
    if 'pasta_para_testes' in file:
        pass
    else:
        se_for_pasta = os.path.isdir(caminho + file)
        if se_for_pasta == True:
            lista = os.listdir(caminho + file)

            for item in lista:
                if '.jpeg' in item or '.jpg' in item or '.png' in item:
                    verifica_tipo(caminho_de_destino_imagens)

                if '.pdf' in item or '.doc' in item or '.docx' in item or '.xlsx' in item or '.odt' in item \
                        or '.html' in item or '.txt' in item:
                    verifica_tipo(caminho_de_destino_arquivos)

                if '.zip' in item or '.7z' in item or '.xz' in item or '.bzip' in item or '.b2zip' in item:
                    verifica_tipo(caminho_de_destino_zipados)