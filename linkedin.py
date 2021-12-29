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
paginas = nav.find_elements(By.XPATH, "/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/section/div/ul/li[*]/button")


for pagina in paginas:
    nav.execute_script('document.querySelector(".jobs-search-results").scrollBy(0,1000)')
    sl(2)
    pagina.click()
    sl(2)

# while True:
#
#     for pagina in paginas:
#
#         for i in range(8):
#             nav.execute_script('document.querySelector(".jobs-search-results").scrollBy(0,500)')
#             sl(1)
#
#             if i == 7:
#                 nav.execute_script('document.querySelector(".jobs-search-results").scrollTo(0,0)')
#                 sl(2)
#                 print(len(nav.find_elements(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[*]/div/div/div[1]')))
#
#         num = int(pagina.text)
#
#         if num >= 2:
#             nav.execute_script('document.querySelector(".jobs-search-results").scrollTo(0,0)')
#             sl(2)
#             print(pagina.text)
#             pagina.click()
#             sl(2)
#             nav.execute_script('document.querySelector(".jobs-search-results").scrollBy(0,500)')

# for n, vaga in enumerate(vagas):
#     if (n%2) == 0 and n >= 4:
#         nav.execute_script('document.querySelector(".jobs-search-results").scrollBy(0,1000)')
#
#     vaga.click()
#     descricao = nav.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[2]/article/div/div[*]')
#     print(f'''Vaga:
#
# {vaga.text}
#
# Descrição:
#
# {descricao.text}
#           ''')
#     print('---------------------------------------------------------------------------')
#     sl(2)