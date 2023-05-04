'''
        Dependencies:

        Libs:
            - smtplib

        arquivo:
            - Qualquer arquivo para a análise
            - Arquivo com o nome de "confidencial" com senha, email e nome_do_servidor.
'''

# Importação da lib necessária
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from confidencial import senha, email, nome_do_servidor

# Configurações para login e conexão com o gmail
server = smtplib.SMTP(nome_do_servidor)
server.ehlo()
server.starttls()
server.login(email, senha)

# Abertura do arquivo e leitura dos dados
var = open('log', 'r')
conteudo_do_arquivo = var.read().lower()

# Condição para identificar o erro
if 'error' in conteudo_do_arquivo or 'err' in conteudo_do_arquivo or 'erro' in conteudo_do_arquivo:
    body = 'Há um erro identificado no arquivo de log, verifique o mesmo por gentileza!'
else:
    pass

# Envio do e-mail
email_msg = MIMEMultipart()
email_msg['From'] = email
email_msg['To'] = email
email_msg['Subject'] = "Erro identificado no log!"
email_msg.attach(MIMEText(body, 'plain'))
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

# Desconectando do gmail
server.quit()
