import datetime, time, pandas as pd, win32com.client as win32, emoji, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl

# variáveis
mes = str(datetime.date.today().month)
ano = str(datetime.date.today().year)
dia = str(datetime.date.today().day)
completo = str(time.ctime())
hora = completo[11:13]
minuto = completo[14:16]
chamados_estourados_no_inicio_do_atendimento = total_de_chamados = finalizados = pendentes =  0

# Abre o navegador
web = webdriver.Chrome()

# Acessa o otrs
web.get('url')
sl(3)
web.find_element_by_id('User').send_keys('login')
web.find_element_by_id('Password').send_keys('senha', Keys.ENTER)

web.maximize_window()
sl(3)

# Acessa os relatório
web.find_element_by_xpath('//*[@id="nav-Reports"]/a').click()
sl(0.5)
web.find_element_by_xpath('//*[@id="nav-Reports-Statistics"]/a').click()
sl(2)
web.find_element_by_xpath('//*[@id="AppWrapper"]/div[3]/div[2]/div/div[2]/table/tbody/tr[19]/td[6]/a').click()
sl(2)

# Altera a data de acordo com a data atual para a extração
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCreateTimeStartMonth"]/option[{mes}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCreateTimeStartYear"]/option[{ano[2:]}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCreateTimeStopDay"]/option[{dia}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCreateTimeStopMonth"]/option[{mes}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCreateTimeStopYear"]/option[{ano[2:]}]').click()
web.find_element_by_xpath(f'//*[@id="StartStatistic"]/span').click()
sl(3)

# Minimiza a janela
web.close()

# Renomeia o arquivo
os.system(r'rename C:\Users\nasser\Downloads\Rel*.xlsx relatorio.xlsx')

# Tratamento dos dados
tabela = pd.read_excel(r"C:\Users\nasser\Downloads\relatorio.xlsx")
headers = tabela.iloc[0]
tabela = pd.DataFrame(tabela.values[1:], columns=headers)
tabela['Tempo de solução em minutos'] = tabela['Tempo de solução em minutos'].astype(int)
tabela['Primeira Resposta em Minutos'] = tabela['Primeira Resposta em Minutos'].astype(int)
tabela['Número'] = tabela['Número'].astype(int)
tabela['Ticket#'] = tabela['Ticket#'].astype(int)
tabela['Delta de tempo de solução em minutos'] = tabela['Delta de tempo de solução em minutos'].astype(int)

# Hora da abertura do chamado e o Atendente
m10m = tabela['Primeira Resposta em Minutos'].mean()
media_10_minutos = '{:.2f}'.format(m10m)

# 1,3,36 horas
ultrapassou_uma_hora = tabela.loc[tabela['Tempo de solução em minutos'] > 60].value_counts().sum()
em_compliance_uma_hora = tabela.loc[tabela['Tempo de solução em minutos'] <= 60].value_counts().sum()
ultrapassou_tres_horas = tabela.loc[tabela['Tempo de solução em minutos'] > 180].value_counts().sum()
em_compliance_tres_horas = tabela.loc[tabela['Tempo de solução em minutos'] <= 180].value_counts().sum()
ultrapassou_trinta_e_seis_horas = tabela.loc[tabela['Tempo de solução em minutos'] > 2160].value_counts().sum()
em_compliance_trinta_e_seis_horas = tabela.loc[tabela['Tempo de solução em minutos'] <= 2160].value_counts().sum()

# Total de chamados abertos, finalizados e pendentes
qtde_de_chamados = tabela['Estado'].value_counts().sum()
finalizados = tabela.loc[tabela['Estado'] == 'Finalizado com êxito'].value_counts().sum()
qtde_de_pendentes_do_mes = 0
pendentes_do_mes = tabela['Estado'] != 'Finalizado com êxito'
for pendente in pendentes_do_mes:
    if pendente == True:
        qtde_de_pendentes_do_mes += 1

# Técnicos
airanildo = tabela.loc[tabela['Atendente/Proprietário'] == 'airanildo.lima', ['Atendente/Proprietário', 'Criado', 'Primeira Resposta', 'Primeira Resposta em Minutos', 'Tempo de solução em minutos']]
thiago = tabela.loc[tabela['Atendente/Proprietário'] == 'thiago.gomes', ['Atendente/Proprietário', 'Criado', 'Primeira Resposta', 'Primeira Resposta em Minutos', 'Tempo de solução em minutos']]

# Chamados por setores
por_setor = tabela[['ID do Cliente', 'Ticket#']].groupby(['ID do Cliente']).count()
por_setor.sort_values(by=['ID do Cliente','Ticket#'], ascending=False)

# Serviços
servico = tabela['Serviço'].value_counts()
servicos_porcentagem = tabela['Serviço'].value_counts(normalize=True).map("{:.1%}".format)

# Até 10 minutos
chamados_estourados_no_inicio_do_atendimento = tabela.loc[
    tabela['Primeira Resposta em Minutos'] > 10].value_counts().sum()
em_compliance_ate_10_minutos = tabela.loc[tabela['Primeira Resposta em Minutos'] <= 10].value_counts().sum()
porcentagem_estourados_10_minutos = 100 - (chamados_estourados_no_inicio_do_atendimento * 100) / qtde_de_chamados

# Até 1 hora
porcentagem_estourados_1_hora = 100 - (ultrapassou_uma_hora * 100) / qtde_de_chamados

# Até 3 horas
porcentagem_estourados_3_hora = 100 - (ultrapassou_tres_horas * 100) / qtde_de_chamados

# Até 36 horas
porcentagem_estourados_36_horas = 100 - (ultrapassou_trinta_e_seis_horas * 100) / qtde_de_chamados

# Enviar email
outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)
email.To = "rhuan.nasser@iti.gov.br; rhuannasser123456@gmail.com; rhuan_nasser@outlook.com"
email.Subject = "Informações OTRS"
email.Body = f'''

                                Informações Gerais: 

Foram abertos {qtde_de_chamados} chamados do dia 1/{mes}/{ano} até o dia {dia}/{mes}/{ano}.
Foram finalizados {finalizados} chamados e {qtde_de_pendentes_do_mes} ainda não foram finalizados.


----------------------------------------------------------------------------------------------------
Início do atendimento <= 10 minutos:

                                 Meta: >= 90%

Quantidade de chamados em compliance: {em_compliance_ate_10_minutos} chamado(s)
Quantidade de chamados estourados:  {chamados_estourados_no_inicio_do_atendimento} chamado(s)
Media do tempo dos atendimentos em até 10 minutos:  {media_10_minutos} Segundos
Meta atual: {porcentagem_estourados_10_minutos:.0f}%

----------------------------------------------------------------------------------------------------
Chamados resolvidos em até 1 hora: 

                                 Meta: >= 75%

Quantidade de chamados em compliance: {em_compliance_uma_hora} chamado(s)
Quantidade de chamados estourados: {ultrapassou_uma_hora} chamado(s)
Meta atual: {porcentagem_estourados_1_hora:.0f}%
----------------------------------------------------------------------------------------------------
Chamados resolvidos em até 3 horas: 

                                 Meta: >= 95%

Quantidade de chamados em compliance: {em_compliance_tres_horas} chamado(s)
Quantidade de chamados estourados: {ultrapassou_tres_horas} chamado(s)
Meta atual: {porcentagem_estourados_3_hora:.0f}%

----------------------------------------------------------------------------------------------------
Chamados resolvidos em até 36 horas: 

                                 Meta: >= 100%

Quantidade de chamados em compliance: {em_compliance_trinta_e_seis_horas} chamado(s)
Quantidade de chamados estourados: {ultrapassou_trinta_e_seis_horas} chamado(s)
Meta atual: {porcentagem_estourados_36_horas:.0f}%

----------------------------------------------------------------------------------------------------
Segue em anexo a base de dados completa para análise adicional.




Atenciosamente,
Equipe de Atendimento ao Usuário
{emoji.emojize(":telephone_receiver:(61) 9999-9999   :computer:", use_aliases=True)}'''

# Exportando para arquivos .xlsx
tabela.to_excel(fr"C:\Users\nasser\OneDrive\Área de Trabalho\Relatório diário detalhado\Chamados.xlsx", index=False)
airanildo.to_excel(fr"C:\Users\nasser\OneDrive\Área de Trabalho\Relatório diário detalhado\Chamados Atendidos por Airanildo.xlsx", index=False)
thiago.to_excel(fr"C:\Users\nasser\OneDrive\Área de Trabalho\Relatório diário detalhado\Chamados Atendidos por Thiago.xlsx", index=False)

# Anexando o arquivo
email.Attachments.Add(r'C:\Users\nasser\OneDrive\Área de Trabalho\Relatório diário detalhado\Chamados.xlsx')
email.Attachments.Add(r'C:\Users\nasser\OneDrive\Área de Trabalho\Relatório diário detalhado\Chamados Atendidos por Airanildo.xlsx')
email.Attachments.Add(r'C:\Users\nasser\OneDrive\Área de Trabalho\Relatório diário detalhado\Chamados Atendidos por Thiago.xlsx')

# Enviando o e-mail
email.Send()

# Exclui a planilha do relatório
os.system(r'del /f /a C:\Users\nasser\Downloads\relatorio.xlsx')
