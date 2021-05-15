import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as s
import pandas

nome_do_produto = str(input('Nome do produto: '))
index = nome_do_produto.find(' ')

while True:
    sim_nao = str(input('Com filtro de valores? (s/n)')).lower()
    if sim_nao == 's':
        de = int(input('De: '))
        ate = int(input('Até: '))
        break
    if sim_nao == 'n':
        break
    else:
        print('Por favor, digite conforme o exemplo.', end=' ')


campo_de_pesquisa_do_produto = '//form/input'
site = 'https://www.mercadolivre.com.br/'

playstation = list()
todos_os_produtos = dict()


# Abre o navegador.
web = webdriver.Chrome()

# Acessa o site.
web.get(site)
s(2)

# Escreve no campo de pesquisa do mercado livre e depois tecla o "ENTER".
web.find_element_by_xpath(campo_de_pesquisa_do_produto).send_keys(nome_do_produto, Keys.ENTER)
s(4)


while True:
    web.execute_script('window.scrollTo(0, 30000)')
    nomes = web.find_elements_by_xpath('.//h2[@class="ui-search-item__title"]')
    links = web.find_elements_by_xpath('//li/div/div/div/a[@href]')
    valores = web.find_elements_by_xpath('.//div/div/div/div/span/span[2][@class="price-tag-fraction"]')
    #print('checando nomes', nomes)
    #print('checando links', links)
    #print('checando preços', valores)

    if not nomes:
        nomes = web.find_elements_by_xpath('.//h2[@class="ui-search-item__title ui-search-item__group__element"]')
        #print('if do nome', nomes)



    for valor, nome, link in zip(valores, nomes, links):
        if nome_do_produto[:index].lower() in nome.text.lower():
            if '.' in valor.text:
                v = valor.text.replace('.', '')
                v = int(v)
                if 's' in sim_nao:
                    if v >= de and v <= ate:
                        todos_os_produtos['Produto'] = nome.text
                        todos_os_produtos['Preço'] = v
                        todos_os_produtos['Links'] = link.get_attribute('href')
                        playstation.append(todos_os_produtos.copy())
                        print(nome.text)
                if 'n' in sim_nao:
                    todos_os_produtos['Produto'] = nome.text
                    todos_os_produtos['Preço'] = v
                    todos_os_produtos['Links'] = link.get_attribute('href')
                    playstation.append(todos_os_produtos.copy())
                    print(nome.text)
            else:
                try:
                    va = int(valor.text)
                    if 's' in sim_nao:
                        if va >= de and va <= ate:
                            todos_os_produtos['Produto'] = nome.text
                            todos_os_produtos['Preço'] = va
                            todos_os_produtos['Links'] = link.get_attribute('href')
                            playstation.append(todos_os_produtos.copy())
                            print(nome.text)
                    if 'n' in sim_nao:
                        todos_os_produtos['Produto'] = nome.text
                        todos_os_produtos['Preço'] = va
                        todos_os_produtos['Links'] = link.get_attribute('href')
                        playstation.append(todos_os_produtos.copy())
                        print(nome.text)
                except:
                    pass

    try:
        web.find_element_by_xpath('//li/a[@class="andes-pagination__link ui-search-link"][@title="Seguinte"]').click()
    except:
         break
    s(2)

planilha = pd.DataFrame(playstation)
planilha_moldada = planilha.sort_values('Preço')
planilha_moldada.to_excel(r'C:\Users\nasser\OneDrive\Área de Trabalho\mercado livre\valores.xlsx', index=False)
