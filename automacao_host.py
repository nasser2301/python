from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep as sl

login = input(str("Digite seu login do HOST: ")).strip()
password = input(str("Digite o password do HOST: ")).strip()

nav = webdriver.Chrome(executable_path='./chromedriver')
nav.maximize_window()
nav.get('https://host.globalhitss.com/')
nav.find_element(By.ID, "UserName").send_keys(login)
nav.find_element(By.ID, "Password").send_keys(password)
nav.find_element(By.ID, "boton").send_keys(Keys.ENTER)

sl(5)
nav.find_element(By.XPATH, '//*[@id="calendario"]/div/table/tbody/tr[1]/td[5]').click()

n = nav.find_elements(By.CLASS_NAME, 'diaInhabil')

final_de_semana = []
for i in n:
    qtde_caracteres = len(i.text)
    if qtde_caracteres == 1:
        qtde_caracteres = '0' + str(i.text)
        final_de_semana.append(qtde_caracteres)
    else:
        final_de_semana.append(i.text)

while True:
    dia = nav.find_element(By.ID, "lblFechaCaptura").text[4:6]

    if dia not in final_de_semana:

        nav.find_element(By.ID, 'cmbActividades').send_keys("ACTU", Keys.ENTER)
        nav.find_element(By.ID, "HorasCapturadas").send_keys("08", Keys.ENTER)
        nav.find_element(By.ID, "btnOk").click()
        sl(3)

        try:
            nav.find_element(By.ID, "btnDiaSiguiente").click()
        except:
            break

    else:
        nav.find_element(By.ID, "btnDiaSiguiente").click()
nav.close()
