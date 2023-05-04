from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randrange
from datetime import datetime

while True:
    sleep(1)
    #hora_e_minuto_atual = datetime.now().strftime("%H:%M")
    hora_atual = datetime.now().strftime("%H")
    minuto_atual = datetime.now().strftime("%M")

    # variável estática
    numero_que_varia = str(randrange(50, 51, 52, 53, 54, 55, 56, 57, 58, 59))

    print(f'Minuto atual: {minuto_atual}\nNumero que varia: {numero_que_varia}')

    if int(minuto_atual) > 14:

        if numero_que_varia == minuto_atual:
            print("bate o ponto agora")


# variável input
# login = input(str("Digite seu login do HOST: ")).strip()
# password = input(str("Digite o password do HOST: ")).strip()
#
# nav = webdriver.Chrome(executable_path='./chromedriver')
# nav.maximize_window()
# nav.get('https://www.mdcomune.com.br/')
# nav.find_element(By.ID, "LogOnModel_UserName").send_keys(login)
# nav.find_element(By.ID, "LogOnModel_Password").send_keys(password)
# nav.find_element(By.ID, "btnFormLogin").click()
