from lib.interface import *
from lib.toConect import *
from time import sleep

conexao = mysql.connector.connect(database='',
                                  host='localhost',
                                  password='',
                                  user='root')

def main():
    while True:
        resposta = menu(['ADICIONAR UM NOVO E-MAIL AO SISTEMA', 'VER QUANTOS CADASTROS EXISTEM', 'SAIR DO SISTEMA'])
        if resposta == 1:
            cabeçalho('CADASTRO DE NOVO E-MAIL')
            novo_email = input('E-mail: ').strip()
            sendToBd(novo_email, conexao)
        elif resposta == 2:
            print(f'Existem {quantId(conexao)} e-mail(s) cadastrados no sistema.')
        elif resposta == 3:
            break
        else:
            print('Por favor, digite um valor válido!')
        sleep(1)

if __name__ == '__main__':
    main()
