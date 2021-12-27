import pandas as pd, datetime, time, os, win32com.client as win32, matplotlib.pyplot as plt, zipfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl
from confidencial import senha, email, otrs

# Variáveis
mes = str(datetime.date.today().month)
ano = str(datetime.date.today().year)
dia = str(datetime.date.today().day)
completo = str(time.ctime())
hora = completo[11:13]
minuto = completo[14:16]

# Chrome Driver
web = webdriver.Chrome()
web.get(otrs)
web.find_element_by_id('User').send_keys(email[:12])
web.find_element_by_id('Password').send_keys(senha, Keys.ENTER)
web.maximize_window()

# Faz o download do relatório do Suporte
web.get(f'{otrs}?Action=AgentStatistics;Subaction=View;StatID=13')
web.find_element_by_xpath('//*[@id="Format_Search"]').click()
sl(1)
web.find_element_by_xpath('/html/body/div[3]/div[1]/div/ul/li[2]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCloseTimeStartMonth"]/option[{mes}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCloseTimeStartYear"]/option[{ano[2:]}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCloseTimeStopDay"]/option[{dia}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCloseTimeStopMonth"]/option[{mes}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCloseTimeStopYear"]/option[{ano[2:]}]').click()
web.find_element_by_xpath(f'//*[@id="StartStatistic"]/span').click()
sl(5)

# Renomeia o arquivo
os.system(fr'rename C:\Users\rhuan\Downloads\Rel*.xlsx suporte_relatorio_total.xlsx')

# Faz o download do relatório do início do atendimento do Suporte
web.get(f'{otrs}?Action=AgentStatistics;Subaction=View;StatID=15')
web.find_element_by_xpath('//*[@id="Format_Search"]').click()
sl(1)
web.find_element_by_xpath('/html/body/div[3]/div[1]/div/ul/li[2]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCloseTimeStartMonth"]/option[{mes}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCloseTimeStartYear"]/option[{ano[2:]}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCloseTimeStopDay"]/option[{dia}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCloseTimeStopMonth"]/option[{mes}]').click()
web.find_element_by_xpath(f'//*[@id="UseAsRestrictionCloseTimeStopYear"]/option[{ano[2:]}]').click()
web.find_element_by_xpath(f'//*[@id="StartStatistic"]/span').click()
sl(3)
web.find_element_by_xpath('//*[@id="ToolBar"]/li/a').click()
web.find_element_by_id('LogoutButton').click()
web.close()

# Renomeia o arquivo
os.system(fr'rename C:\Users\rhuan\Downloads\Rel*.xlsx suporte_relatorio_inicio_do_atendimento.xlsx')

# Tratamento dos dados
tabela = pd.read_excel(fr'C:\Users\rhuan\Downloads\suporte_relatorio_total.xlsx')
tabela10min = pd.read_excel(fr'C:\Users\rhuan\Downloads\suporte_relatorio_inicio_do_atendimento.xlsx')
#headers = rel.iloc[0]
#tabela = pd.DataFrame(rel.values[1:], columns=headers)
tabela['Tempo de solução em minutos'] = tabela['Tempo de solução em minutos'].astype(int)
tabela['Primeira Resposta em Minutos'] = tabela['Primeira Resposta em Minutos'].astype(int)
tabela['Delta de tempo de solução em minutos'] = tabela['Delta de tempo de solução em minutos'].astype(int)
tabela10min['Tempo de solução em minutos'] = tabela['Tempo de solução em minutos'].astype(int)
tabela10min['Primeira Resposta em Minutos'] = tabela['Primeira Resposta em Minutos'].astype(int)
tabela10min['Delta de tempo de solução em minutos'] = tabela['Delta de tempo de solução em minutos'].astype(int)

# Chamados de 10 miunutos estourados por técnico
estourado_10_minutos_airanildo= tabela10min[['Ticket#', 'Usuário Cliente', 'Primeira Resposta em Minutos']].loc[(tabela10min['Atendente/Proprietário'] == 'Airanildo Alves de Lima') & (tabela10min['Primeira Resposta em Minutos'] >= 10)]
estourado_10_minutos_italo = tabela10min[['Ticket#', 'Usuário Cliente', 'Primeira Resposta em Minutos']].loc[(tabela10min['Atendente/Proprietário'] == 'Italo Torres de Oliveira') & (tabela10min['Primeira Resposta em Minutos'] >= 10)]

if not estourado_10_minutos_airanildo.empty:
    html10min_airanildo = estourado_10_minutos_airanildo.to_html()
else:
    html10min_airanildo = 'Não há chamados estourados!'

if not estourado_10_minutos_italo.empty:
    html10min_italo = estourado_10_minutos_italo.to_html()
else:
    html10min_italo = 'Não há chamados estourados!'

# Chamados de 1 ou mais horas estourados por técnico
estourado_1_hora_airanildo = tabela[['Ticket#', 'Usuário Cliente', 'Delta de tempo de solução em minutos']].loc[(tabela['Atendente/Proprietário'] == 'Airanildo Alves de Lima') & (tabela['Delta de tempo de solução em minutos'] < 0)]
estourado_1_hora_italo = tabela[['Ticket#', 'Usuário Cliente', 'Delta de tempo de solução em minutos']].loc[(tabela['Atendente/Proprietário'] == 'Italo Torres de Oliveira') & (tabela['Delta de tempo de solução em minutos'] < 0)]

if not estourado_1_hora_airanildo.empty:
    html1hora_airanildo = estourado_1_hora_airanildo.to_html()
else:
    html1hora_airanildo = 'Não há chamados estourados!'

if not estourado_1_hora_italo.empty:
    html1hora_italo = estourado_1_hora_italo.to_html()
else:
    html1hora_italo = 'Não há chamados estourados!'

# Quantidade de chamados estourados (Até 10 minutos)
ate_10 = tabela[['Ticket#', 'Atendente/Proprietário', 'Primeira Resposta em Minutos', 'Criado', 'Primeira Resposta']].loc[tabela['Primeira Resposta em Minutos'] > 10]

if not ate_10.empty:
    ate_10.to_excel('C:/Users/rhuan/OneDrive/Documentos/Relatório/chamados estourados de 10 minutos.xlsx')
    html10min = ate_10.to_html()
else:
    pass

# Quantidade de chamados estourados (Até 1 hora)
ate_1 = tabela[['Ticket#', 'Atendente/Proprietário', 'Tempo de solução em minutos', 'Criado', 'Primeira Resposta', 'Delta de tempo de solução em minutos']].loc[(tabela['Delta de tempo de solução em minutos'] < 0) & (tabela['Tempo de solução em minutos'] != 0)]

if not ate_1.empty:
    ate_1.to_excel('C:/Users/rhuan/OneDrive/Documentos/Relatório/chamados estourados de 1 hora.xlsx')
    html1hora = ate_1.to_html()
else:
    pass

# Quantidade de chamados estourados (Até 3 horas)
ate_3 = tabela[['Ticket#', 'Atendente/Proprietário', 'Tempo de solução em minutos', 'Criado', 'Primeira Resposta', 'Delta de tempo de solução em minutos']].loc[tabela['Delta de tempo de solução em minutos'] < -120]

if not ate_3.empty:
    ate_3.to_excel('C:/Users/rhuan/OneDrive/Documentos/Relatório/chamados estourados de 3 horas.xlsx')
    html3horas = ate_3.to_html()
else:
    pass

# Quantidade de chamados estourados (Até 36 horas)
ate_36 = tabela[['Ticket#', 'Atendente/Proprietário', 'Tempo de solução em minutos', 'Criado', 'Primeira Resposta', 'Delta de tempo de solução em minutos']].loc[tabela['Delta de tempo de solução em minutos'] < -2100]

if not ate_36.empty:
    ate_36.to_excel('C:/Users/rhuan/OneDrive/Documentos/Relatório/chamados estourados de 36 horas.xlsx', ascending=False)
    html36horas = ate_36.to_html()
else:
    pass

# Agrupados por (Tipo)
#tipo = tabela[['Tipo','Ticket#']].groupby('Tipo').count().sort_values(by=['Ticket#'], ascending=False)
#qtde_incidentes_requisicoes = list(tabela['Tipo'].value_counts())

#fig = plt.figure(figsize=(10, 10))
#ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#labels = 'Incidentes', 'Requisições'
#fracs = qtde_incidentes_requisicoes
#explode = (0, 0.05)
#pies1 = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
#Title = plt.title('TIPO')
#plt.savefig('C:/Users/rhuan/OneDrive/Documentos/Relatório/Tickets por tipo.jpeg', format='jpeg')

# Agrupados por (Serviço)
servico = tabela[['Serviço','Ticket#']].groupby('Serviço').count().sort_values(by=['Ticket#'], ascending=False)
servico.to_excel('C:/Users/rhuan/OneDrive/Documentos/Relatório/Por serviço.xlsx')
html_servicos = servico.to_html()

# Agrupados por (Setor)
setor = tabela[['ID do Cliente','Ticket#']].groupby('ID do Cliente').count().sort_values(by=['Ticket#'], ascending=False)
setor.to_excel('C:/Users/rhuan/OneDrive/Documentos/Relatório/Por setor.xlsx')
html_setor = setor.to_html()

# Agrupados por (Usuários)
usuarios = tabela[['Usuário Cliente','Ticket#']].groupby('Usuário Cliente').count().sort_values(by=['Ticket#'], ascending=False)
usuarios.to_excel('C:/Users/rhuan/OneDrive/Documentos/Relatório/Por usuario.xlsx')
html_usuarios = usuarios.to_html()

# Agrupados por (Estado)
estado = tabela[['Estado', 'Ticket#']].groupby('Estado').count().sort_values(by=['Ticket#'], ascending=False)
estado.to_excel('C:/Users/rhuan/OneDrive/Documentos/Relatório/Por estado.xlsx')
html_estado = estado.to_html()

# Agrupados por (Tipo)
tipo = tabela[['Tipo', 'Ticket#']].groupby('Tipo').count().sort_values(by=['Ticket#'], ascending=False)
tipo.to_excel('C:/Users/rhuan/OneDrive/Documentos/Relatório/Por estado.xlsx')
html_tipo = tipo.to_html()

# Coleta de informações para os gráficos
correto_10 = tabela10min.loc[tabela10min['Primeira Resposta em Minutos'] <= 10]
nao_correto_10 = tabela10min.loc[tabela10min['Primeira Resposta em Minutos'] > 10]

# Transforma a coluna Delta em str
#tabela['Delta de tempo de solução em minutos'] = tabela['Delta de tempo de solução em minutos'].astype(str)

# Transforma a coluna Delta em int novamente
#tabela['Delta de tempo de solução em minutos'] = tabela['Delta de tempo de solução em minutos'].astype(int)

correto_60 = tabela.loc[tabela['Delta de tempo de solução em minutos'] >= 0]
nao_correto_60 = tabela.loc[tabela['Delta de tempo de solução em minutos'] < 0]

correto_180 = tabela.loc[tabela['Delta de tempo de solução em minutos'] >= -120]
nao_correto_180 = tabela.loc[tabela['Delta de tempo de solução em minutos'] < -120]

correto_2160 = tabela.loc[tabela['Delta de tempo de solução em minutos'] > -2100]
nao_correto_2160 = tabela.loc[tabela['Delta de tempo de solução em minutos'] <= -2100]

encerrado_por_airanildo = tabela.loc[tabela['Atendente/Proprietário'] == 'Airanildo Alves de Lima']
encerrado_por_italo = tabela.loc[tabela['Atendente/Proprietário'] == 'Italo Torres de Oliveira']

c60 = correto_60.value_counts().sum()
nc60 = nao_correto_60.value_counts().sum()
c10 = correto_10.value_counts().sum()
nc10 = nao_correto_10.value_counts().sum()
c180 = correto_180.value_counts().sum()
nc180 = nao_correto_180.value_counts().sum()
c2160 = correto_2160.value_counts().sum()
nc2160 = nao_correto_2160.value_counts().sum()
ea = encerrado_por_airanildo.value_counts().sum()
ei = encerrado_por_italo.value_counts().sum()

qtde_incidentes_requisicoes = list(tabela['Tipo'].value_counts())


# Até 10 minutos
fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
labels = 'Em compliance', 'Vencido'
fracs = c10, nc10
explode = (0, 0.05)
pies = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
Title = plt.title('ATÉ 10 MINUTOS')
plt.savefig('C:/Users/rhuan/OneDrive/Documentos/Relatório/Até 10 minutos.jpeg', format='jpeg')

# Até 60 minutos
fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
labels = 'Em compliance', 'Vencido'
fracs = c60, nc60
explode = (0, 0.05)
pies1 = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
Title = plt.title('ATÉ 1 HORA')
plt.savefig('C:/Users/rhuan/OneDrive/Documentos/Relatório/ate1hora.jpeg', format='jpeg')

# Até 3 horas
fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
labels = 'Em compliance', 'Vencido'
fracs = c180, nc180
explode = (0, 0.05)
pies1 = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
Title = plt.title('ATÉ 3 HORAS')
plt.savefig('C:/Users/rhuan/OneDrive/Documentos/Relatório/Até 3 horas.jpeg', format='jpeg')

# Até 36 horas
fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
labels = 'Em compliance', 'Vencido'
fracs = c2160, nc2160
explode = (0, 0.05)
pies1 = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
Title = plt.title('ATÉ 36 HORAS')
plt.savefig('C:/Users/rhuan/OneDrive/Documentos/Relatório/Até 36 horas.jpeg', format='jpeg')

# Por Serviço (Total):
servico['Ticket#'].sum()

# TOP 10 Usuários
top10 = usuarios.head(10).sort_values(by=['Ticket#'], ascending=True).plot.barh(width=0.7)
plt.savefig('C:/Users/rhuan/OneDrive/Documentos/Relatório/TOP 10.jpeg', dpi = 300, bbox_inches='tight', format='jpeg')

# CHAMADOS ENCERRADOS CORRETAMENTE E INCORRETAMENTE
fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
labels = 'Encerrado por Airanildo', 'Encerrado por Ítalo'
fracs = ea, ei
explode = (0, 0.05)
pies = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
Title = plt.title('CHAMADO ENCERRADO POR TÉCNICO')
plt.savefig('C:/Users/rhuan/OneDrive/Documentos/Relatório/CHAMADO ENCERRADO POR TÉCNICO.jpeg', format='jpeg')

# Lista os diretórios e joga eles em uma lista
Arquivos_relatorio = os.listdir('C:/Users/rhuan/OneDrive/Documentos/Relatório')

# Zipa a pasta com o conteúdo da lista obtida acima
z = zipfile.ZipFile('C:/Users/rhuan/OneDrive/Documentos/Relatório/relatorio.zip', 'w', zipfile.ZIP_DEFLATED)
for arquivo in Arquivos_relatorio:
    if 'relatorio' not in arquivo:
        z.write(fr'C:/Users/rhuan/OneDrive/Documentos/Relatório/{arquivo}')
    else:
        pass

z.close()

# Cria a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# Cria um e-mail
email = outlook.CreateItem(0)

# Configura as informações do seu e-mail
email.To = "rhuan.nasser@iti.gov.br"
email.Subject = "Informações sobre a Equipe de Suporte do ITI"
email.HTMLBody = fr"""
<p><h3>Prezado <strong>Rhuan</strong>,</h3></p>
    <p><h3>&emsp;Segue abaixo e em anexo informações úteis para a análise do atendimento do suporte!</h3></p><br>

    <center><strong><h1>Quantidade de Chamados Abertos por Setor</h1></strong><br><\center>
    <center><strong>{html_setor}</strong><br><\center><br> 

    <center><strong><h1>Quantidade de Chamados Abertos por Usuário<\h1></strong></center>
    <center><strong>{html_usuarios}</strong></center><br>

    <center><strong><h1>Serviços Utilizados do Catálogo pelos Usuários do mês atual<\h1></strong></center>
    <center><strong><h1>{html_servicos}<\h1></strong></center><br> 

    <center><strong><h1>Quantidade de Chamados Encerrados<\h1></strong></center>
    <center><strong><h1>{html_estado}<\h1></strong></center><br>

    <center><strong><h1>Classificados por Tipo<\h1></strong></center>
    <center><strong><h1>{html_tipo}<\h1></strong></center><br> 
    
    <center><strong><h1>Chamados estourados no início do atendimento<\h1></strong></center>
    <center><strong><h3>Airanildo: {html10min_airanildo}<\h3></strong></center>
    <center><strong><h3>Ítalo: {html10min_italo}<\h3></strong></center><br> 
    
    <center><strong><h1>Chamados estourados com mais de 1 hora de atendimento<\h1></strong></center> 
    <center><strong><h3>Airanildo: {html1hora_airanildo}<\h3></strong></center>
    <center><strong><h3>Ítalo: {html1hora_italo}<\h3></strong></center><br>
    
    <p><strong><h3>Atenciosamente,</h3></strong></p>
    <p>&nbsp;</p>
<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="padding: 1.5pt 1.5pt 1.5pt 1.5pt;"><a href="http://www.iti.gov.br/"><img src="http://www.iti.gov.br/images/icones-email/logo-iti.png" alt="ITI - Instituto
                Nacional de Tecnologia da Informa&ccedil;&atilde;o" width="129" height="60" border="0" /></a></td>
<td style="padding: 1.5pt 1.5pt 1.5pt 1.5pt;">
<p class="MsoNormal"><span style="font-size: 13.5pt; font-family: 'Times New Roman','serif'; color: black; mso-fareast-language: PT-BR;">&nbsp;</span></p>
</td>
<td style="padding: 1.5pt 1.5pt 1.5pt 5.25pt;" rowspan="2">
<p class="MsoNormal"><span style="color: #19295a;"><strong><span style="font-size: 8.5pt; font-family: 'Tahoma','sans-serif';"> BOT </span></strong></span><span style="font-size: 8.5pt; font-family: 'Tahoma','sans-serif'; color: #002a4e; mso-fareast-language: PT-BR;"><span style="color: #19295a;">| COTIC <br /> CARGO | Robô | COTIC <br /> Casa Civil - Presid&ecirc;ncia da Rep&uacute;blica<br /> +55 61 3424-3833-<br /> SCN Quadra 2 bloco E<br /> 70712-905</span></span><span style="font-size: 8.5pt; font-family: 'Tahoma','sans-serif'; color: #002a4e; mso-fareast-language: PT-BR;"><span style="color: #19295a;"><span style="color: #19295a;"><span style="font-size: 8.5pt; font-family: 'Tahoma','sans-serif';"> </span></span><span style="font-size: 8.5pt; font-family: 'Tahoma','sans-serif'; color: #002a4e; mso-fareast-language: PT-BR;"><span style="color: #19295a;">| </span></span>Bras&iacute;lia/DF</span></span></p>
</td>
</tr>
<tr>
<td style="padding: 1.5pt 1.5pt 1.5pt 1.5pt;">
<p class="MsoNormal" style="text-align: center;" align="center"><a href="https://www.facebook.com/itigovbr"><span style="font-size: 13.5pt; font-family: 'Times NewRoman','serif'; color: blue; mso-fareast-language: PT-BR; text-decoration: none;"><img id="Imagem_x0020_2" src="http://www.iti.gov.br/images/icones-email/facebook.png" alt="Descri&ccedil;&atilde;o: Facebook" width="8" height="13" border="0" /></span></a><span style="font-size: 13.5pt; font-family: 'Times New Roman','serif'; color: black; mso-fareast-language: PT-BR;">&nbsp;&nbsp;&nbsp;</span><a href="https://instagram.com/itigovbr"><span style="font-size: 13.5pt; font-family: 'Times NewRoman','serif'; color: blue; mso-fareast-language: PT-BR; text-decoration: none;"><img id="Imagem_x0020_3" src="http://www.iti.gov.br/images/icones-email/instagram.png" alt="Descri&ccedil;&atilde;o: Instagram" width="14" height="14" border="0" /></span></a><span style="font-size: 13.5pt; font-family: 'Times New Roman','serif'; color: black; mso-fareast-language: PT-BR;">&nbsp;&nbsp;&nbsp;</span><a href="https://twitter.com/itigovbr"><span style="font-size: 13.5pt; font-family: 'Times NewRoman','serif'; color: blue; mso-fareast-language: PT-BR; text-decoration: none;"><img id="Imagem_x0020_4" src="http://www.iti.gov.br/images/icones-email/twitter.png" alt="Descri&ccedil;&atilde;o: Twitter" width="16" height="13" border="0" /></span></a><span style="font-size: 13.5pt; font-family: 'Times New Roman','serif'; color: black; mso-fareast-language: PT-BR;">&nbsp;&nbsp;&nbsp;</span><a href="https://youtube.com/user/itidigital"><span style="font-size: 13.5pt; font-family: 'Times NewRoman','serif'; color: blue; mso-fareast-language: PT-BR; text-decoration: none;"><img id="Imagem_x0020_5" src="http://www.iti.gov.br/images/icones-email/youtube.png" alt="Descri&ccedil;&atilde;o: YouTube" width="11" height="13" border="0" /></span></a><span style="font-size: 13.5pt; font-family: 'Times New Roman','serif'; color: black; mso-fareast-language: PT-BR;">&nbsp;&nbsp;&nbsp;</span><a href="https://www.iti.gov.br/noticias/17-indice-de-noticias"><span style="font-size: 13.5pt; font-family: 'Times NewRoman','serif'; color: blue; mso-fareast-language: PT-BR; text-decoration: none;"><img id="Imagem_x0020_6" src="http://www.iti.gov.br/images/icones-email/rss.png" alt="Descri&ccedil;&atilde;o: Blog" width="13" height="13" border="0" /></span></a><span style="font-size: 13.5pt; font-family: 'Times New Roman','serif'; color: black; mso-fareast-language: PT-BR;"></span></p>
</td>
<td style="padding: 1.5pt 1.5pt 1.5pt 1.5pt;">
<p class="MsoNormal"><span style="font-size: 13.5pt; font-family: 'Times New Roman','serif'; color: black; mso-fareast-language: PT-BR;">&nbsp;</span></p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>

"""
anexo = 'C:/Users/rhuan/OneDrive/Documentos/Relatório/relatorio.zip'
email.Attachments.Add(anexo)
email.Send()

# Exclui a planilha do relatório
os.system(r'del /f /a C:\Users\rhuan\Downloads\suporte_relatorio_inicio_do_atendimento.xlsx')
os.system(r'del /f /a C:\Users\rhuan\Downloads\suporte_relatorio_total.xlsx')
os.system(r'del /f /a C:\Users\rhuan\OneDrive\Documentos\Relatório\relatorio.zip')
