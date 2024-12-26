import os

try:
    usuario = os.environ['USERNAME'] if os.name == 'nt' else os.environ['USER']
except KeyError:
    print("Erro: Não foi possível determinar o usuário do sistema.")
    exit()

cam_dir_downloads = fr'/home/{usuario}/Downloads'
cam_dir_ISO = fr'/home/{usuario}/Downloads/ISO'
cam_dir_ZIPADOS = fr'/home/{usuario}/Downloads/ZIPADOS'
cam_dir_EXECUTÁVEIS = fr'/home/{usuario}/Downloads/EXECUTÁVEIS'
cam_dir_ARQUIVOS_GERAIS = fr'/home/{usuario}/Downloads/ARQUIVOS_GERAIS'
cam_dir_IMAGENS = fr'/home/{usuario}/Downloads/IMAGENS'
cam_dir_VIDEOS_E_SONS = fr'/home/{usuario}/Downloads/VIDEOS_E_SONS'
cam_dir_KEYS = fr'/home/{usuario}/Downloads/KEYS'

dir_downloads = os.listdir(cam_dir_downloads)

for arquivo in dir_downloads:

    if '.iso' in arquivo:
        if os.path.isdir(cam_dir_ISO):
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/ISO/{arquivo}')
        if not os.path.isdir(cam_dir_ISO):
            os.mkdir(cam_dir_ISO)
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/ISO/{arquivo}')

    if '.zip' in arquivo or '.7z' in arquivo or '.tar' in arquivo or '.TAR' in arquivo or '.rar' in arquivo or '.tgz' in arquivo:
        if os.path.isdir(cam_dir_ZIPADOS):
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/ZIPADOS/{arquivo}')
        if not os.path.isdir(cam_dir_ZIPADOS):
            os.mkdir(cam_dir_ZIPADOS)
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/ZIPADOS/{arquivo}')

    if '.msi' in arquivo or '.exe' in arquivo or '.EXE' in arquivo or '.deb' in arquivo:
        if os.path.isdir(cam_dir_EXECUTÁVEIS):
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/EXECUTÁVEIS/{arquivo}')
        if not os.path.isdir(cam_dir_EXECUTÁVEIS):
            os.mkdir(cam_dir_EXECUTÁVEIS)
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/EXECUTÁVEIS/{arquivo}')

    if '.pdf' in arquivo or '.sh' in arquivo or '.PDF' in arquivo or'.odf' in arquivo or '.txt' in arquivo or '.doc' in arquivo or '.docx' in arquivo\
            or '.accdb' in arquivo or '.xlsx' in arquivo or '.log' in arquivo or '.html' in arquivo\
            or '.pub' in arquivo or '.csv' in arquivo or '.pbix' in arquivo or '.odt' in arquivo or '.ods' in arquivo \
            or '.bpm' in arquivo or '.xml' in arquivo or '.xlsb' in arquivo or '.yml' in arquivo or '.yaml' in arquivo \
            or '.json' in arquivo or '.ppt' in arquivo or '.pptx' in arquivo or '.jar' in arquivo or '.vce' in arquivo:

        if os.path.isdir(cam_dir_ARQUIVOS_GERAIS):
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/ARQUIVOS_GERAIS/{arquivo}')
        if not os.path.isdir(cam_dir_ARQUIVOS_GERAIS):
            os.mkdir(cam_dir_ARQUIVOS_GERAIS)
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/ARQUIVOS_GERAIS/{arquivo}')

    if '.jpeg' in arquivo or '.JPEG' in arquivo or '.png' in arquivo or '.PNG' in arquivo or '.jpg' in arquivo\
            or '.JPG' in arquivo or '.webp' in arquivo:
        if os.path.isdir(cam_dir_IMAGENS):
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/IMAGENS/{arquivo}')
        if not os.path.isdir(cam_dir_IMAGENS):
            os.mkdir(cam_dir_IMAGENS)
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/IMAGENS/{arquivo}')

    if '.mp4' in arquivo or '.mp3' in arquivo:
        if os.path.isdir(cam_dir_VIDEOS_E_SONS):
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/VIDEOS_E_SONS/{arquivo}')
        if not os.path.isdir(cam_dir_VIDEOS_E_SONS):
            os.mkdir(cam_dir_VIDEOS_E_SONS)
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/VIDEOS_E_SONS/{arquivo}')

    if '.pem' in arquivo or '.pub' in arquivo:
        if os.path.isdir(cam_dir_KEYS):
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/KEYS/{arquivo}')
        if not os.path.isdir(cam_dir_KEYS):
            os.mkdir(cam_dir_KEYS)
            os.rename(fr'{cam_dir_downloads}/{arquivo}', fr'{cam_dir_downloads}/KEYS/{arquivo}')
