import os
import shutil

caminho = '/home/nasser/Área de Trabalho/'
caminho_de_destino_imagens = 'pasta_para_testes/imagens/'
caminho_de_destino_arquivos = 'pasta_para_testes/arquivos/'
caminho_de_destino_zipados = 'pasta_para_testes/zipados/'

for file in os.listdir(caminho):
    if 'pasta_para_testes' in file:
        pass
    else:
        se_for_pasta = os.path.isdir(caminho + file)
        if se_for_pasta == True:
            lista = os.listdir(caminho + file)

            for item in lista:
                if '.jpeg' in item or '.jpg' in item or '.png' in item:
                    if os.path.isdir(caminho + caminho_de_destino_imagens) == True:
                        src = caminho + file + f'/{item}'
                        dst = caminho + caminho_de_destino_imagens + item
                        shutil.copyfile(src, dst)
                    else:
                        os.mkdir(caminho + caminho_de_destino_imagens)
                        src = caminho + file + f'/{item}'
                        dst = caminho + caminho_de_destino_imagens + item
                        shutil.copyfile(src, dst)

                if '.pdf' in item or '.doc' in item or '.docx' in item or '.xlsx' in item or '.odt' in item \
                        or '.html' in item or '.txt' in item:
                    if os.path.isdir(caminho + caminho_de_destino_arquivos) == True:
                        src = caminho + file + f'/{item}'
                        dst = caminho + caminho_de_destino_arquivos + item
                        shutil.copyfile(src, dst)
                    else:
                        os.mkdir(caminho + caminho_de_destino_arquivos)
                        src = caminho + file + f'/{item}'
                        dst = caminho + caminho_de_destino_arquivos + item
                        shutil.copyfile(src, dst)

                if '.zip' in item or '.7z' in item or '.xz' in item or '.bzip' in item or '.b2zip' in item:
                    if os.path.isdir(caminho + caminho_de_destino_zipados) == True:
                        src = caminho + file + f'/{item}'
                        dst = caminho + caminho_de_destino_zipados + item
                        shutil.copyfile(src, dst)

                    else:
                        os.mkdir(caminho + caminho_de_destino_zipados)
                        src = caminho + file + f'/{item}'
                        dst = caminho + caminho_de_destino_zipados + item
                        shutil.copyfile(src, dst)