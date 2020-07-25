def consulta_negative(arq, txt):
    try:
        a = open(arq, 'rt')
    except:
        print('\033[31mERRO ao ler o arquivo!\033[m')
    else:
        if txt not in a.read():
            print('\033[31mO alimento não consta na Base de Dados!\033[m')
            print('-' * 132)
        else:
            a.close()
            consulta(arq, txt)


def consulta(arq, txt):
    try:
        a = open(arq, 'rt')
    except:
        print('\033[31mERRO ao ler o arquivo!\033[m')
    else:
        for linha in a:
            if txt in linha:
                print('\033[34m-' * 83)
                print('ALIMENTO', end='                                         ')
                print('CARB (g)', end='    ')
                print('PROT (g)', end='    ')
                print('LIP (g)\033[m')
                dado = linha.split(';')
                dado[3] = dado[3].replace('\n', '')
                print(f'\033[30m{dado[0]:<49}{dado[1]:<12}{dado[2]:<12}{dado[3]:<6}\033[m')
    finally:
        print()
        print()
        print('                                                 ABREVIATURAS: nd - Não disponível')
        print('                                                               tr - Traço')
        a.close()
        print('-' * 132)


def cadastrar(arq, alim, carb, prot, lip):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{alim};{carb};{prot};{lip}\n')
        except:
            print('\033[31mHouve um ERRO ao escrever os dados!\033[m')
        else:
            print(f'\nNovo registro de \033[34m{alim}\033[m adicionado.')
            a.close()
        print('-' * 132)
