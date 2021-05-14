from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as s
import requests

def telegram_bot_sendtext(bot_message):
    bot_token = 'token_telegram'
    bot_chatID = 'id_do_contato ou grupo'
    send_text = f'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()



url = 'url'
login = 'login'
senha = 'senha'

# Abre o navegador
w = webdriver.Chrome(executable_path=r'/home/nasser/Desktop/chromedriver')
w.maximize_window()
w.get(url)
w.find_element_by_id('User').send_keys(login)
w.find_element_by_id('Password').send_keys(senha, Keys.ENTER)
s(1)

while True:
    try:
        filas = w.find_elements_by_xpath('//div[3]/div[1]/div[1]/ul/li/a[@class]')
        chamados_abertos = w.find_elements_by_xpath('//*[@class="MasterAction"]')
        qtde_de_chamados_na_fila = len(chamados_abertos)

        if qtde_de_chamados_na_fila == 0:
            w.refresh()
            s(5)

        if qtde_de_chamados_na_fila == 1:

            for fila in filas:
                fila = fila.text
                if 'Suporte' in fila:
                        ticket = w.find_element_by_xpath('//td[4]/a').text
                        tecnico = w.find_element_by_xpath('//td[10]/div').get_attribute('title')
                        tempo = w.find_element_by_xpath('//td[5]/div').get_attribute('title')
                        usuario = w.find_element_by_xpath('//td[6]/div[1]').get_attribute('title')
                        assunto = w.find_element_by_xpath('//td[6]/div[2]').get_attribute('title')
                        s(4)

                        #telegram_bot_sendtext(f'Chamado: {ticket}')
                        telegram_bot_sendtext(f'Chamado {ticket} aberto na fila ')
                        telegram_bot_sendtext(f'Usuário: {usuario} ')
                        telegram_bot_sendtext(f'Assunto: {assunto}')
                        telegram_bot_sendtext(f'Técnico: {tecnico}')
                        telegram_bot_sendtext(f'Tempo: {tempo}')
                        telegram_bot_sendtext(f'Fila: {fila}')
                        telegram_bot_sendtext(f'-' * 30)
                        #telegram_bot_sendtext(f'''
                        #{ticket} aberto na fila
                        #Usuário: {usuario}
                        #Assunto: {assunto}
                        #Técnico: {tecnico}
                        #Tempo: {tempo}
                        #Fila: {fila}''')
                        s(60)

        if qtde_de_chamados_na_fila == 2 or qtde_de_chamados_na_fila > 2:
            telegram_bot_sendtext('Há 2 ou mais chamados na fila!')
            s(30)

    except:
        pass
