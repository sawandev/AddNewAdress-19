from lib.interface import *
from lib.toConect import *
from time import sleep

def main():
    while True:
        resposta = menu(['ADICIONAR UM NOVO E-MAIL AO SISTEMA', 'VER QUANTOS CADASTROS EXISTEM', 'SAIR DO SISTEMA'])
        if resposta == 1:
            cabeçalho('CADASTRO DE NOVO E-MAIL')
            novo_email = input('E-mail: ').strip()
            sendToBd(novo_email)
        elif resposta == 2:
            print(f'Existem {quantId()} e-mail(s) cadastrados no sistema.')
        elif resposta == 3:
            break
        else:
            print('Por favor, digite um valor válido!')
        sleep(1)

if __name__ == '__main__':
    main()
