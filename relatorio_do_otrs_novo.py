#!/usr/bin/env python
# coding: utf-8

# # Bibliotecas

# In[235]:


import pandas as pd, datetime, time, os
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl


# # Variáveis

# In[236]:


mes = str(datetime.date.today().month)
ano = str(datetime.date.today().year)
dia = str(datetime.date.today().day)
completo = str(time.ctime())
hora = completo[11:13]
minuto = completo[14:16]


# # Chrome Driver

# In[237]:


web = webdriver.Chrome('/home/nasser/Documentos/chromedriver')
web.get('http://urubu.in.iti.gov.br/otrs/index.pl')
web.find_element_by_id('User').send_keys('<>')
web.find_element_by_id('Password').send_keys('<>', Keys.ENTER)
web.maximize_window()


# # Acesso aos relatórios

# In[238]:


web.find_element_by_xpath('//*[@id="nav-Reports"]/a').click()
web.find_element_by_xpath('//*[@id="nav-Reports-Statistics"]/a').click()
web.find_element_by_xpath('//*[@id="AppWrapper"]/div[3]/div[2]/div/div[2]/table/tbody/tr[19]/td[6]/a').click()


# # Altera a data de acordo com a data atual para a extração

# In[239]:


web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCreateTimeStartMonth"]/option[{mes}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCreateTimeStartYear"]/option[{ano[2:]}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCreateTimeStopDay"]/option[{dia}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCreateTimeStopMonth"]/option[{mes}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCreateTimeStopYear"]/option[{ano[2:]}]').click()
web.find_element_by_xpath(f'//*[@id="StartStatistic"]/span').click()
sl(3)
web.close()


# # Renomeia o arquivo

# In[240]:


os.system(r'mv /home/nasser/Downloads/Relatório_*.xlsx /home/nasser/Downloads/relatorio.xlsx')


# # Tratamento dos dados

# In[241]:


rel = pd.read_excel('/home/nasser/Downloads/relatorio.xlsx')
headers = rel.iloc[0]
tabela = pd.DataFrame(rel.values[1:], columns=headers)
tabela['Tempo de solução em minutos'] = tabela['Tempo de solução em minutos'].astype(int)
tabela['Primeira Resposta em Minutos'] = tabela['Primeira Resposta em Minutos'].astype(int)
tabela['Delta de tempo de solução em minutos'] = tabela['Delta de tempo de solução em minutos'].astype(int)


# # Quantidade de chamados estourados (Até 10 minutos)

# In[242]:


ate_10 = tabela[['Ticket#', 'Atendente/Proprietário', 'Primeira Resposta em Minutos', 'Criado', 'Primeira Resposta']].loc[tabela['Primeira Resposta em Minutos'] > 10]

if not ate_10.empty:
    ate_10.to_excel('/home/nasser/Área de Trabalho/Relatório/chamados estourados de 10 minutos.xlsx')
else:
    pass


# # Quantidade de chamados estourados (Até 1 hora)
# 

# In[243]:


ate_1 = tabela[['Ticket#', 'Atendente/Proprietário', 'Tempo de solução em minutos', 'Criado', 'Primeira Resposta', 'Delta de tempo de solução em minutos']].loc[(tabela['Delta de tempo de solução em minutos'] < 0) & (tabela['Tempo de solução em minutos'] != 0)]

if not ate_1.empty:
    ate_1.to_excel('/home/nasser/Área de Trabalho/Relatório/chamados estourados de 1 hora.xlsx')
else:
    pass


# # Quantidade de chamados estourados (Até 3 horas)

# In[244]:


ate_3 = tabela[['Ticket#', 'Atendente/Proprietário', 'Tempo de solução em minutos', 'Criado', 'Primeira Resposta', 'Delta de tempo de solução em minutos']].loc[tabela['Delta de tempo de solução em minutos'] < -120]

if not ate_3.empty:
    ate_3.to_excel('/home/nasser/Área de Trabalho/Relatório/chamados estourados de 3 horas.xlsx')
else:
    pass


# # Quantidade de chamados estourados (Até 36 horas)

# In[245]:


ate_36 = tabela[['Ticket#', 'Atendente/Proprietário', 'Tempo de solução em minutos', 'Criado', 'Primeira Resposta', 'Delta de tempo de solução em minutos']].loc[tabela['Delta de tempo de solução em minutos'] < -2100]

if not ate_36.empty:
    ate_36.to_excel('/home/nasser/Área de Trabalho/Relatório/chamados estourados de 36 horas.xlsx', ascending=False)
else:
    pass


# # Agrupados por (Tipo)

# In[246]:


tipo = tabela[['Tipo','Ticket#']].groupby('Tipo').count().sort_values(by=['Ticket#'], ascending=False)
tipo


# In[247]:


qtde_incidentes_requisicoes = list(tabela['Tipo'].value_counts())

fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

labels = 'Incidentes', 'Requisições'
fracs = qtde_incidentes_requisicoes
explode = (0, 0.05)
pies1 = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
Title = plt.title('TIPO')
plt.savefig('/home/nasser/Área de Trabalho/Relatório/Tickets por tipo.pdf', format='pdf')


# # Agrupados por (Serviço)

# In[248]:


servico = tabela[['Serviço','Ticket#']].groupby('Serviço').count().sort_values(by=['Ticket#'], ascending=False)
servico.to_excel('/home/nasser/Área de Trabalho/Relatório/Por serviço.xlsx')


# # Agrupados por (Setor)

# In[249]:


setor = tabela[['ID do Cliente','Ticket#']].groupby('ID do Cliente').count().sort_values(by=['Ticket#'], ascending=False)
setor.to_excel('/home/nasser/Área de Trabalho/Relatório/Por setor.xlsx')


# # Agrupados por (Usuários)

# In[250]:


usuarios = tabela[['Usuário Cliente','Ticket#']].groupby('Usuário Cliente').count().sort_values(by=['Ticket#'], ascending=False)
usuarios.to_excel('/home/nasser/Área de Trabalho/Relatório/Por usuario.xlsx')


# # Agrupados por (Estado)

# In[251]:


estado = tabela[['Estado', 'Ticket#']].groupby('Estado').count().sort_values(by=['Ticket#'], ascending=False)
estado.to_excel('/home/nasser/Área de Trabalho/Relatório/Por estado.xlsx')


# # Coleta de informações para os gráficos

# In[252]:


correto_10 = tabela.loc[tabela['Primeira Resposta em Minutos'] <= 10]
nao_correto_10 = tabela.loc[tabela['Primeira Resposta em Minutos'] > 10]

# Transforma a coluna Delta em str
tabela['Delta de tempo de solução em minutos'] = tabela['Delta de tempo de solução em minutos'].astype(str)

# Transforma a coluna Delta em int novamente
tabela['Delta de tempo de solução em minutos'] = tabela['Delta de tempo de solução em minutos'].astype(int)

correto_60 = tabela.loc[tabela['Delta de tempo de solução em minutos'] >= 0]
nao_correto_60 = tabela.loc[tabela['Delta de tempo de solução em minutos'] < 0]

correto_180 = tabela.loc[tabela['Delta de tempo de solução em minutos'] >= -120]
nao_correto_180 = tabela.loc[tabela['Delta de tempo de solução em minutos'] < -120]

correto_2160 = tabela.loc[tabela['Delta de tempo de solução em minutos'] > -2100]
nao_correto_2160 = tabela.loc[tabela['Delta de tempo de solução em minutos'] <= -2100]


c60 = correto_60.value_counts().sum()
nc60 = nao_correto_60.value_counts().sum()
c10 = correto_10.value_counts().sum()
nc10 = nao_correto_10.value_counts().sum()
c180 = correto_180.value_counts().sum()
nc180 = nao_correto_180.value_counts().sum()
c2160 = correto_2160.value_counts().sum()
nc2160 = nao_correto_2160.value_counts().sum()
qtde_incidentes_requisicoes = list(tabela['Tipo'].value_counts())


# # Até 10 minutos

# In[253]:


fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

labels = 'Em compliance', 'Vencido'
fracs = c10, nc10
explode = (0, 0.05)

pies = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
Title = plt.title('ATÉ 10 MINUTOS')
plt.savefig('/home/nasser/Área de Trabalho/Relatório/Até 10 minutos', format='jpeg')


# # Até 60 minutos

# In[254]:


fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

labels = 'Em compliance', 'Vencido'
fracs = c60, nc60
explode = (0, 0.05)

pies1 = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
Title = plt.title('ATÉ 1 HORA')
plt.savefig('/home/nasser/Área de Trabalho/Relatório/Até 1 hora', format='jpeg')


# # Até 3 horas

# In[255]:


fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

labels = 'Em compliance', 'Vencido'
fracs = c180, nc180
explode = (0, 0.05)
pies1 = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
Title = plt.title('ATÉ 3 HORAS')
plt.savefig('/home/nasser/Área de Trabalho/Relatório/Até 3 horas', format='jpeg')


# # Até 36 horas

# In[256]:


fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
labels = 'Em compliance', 'Vencido'
fracs = c2160, nc2160
explode = (0, 0.05)
pies1 = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
Title = plt.title('ATÉ 36 HORAS')
plt.savefig('/home/nasser/Área de Trabalho/Relatório/Até 36 horas', format='jpeg')


# # Por Serviço (Total):

# In[257]:


servico['Ticket#'].sum()


# # TOP 10 Usuários

# In[258]:


top10 = usuarios.head(10).sort_values(by=['Ticket#'], ascending=True).plot.barh(width=0.7)
#plt.figure(figsize=(20,18))
plt.savefig('/home/nasser/Área de Trabalho/Relatório/TOP 10', dpi = 300, bbox_inches='tight', format='jpeg')


# # Exclui a planilha do relatório
# 

# In[259]:


os.system(r'rm -rf /home/nasser/Downloads/relatorio.xlsx')
