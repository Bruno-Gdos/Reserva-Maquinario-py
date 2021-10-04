
# Imports de funções que irei usar
import os

clear = lambda: os.system('cls')
import random
from funcao import a, b, c, d, e
clear()
# Listas que irei usar
maquiario = []
cadastrados = []
Alugados = []

with open('Cadastro.txt', 'w') as arquivo:

    while True:

        # Escrever arquivo
        e(cadastrados, maquiario, Alugados)
        
        # Menu
        opcao = b()

        # Bifurcações do Menu
        if opcao == 1: # Cadastrando o cliente
            
            cliente = a()
            cadastrados.append(cliente)

        if opcao == 2: # Cadastrando Maquina
            
            maquina = c()
            maquiario.append(maquina)

        if opcao == 3: #Reservando Maquina

            aluguel = d(cadastrados, maquiario)
            Alugados.append(aluguel)


        if opcao == 4: # Relatório de Clientes
            
            print('Os clientes cadastrados são: ')
            for i in range(len(cadastrados)):
                print(f'''Nome: {cadastrados[i][0]}  
        CPF: {cadastrados[i][1]}
        ------
        ''')

        if opcao == 5: #Relatório do Maquinário

            for i in range(len(maquiario)):
                print(f'''  Maquinario: {maquiario[i][0]}
            Marca: {maquiario[i][1]}
            Modelo: {maquiario[i][2]}
            Ano: {maquiario[i][3]}
            Valor: {maquiario[i][4]}
            Cód. Ident: {maquiario[i][5]}
            Status: {maquiario[i][6]}
                Se status for '1', então a máquina está disponível
                -------
        ''')

        if opcao == 6: #Relatório de Alugueis
            print('Relatório de Alugueis:')

            for i in range(len(Alugados)):
                print(f'''  Nome do cliente: {Alugados[i][0][0]}
            Cod. da maquina: {Alugados[i][1][0]}
            Tipo da maquina: {Alugados[i][1][1]}
            Valor da maquina: {Alugados[i][1][2]}
            -------
        ''')

        if opcao == 7:
            break

