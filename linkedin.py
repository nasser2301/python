from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep as sl
from confidencial import senha2, login_email


nav = webdriver.Chrome("./chromedriver")
nav.maximize_window()
nav.get('https://www.linkedin.com/')
nav.find_element(By.ID, 'session_key').send_keys(login_email)
nav.find_element(By.ID, 'session_password').send_keys(senha2, Keys.ENTER)
nav.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]').click()
sl(3)
nav.find_element(By.XPATH, '/html/body/div[5]/header/div/div/div/div[2]/div[1]/div/div/input[1]').send_keys('devops', Keys.ENTER)
sl(2)
nav.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[3]/section/div/div/div/div/div/button').click()
sl(2)
nav.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[1]/fieldset/div/ul/li[1]/label/p/span[1]').click()
sl(1)
nav.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/div/button[2]').click()


sl(2)
vagas = nav.find_elements(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[*]')

section1 = nav.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]')

for vaga in vagas:
    nav.execute_script("arguments[0].scrollBy(0, 500)", section1)
    vaga.click()
    descricao = nav.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[2]/article/div/div[*]')
    print(f'''Vaga:

{vaga.text}

Descrição:          

{descricao.text}
          ''')
    print('---------------------------------------------------------------------------')
    sl(2)