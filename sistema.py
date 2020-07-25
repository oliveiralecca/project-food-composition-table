from MacroNutrientesSys.library.interface import *
from MacroNutrientesSys.library.arquivo import *
from datetime import date
from time import sleep

arqv = 'database.txt'

cabecalho_principal('TABELA DE MACRONUTRIENTES')
sleep(0.3)

while True:
    resposta = menu(['Consultar alimento', 'Cadastrar novo alimento', 'Sair do programa'])
    if resposta == 1:
        # Consulta a elemento do database!
        print('\033[34mBUSCA POR ALIMENTO\033[m'.center(140))
        print('\033[31mAVISO: Faça sua busca sem acentos e caracteres especiais!\033[m'.center(140))
        print()
        alimento = str(input('Alimento >> ')).strip().upper()
        consulta_negative(arqv, alimento)
        sleep(0.5)
    elif resposta == 2:
        # Opção de cadastrar um novo alimento!
        print('\033[34mCADASTRO DE NOVO ALIMENTO\033[m'.center(140))
        print('\033[31mAVISO: Faça o cadastro sem acentos e caracteres especiais!\033[m'.center(140))
        print()
        alimento = str(input('Alimento: ')).strip().upper()
        carbo = float(input('Carboidrato (g): '))
        ptn = float(input('Proteína (g): '))
        lipd = float(input('Lipídio (g): '))
        cadastrar(arqv, alimento, carbo, ptn, lipd)
        sleep(0.5)
    elif resposta == 3:
        print('\033[34mSAINDO DO SISTEMA... ATÉ LOGO!\033[m'.center(140))
        sleep(1)
        break

data_atual = date.today().year
rodape('Tabela de Composição de Alimentos', f'Atualizado em {data_atual}')
