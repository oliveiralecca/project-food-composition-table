def fonte(txt):
    traco = '-' * (len(txt)-8)
    print(f'{traco:>132}')
    print(f'{txt:>140}')


def cabecalho_principal(txt):
    print('-=' * 66)
    print('\033[1:34:40m')
    print(txt.center(132))
    print('\n\033[m', end='')
    fonte('\033[30mFonte: Sônia Tucunduva\033[m')
    fonte('\033[34mDesenvolvido por: Letícia Oliveira\033[m')
    print('-' * 132)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
            continue   # VOLTA PARA O WHILE
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[35m{item}\033[m')
        c += 1
    print()
    opc = leiaInt('\033[32mSua Opção: \033[m')
    while opc > 3:
        print('\033[31mERRO: Digite uma opção válida.\033[m')
        opc = leiaInt('\033[32mSua Opção: \033[m')
    print('-' * 132)
    return opc


def rodape(txt1, txt2):
    print('-' * 132)
    print(txt1.center(132))
    print(txt2.center(132))
    print('-=' * 66)
