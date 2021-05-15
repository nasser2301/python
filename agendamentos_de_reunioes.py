from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep as s
import datetime
import re

def day():
     while True:
            try:
                number = int(input('dia (1-31): '))

                if number >= 1 and number <= 31:
                    return number
                    break
                else:
                    print('Dia inválido! Digite novamente o ', end='')
            except ValueError as e:
                print('Este campo só aceita valores numéricos. Por favor, digite o ', end='')
def day_of_week():
    while True:

        dia = str(input('Dia da semana (Seg à Sex): ')).lower()

        if dia == 'segunda-feira' or dia == 'segunda' or dia == 'seg' or dia == 'monday':
            dia = 'Monday'
            return dia

        if dia == 'terça-feira' or dia == 'terça' or dia == 'ter' or dia == 'tuesday':
            dia = 'Tuesday'
            return dia

        if dia == 'quarta-feira' or dia == 'quarta' or dia == 'qua' or dia == 'wednesday':
            dia = 'Wednesday'
            return dia

        if dia == 'quinta-feira' or dia == 'quinta' or dia == 'qui' or dia == 'thursday':
            dia = 'Thursday'
            return dia

        if dia == 'sexta-feira' or dia == 'sexta' or dia == 'sex' or dia == 'friday':
            dia = 'Friday'
            return dia

        if dia == 'sabado' or dia == 'sab' or dia == 'saturday' or dia == 'domingo' or dia == 'dom' or dia == 'sunday':
            print('Não é possível agendar eventos nos finais de semana:', end=' ')
        else:
            print('Inválido, digite conforme o exemplo:', end=' ')
def hours():

    while True:
        try:
            num = int(input('hora do início da reunião: (0-23): '))

            if num <= 23:
                return num
            else:
                print('Inválido, digite conforme o exemplo.', end=' ')
        except ValueError:
            print('Este campo só aceita valores numéricos. Por favor, digite a ', end='')
def validar_minuto():
    while True:
        try:
            num = int(input('minuto (0-60) (Ex: 05,10,15...): '))
            if num == 0 or num == 5:
                return num
            if num == 5 or num == 10:
                return num
            if num == 15 or num == 20:
                return num
            if num == 25 or num == 30:
                return num
            if num == 35 or num == 40:
                return num
            if num == 45 or num == 50:
                return num
            if num == 55 or num == 60:
                return num
            else:
                print('Número inválido, digite no intervalo conforme o exemplo', end=' ')

        except ValueError:
            print('Este campo só aceita valores numéricos. Por favor, digite o ', end='')
def duration_hours():

    while True:
        try:
            num = int(input('duração em horas (0-24): '))

            if num <= 24:

                if num == 1:
                    num = str(num)
                    return num + ' hora'
                    break
                if num == 0 or num > 1:
                    num = str(num)
                    return num + ' horas'
                    break
            if num > 24 or type(num) == str:
                print('Número Inválido, por favor, digite um número de 0 à 24..\n')

        except ValueError:
            print('Este campo só aceita valores numéricos. Por favor, digite a ', end='')
def duration_minutes():


    while True:

        try:
            num = int(input('duração em minutos (Ex: 0,5,10....): '))

            if num <= 60:

                if num == 0 or num == 5:
                    num = str(num)
                    return num + ' minutos'
                    break
                if num == 5 or num == 10:
                    num = str(num)
                    return num + ' minutos'
                    break
                if num == 15 or num == 20:
                    num = str(num)
                    return num + ' minutos'
                    break
                if num == 25 or num == 30:
                    num = str(num)
                    return num + ' minutos'
                    break
                if num == 35 or num == 40:
                    num = str(num)
                    return num + ' minutos'
                    break
                if num == 45 or num == 50:
                    num = str(num)
                    return num + ' minutos'
                    break
                if num == 55 or num == 60:
                    num = str(num)
                    return num + ' minutos'
                    break
                else:
                    print('Número inválido, digite no intervalo conforme o exemplo', end=' ')
            if num > 60:
                print('Número Inválido, por favor, digite um número de 0 à 60..\n')

        except ValueError:
            print('Este campo só aceita valores numéricos. Por favor, digite a ', end='')


# Variáveis
mes = datetime.datetime.today().ctime()[4:7]
dia_atual = str(datetime.date.today().day)
dia_da_semana_atual = str(datetime.datetime.today().strftime('%A')).capitalize()
emails = []
emails_para_colar = ''
site = 'url'
login = 'login'
senha = 'senha'
botao_iniciar_sessao_xpath = '//*[@id="guest_signin_split_button-trigger"]/div/button[1]/span'
campo_para_digitar_o_login = '//*[@id="IDToken1"]'
campo_para_digitar_a_senha = '//*[@id="IDToken2"]'
botao_para_agendar_a_reuniao = '//*[@id="scheduleEntry"]'
campo_do_topico_da_reuniao = '//*[@id="topic"]'
clique_da_data_e_hora = '//*[@id="scheduleTimeTrigger"]/span[2]/span[2]'
duracao_min = '//*[@id="scheduleFormSelectDurationMinute"]'
duracao_hora = '//*[@id="scheduleFormSelectDurationHour"]'
botao_concluido = '//*[@id="scheduleDone"]'
campo_para_digitar_os_emails = '//*[@id="invite_attendee_input"]'
botao_iniciar = '//*[@id="scheduleEdit"]'
link_da_reuniao = '//*[@id="main_content"]/div/div[1]/div[2]/dl/dd[1]/span[1]'
numero_da_reuniao = '//*[@id="meetingKeySelector"]'
horario_de_inicio_e_termino = '//*[@id="main_content"]/div/div[1]/div[1]/div[1]/div[2]/div[3]/span[1]'
dia_agendado = '//*[@id="main_content"]/div/div[1]/div[1]/div[1]/div[2]/div[3]/span[2]'
emails_criados_na_reuniao = '//div[@class="mdp_attendee_name"]'


# Variáveis interativas
topico_da_reuniao = str(input('Tópico da reunião: ')).title()
dia = day()
dia_que_ocorrera_a_reuniao = day_of_week()
horario_de_inicio_da_reuniao = hours()
minuto_de_inicio_da_reuniao = validar_minuto()
duracao_da_reuniao_em_horas = duration_hours()
duracao_da_reuniao_em_minutos = duration_minutes()

# Validador de e-mails
while True:
    email = (str(input('emails dos participantes: ')))
    validador_de_email = re.search(r'[A-Za-z0-9._]+@[a-zA-Z]+.+[A-Za-z]+.+[A-Za-z]+', email)
    if validador_de_email == None:
        print('Email inválido, digite novamente o', end=' ')
    if validador_de_email:
        emails.append(email)
        resp = str(input('Deseja adicionar mais emails?')).lower()
        if resp in 'naonão':
            break
        if resp != 'sim' or (resp != 'não' or resp != 'nao'):
            print('Resposta incorreta, por favor, digite sim ou não!')

# contatenador de e-mails
for em in emails:
    emails_para_colar += em + '; '

# Abre o navegador
web = webdriver.Chrome()

# Navega no site informado
web.get(site)
s(3)

# clica no botão "Iniciar Sessão"
web.find_element_by_xpath(botao_iniciar_sessao_xpath).click()
s(4)

# Digita o login e pressiona a tecla "ENTER"
web.find_element_by_xpath(campo_para_digitar_o_login).send_keys(login, Keys.ENTER)
s(4)

# Digita a senha e pressiona a tecla "ENTER"
web.find_element_by_xpath(campo_para_digitar_a_senha).send_keys(senha, Keys.ENTER)
s(4)

# Clica no botão para agendar a reunião
web.find_element_by_xpath(botao_para_agendar_a_reuniao).click()
s(6)

# Preenche o tópico da reunião
web.find_element_by_xpath(campo_do_topico_da_reuniao).send_keys(topico_da_reuniao)

# Clica na data e hora para carregar o calendario e os campos de horários
web.find_element_by_xpath(clique_da_data_e_hora).click()
s(4)

# Procura pelo elemento de acordo com os parâmetros especificados nas variáveis para o click correto no calendário.
web.find_element_by_css_selector(f"[aria-label='{dia_que_ocorrera_a_reuniao} {mes} {dia}, 2021']").click()
s(4)
# identifica o campo de hora da reunião, limpa o campo, clica, coloca a hora especificada, pressiona "ENTER" e depois "TAB"
horario = web.find_element_by_xpath('//*[@id="scheduleFormSelectHour"]')
horario.click()
horario.send_keys(Keys.BACKSPACE)
horario.send_keys(Keys.BACKSPACE)
horario.send_keys(horario_de_inicio_da_reuniao)
s(1)
horario.send_keys(Keys.ENTER)
s(1)
horario.send_keys(Keys.TAB)

# identifica o campo de minuto da reunião, digita o minuto especificado na variável, pressiona "ENTER" e depois "TAB"
minuto_ini = web.find_element_by_xpath('//*[@id="scheduleFormSelectMinute"]')
minuto_ini.click()
minuto_ini.send_keys(Keys.BACKSPACE)
minuto_ini.send_keys(Keys.BACKSPACE)
minuto_ini.send_keys(minuto_de_inicio_da_reuniao)
s(1)
minuto_ini.send_keys(Keys.ENTER)
s(1)
minuto_ini.send_keys(Keys.TAB)

'''
identifica o campo de duração da reunião em horas, clica, roda um for com todas as classes 
para comparar a string da classe com a string especificada na variável.
'''
web.find_element_by_xpath(duracao_hora).click()
s(3)
x_hora = web.find_elements_by_class_name('el-select-dropdown__item')

for i in x_hora:
    if i.text == duracao_da_reuniao_em_horas:
        i.click()
        i.send_keys(Keys.ENTER)

'''
identifica o campo de duração da reunião em minutos, clica, roda um for com todas as classes 
para comparar a string da classe com a string especificada na variável.
'''
web.find_element_by_xpath(duracao_min).click()
x_minuto = web.find_elements_by_class_name('el-select-dropdown__item')

for j in x_minuto:
    if j.text == duracao_da_reuniao_em_minutos:
        j.click()
        j.send_keys(Keys.ENTER)

# Clica no botão "Concluido"
web.find_element_by_xpath(botao_concluido).click()
s(4)

# Cola os e-mails informados para participar da reunião e clica em iniciar para finalizar o agendamento.
web.find_element_by_xpath(campo_para_digitar_os_emails).send_keys(emails_para_colar, Keys.ENTER)
s(0.5)
web.find_element_by_xpath(botao_iniciar).click()
s(4)

link_da_reuniao = web.find_element_by_xpath(link_da_reuniao).text
numero_da_reuniao = web.find_element_by_xpath(numero_da_reuniao).text
horario_de_inicio_e_termino = web.find_element_by_xpath(horario_de_inicio_e_termino).text
dia_agendado = web.find_element_by_xpath(dia_agendado).text
emails_criados_na_reuniao = web.find_elements_by_xpath(emails_criados_na_reuniao)

emails2 = list()
for email in emails_criados_na_reuniao:
       emails2.append(email.text)

# Fecha o navegador
#web.close()

print(f'''
Reunião Agendada conforme solicitado, segue as informações:

Tópico da Reunião: {topico_da_reuniao}
Dia: {dia_agendado}
Horário: {horario_de_inicio_e_termino}
Link da Reunião: {link_da_reuniao}
Número da reunião: {numero_da_reuniao}
E-mail dos participantes: {emails2}
''')
