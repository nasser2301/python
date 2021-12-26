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
from confidencial import senhaa, email, name_server

# Configurações para login e conexão com o gmail
server = smtplib.SMTP(name_server)
server.ehlo()
server.starttls()
server.login(email, senhaa)

body = '''
Prezados,

    Está é uma mensagem de teste!
    

At.te,
Rhuan Diego Nobre Nasser
Preposto/Coordenador de Tecnologia da Informação
'''

# Envio do e-mail
email_msg = MIMEMultipart()
email_msg['From'] = email
email_msg['To'] = email
email_msg['Subject'] = "Utilizando webmail do ITI!"
email_msg.attach(MIMEText(body, 'plain'))
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

# Desconectando do gmail
server.quit()
