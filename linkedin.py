from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep as sl
from confidencial import senha2, login_email
import random


nav = webdriver.Chrome("./chromedriver")
nav.maximize_window()
nav.get('https://www.linkedin.com/')
nav.find_element(By.ID, 'session_key').send_keys(login_email)
nav.find_element(By.ID, 'session_password').send_keys(senha2, Keys.ENTER)
nav.get('https://www.linkedin.com/mynetwork/')
sl(12)
nav.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[1]/div/button').click()
sl(3)

for repeat in range(0, 6):
    nav.execute_script('document.querySelector(".discover-cohort-recommendations-modal__content").scrollBy(0,1000000)')
    sl(4)

sl(1)
nav.execute_script('document.querySelector(".discover-cohort-recommendations-modal__content").scrollTo(0,0)')
sl(1)

pessoas = nav.find_elements(By.XPATH, '/html/body/div[3]/div/div/div[2]/section/div/ul/li[*]/div/section/div[2]/footer/button')

for pessoa in pessoas:
    sl(random.randint(3, 7))
    pessoa.click()


