from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from pygame import mixer
from password import senha, login
import os, getpass

usuario = os.environ['USERNAME']
senha = getpass.getpass("Digite sua senha do OTRS: ")

# Chrome Driver
web = webdriver.Chrome()
web.maximize_window()
web.get('http://otrs.in.iti.gov.br/otrs/index.pl')
web.find_element_by_id('User').send_keys(usuario)
web.find_element_by_id('Password').send_keys(senha, Keys.ENTER)
web.get('http://otrs.in.iti.gov.br/otrs/index.pl?Action=AgentTicketQueue;QueueID=5;View=Small;Filter=Unlocked')
chamados_na_fila_da_cotic = web.find_elements_by_xpath('/html/body/div[1]/div[4]/form/table/tbody/tr[*]/td[8]')

while chamados_na_fila_da_cotic:

    for chamado in chamados_na_fila_da_cotic:

        chamado = chamado.text

        if 'novo' in chamado:
            try:
                mixer.init()
                mixer.music.load('alert.mp3')
                mixer.music.play()
                sleep(7)
            except:
                pass
        else:
            pass

    web.refresh()
    sleep(3)
    chamados_na_fila_da_cotic = web.find_elements_by_xpath('/html/body/div[1]/div[4]/form/table/tbody/tr[*]/td[8]')
