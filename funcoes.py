def a(): #Pegar Cadastro
    import os
    clear = lambda: os.system('cls')
    cliente_nome = input('Digite o nome do cliente: ')
    cliente_cpf = input('Digite o CPF  do cliente: ')
    clientes_dados = (cliente_nome, cliente_cpf)
    clear()
    print('Cliente adicionado')
    return clientes_dados


def b(): #MENU
    import os
    clear = lambda: os.system('cls')
    option = int(input('''
[1] - Cadastrar Cliente
[2] - Cadastratar Maquina
[3] - Alugar Maquinas
[4] - Relatório de Clientes
[5] - Relatório de Maquinas
[6] - Relatorio de Alugueis
[7] - Sair
'''))
    clear()
    return option


def c(): #Registar Maquinas
    import os
    clear = lambda: os.system('cls')
    import random
    print('Vamos Iniciar o cadastro de uma nova maquina')
    cod_ident = random.randint(1, 100)
    print(f'O codigo da maquina é {cod_ident}')

    tipo_maq = input('''Qual o maquinario que vai ser usado?
    [1] - Demolidor
    [2] - Perfurador
    [3] - Compactador
    ''')

    if tipo_maq == '1':
        maqui = 'Demolidora'
    if tipo_maq == '2':
        maqui = 'Perfuradora'
    if tipo_maq == '3':
        maqui = 'Compactadora'

    marca = input(f'Qual a marca da {maqui}? ')
    modelo = input(f'Qual o modelo da {maqui}? ')
    ano = input(f'Qual o ano da {maqui}? ')
    valor = int(input(f'Qual o valor da {maqui}"? '))
    status = 1

    maquina = [maqui, marca, modelo, ano, valor, cod_ident, status]
    clear()
    print(maquina)
    print('Maquina cadastrada')
    return maquina


def d(clientes, maquinario): #Reserva de Maquinas
    
    import os
    clear = lambda: os.system('cls')

    clear()
    maq_temp = []
    pessoa_temp = []

    avaliar = 0



    cpf = input('Digite aqui o CPF do cliente: ')
    for i in range(len(clientes)):
        if cpf == clientes[i][1]:
            print(f'Olá {clientes[i][0]} ')
            pessoa_temp.append(clientes[i][0])
            avaliar += 1
            break
    if avaliar == 0:
        print('CPF não encontrado')


    avaliar2 = 0

    codmaquina = int(input('Digite o codigo da maquina: '))

    for i in range(len(maquinario)):
        if codmaquina == maquinario[i][5]:

            if maquinario[i][6] == 1:
                print('Maquina Reservada para você')
                maquinario[i][6] = 0
                maq_temp.append(maquinario[i][5])
                maq_temp.append(maquinario[i][0])
                maq_temp.append (maquinario[i][4])
                avaliar2 += 1
                # Código identificador da máquina, tipo da máquina, valor do aluguel;

            if maquinario[i][6] == 0:
                print('Maquina indisponivel')



    if avaliar2 == 0:
         print('Codigo não encontrado')

    if avaliar2 == 1:
        maquina = [pessoa_temp, maq_temp]
        clear()
        print(maquina)
        print('Cadastro Feito')
        return maquina

def e(clientes, maquinario, alugados): # Escrever aquivo

    with open('Registros.txt', 'w') as arquivo:
        arquivo.write(f' || Empresa Maquinário Construção  || \n')
        arquivo.write(f'############################################################\n')
        arquivo.write(f'\n')
        arquivo.write(f'\n')
        arquivo.write(f'{"Clientes cadastrados:".ljust(10," ")}\n')
        arquivo.write(f'\n')
        for i in range(len(clientes)):
            arquivo.write(f'''Nome: {clientes[i][0]}\n  
        CPF: {clientes[i][1]}\n
        ------\n
        '''.ljust(10, " "))

        arquivo.write(f'\n')

        arquivo.write(f'{"Maquinário cadastrados:".ljust(10," ")}\n')
        arquivo.write(f'\n')
        for i in range(len(maquinario)):
            arquivo.write(f'''  Maquinario: {maquinario[i][0]}\n
            Marca: {maquinario[i][1]}\n
            Modelo: {maquinario[i][2]}\n
            Ano: {maquinario[i][3]}\n
            Valor: {maquinario[i][4]}\n
            Cód. Ident: {maquinario[i][5]}\n
            Status: {maquinario[i][6]}\n
                Se status for '1', então a máquina está disponível\n
                -------\n
        '''.ljust(10," "))

        arquivo.write(f'{"Relatório de Alugueis:".ljust(10, " ")}\n')

        arquivo.write(f'\n')

        for i in range(len(alugados)):
            arquivo.write(f'''  Nome do cliente: {alugados[i][0][0]}\n
            Cod. da maquina: {alugados[i][1][0]}\n
            Tipo da maquina: {alugados[i][1][1]}\n
            Valor da maquina: {alugados[i][1][2]}\n
            -------\n
        '''.ljust(10, " "))
