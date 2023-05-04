from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from confidencial import senha, email, webmail
from time import sleep as sl

# Logar no webmail
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

nav = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
nav.maximize_window()
nav.get(webmail)
nav.find_element(By.XPATH, '//*[@id="rcmloginuser"]').send_keys(email[:12], Keys.TAB)
nav.find_element(By.XPATH, '//*[@id="rcmloginpwd"]').send_keys(senha, Keys.ENTER)
sl(2)

# contadores
c = 0
c1 = 0

while True:

    try:

        # Verificando a existência de e-mails não visualizados.
        novo_email = nav.find_element(By.XPATH, '//*[@id="rcmliSU5CT1g"]/a/span')

        # Verificando se houve a coleta de informação.
        if novo_email and c == 0:
            print('Novo(s) email(s) na caixa de entrada!')
            c += 1
            c1 = 0

    except:

        novo_email = ''

        if not novo_email and c1 == 0:
            print('Não há emails novos!')
            c1 += 1
            c = 0


    nav.refresh()
    sl(4)