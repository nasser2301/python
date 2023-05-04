from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randrange
from datetime import datetime
import re

nav = webdriver.Chrome(executable_path='./chromedriver')

nav.maximize_window()

nav.get("https://getran.detran.df.gov.br/site/habilitacao/consultas/filtro-consulta-resultado-htm.jsp")
nav.find_element(By.ID, "CPF").send_keys("03910374123")
nav.find_element(By.XPATH, '//*[@id="content-update"]/div/div/div/div/a[1]').click()
sleep(3)
var = nav.find_element(By.ID, 'pergunta').text
split0 = var.split('+')[0].strip()
split1 = var.split('+')[1].strip()

print(split0)
print(split1)

regex = re.search("[0-9]", split0)
regex1 = re.search("[0-9]", split1)

regex = int(regex.group())
regex1 = int(regex1.group())

resultado = str(regex + regex1)
nav.find_element(By.ID, "CODSEG").send_keys(resultado)
nav.find_element(By.XPATH, '//*[@id="content-update"]/div/div/div/div[2]/a[1]').click()
sleep(2)

while True:

    nav.find_element(By.ID, "headingPendencia").click()
    resultado = nav.find_element(By.XPATH, '//*[@id="collapsePendencia"]/div/div/div[2]/div/div/table/tbody/tr/td[5]').text.strip()

    if not resultado:
        pass
    else:
        print(resultado)
        nav.close()
        break
    sleep(3)
    nav.refresh()




