import os

# Retorna informações sobre o sistema operacional, como: arquitetura, tipo de sistema operacional, nome do computador, versão do kernel e uptime.
import stat

print(f"SO: {os.uname()[0]}")
print(f"Nome do Computador: {os.uname()[1]}")
print(f"Versão do Kernel: {os.uname()[2]}")
print(f"Versão do SO, hora e outros: {os.uname()[3]}")

# retorna o terminal atual
print(os.ctermid())

# retorna as variáveis de ambiente
print(os.environ)
'''
retorna o valor se for True a condição. Segue abaixo exemplo

os.F_OK
os.R_OK¶
os.W_OK
os.X_OK
'''

if os.access("/home/nasser/PycharmProjects/py/python/monitoramento_de_chamados_e_alerta_sonoro.py", os.W_OK):
    with open("monitoramento_de_chamados_e_alerta_sonoro.py") as fp:
        print(fp.read())

# Acessa o diretório especificado
os.chdir('/home/nasser')

# transformar octal em decimal para o uso, o chmod faz a troca de permissão nas pastas e/ou arquivos
os.chmod('/home/nasser/teste', 457)

# executa um comando qualquer do Sistema operacional
os.system('ls -l /home/nasser/teste')

# troca o dono e o grupo do arquivo
os.chown('/home/nasser/teste', 1000, 1000)
os.system('ls -l /home/nasser/teste')

# altera o diretório raiz
#os.chroot("/home/nasser")

# Retorna o diretório atual. Faz a mesma coisa que o pwd
print(os.getcwd())

# inclui todos os arquivos e diretórios em uma lista
print(os.listdir())

