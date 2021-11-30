# depends on:
#   Executable: chromedriver
#   Folder: audios_suporte
#   Libs: selenium, pygame


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl
from pygame import mixer
import getpass, platform

SO = platform.system()

print("Welcome OTRS!")
print("-" * 30)
login = input(str('Login:'))
password = getpass.getpass(prompt='Password: ', stream=None)

if 'Windows' in SO:
    driver = webdriver.Chrome(executable_path="chromedriver_windows.exe")
if 'Linux' in SO:
    driver = webdriver.Chrome(executable_path="chromedriver")

driver.maximize_window()
driver.get("http://otrs.in.iti.gov.br/otrs/index.pl")
driver.find_element_by_id('User').send_keys(login, Keys.TAB)
driver.find_element_by_id('Password').send_keys(password, Keys.ENTER)
driver.get('http://otrs.in.iti.gov.br/otrs/index.pl?Action=AgentTicketQueue;QueueID=0;SortBy=Queue;OrderBy=Up;View='
           'Small;Filter=All')

while True:

    lista = list()

    chamados = driver.find_elements_by_class_name('MasterAction')

    try:
        star = driver.find_element_by_class_name('UnreadArticles')
        if star:
            mixer.init()
            mixer.music.load('audios_suporte/note.mp3')
            mixer.music.play()
            sl(1)
    except:
        pass

    for chamado in chamados:
        ticket = chamado.find_elements_by_xpath('//td[10]')
        lista.append(ticket)

    for estados in lista[0]:
        estado = estados.text
        if 'novo' in estado:
            mixer.init()
            mixer.music.load('audios_suporte/new.mp3')
            mixer.music.play()
            sl(2)

    driver.refresh()
    sl(2)
