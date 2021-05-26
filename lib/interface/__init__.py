def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número inteiro válido.')
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar esse número.')
        else:
            return n


def linha(tam = 50):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
