import os  # Biblioteca utilizada para utilizar o metódo de limpar a tela
import re  # Biblioteca utilizada para as verificações de número de contato e CPF


def selecionar_opcao():  # Nessa função, estão as opções do menu principal
    while True:
        opcao = int(input('Qual opção você deseja gerenciar?'
                          '\n1- Estoque'
                          '\n2- Pessoas'
                          '\n3- Sair do programa: '))
        os.system('cls')
        return opcao


def selecionar_contato():  # Essa função faz parte da verificação de contato
    contato = input(f'Digite o número de contato.')
    return contato


def selecionar_cpf():  # Essa função faz parte da verificação de CPF
    cpf = input('Digite o CPF: ')
    return cpf


# Listas para organizar os dados
lista_estoque = []
lista_clientes = []
lista_funcionarios = []

# Dicionários para organizar os dados dentro das listas
estoque = {}
clientes = {}
funcionarios = {}

print('--- Gerenciamento de Fruteira ---')

while True:  # No começo do loop, ele sempre vai executar a função de selecionar as opções
    opcao = selecionar_opcao()

    if opcao == 1:
        while True:  # Submenu de Estoque
            print('--- Estoque ---'
                  '\n1- Adicionar produto'
                  '\n2- Atualizar disponibilidade'
                  '\n3- Verificar disponibilidade'
                  '\n4- Remover produto'
                  '\n5- Voltar ao menu principal')
            fazer = int(input('Digite o número do que deseja fazer: '))
            # cls é o nome do método utilizado para limpar a tela
            os.system('cls')

            if fazer == 1:
                os.system('cls')
                prod = input('Digite o nome do produto. ')
                vali = int(input('Digite a validade do produto. '))
                dispon = int(input('Digite a quantidade do produto. '))
                estoque['Produto'] = prod
                estoque['Validade'] = vali
                estoque['Disponibilidade'] = dispon
                lista_estoque.append(estoque.copy())
            elif fazer == 2:
                os.system('cls')
                print('Produtos registrados até o momento:')
                # Esse for é utilizado para mostrar os produtos cadastrados
                for i in range(len(lista_estoque)):
                    print(f'Número: {i}, {lista_estoque[i]}')
                atu = int(
                    input(f'Qual o índice de 0 a {len(lista_estoque)-1} a atualizar? '))  # Utilizamos -1 para mostrar o índice corretamente
                dispon = int(input('Qual a nova quantidade? '))
                # O sistema atualiza a disponibilidade do item da lista conforme o input do usuário
                lista_estoque[atu]['Disponibilidade'] = dispon
                print(lista_estoque[atu])
            elif fazer == 3:
                os.system('cls')
                ver = int(input(
                    f'Digite o índice de 0 a {len(lista_estoque)-1} do produto que deseja verificar a disponibilidade: '))
                # O print mostra o produto do índice que o usuário digitou.
                print(lista_estoque[ver])
            elif fazer == 4:
                os.system('cls')
                print('Produtos registrados até o momento:')
                if len(lista_estoque) <= 0:
                    os.system('cls')
                    print("Insira algum produto no estoque antes!")
                    print("-----------------------------------------------")
                    break
                else:
                    for i in range(len(lista_estoque)):
                        # Esse for é utilizado para mostrar os produtos cadastrados
                        print(f'Número: {i}, {lista_estoque[i]}')
                    remover = int(
                        input(f'Digite o índice de 0 a {len(lista_estoque)-1} do produto a remover: '))
                    lista_estoque.pop(remover)
            elif fazer == 5:
                os.system('cls')
                break
            else:
                print('Opção inválida. Digite novamente.')

    elif opcao == 2:
        while True:
            print('--- Pessoas ---'
                  '\n1 - Cadastrar cliente'
                  '\n2 - Excluir cadastro do cliente'
                  '\n3 - Cadastrar funcionário'
                  '\n4 - Excluir cadastro do funcionário'
                  '\n5 - Voltar ao menu principal')
            fazer = int(input('Digite o número da ação desejada: '))
            os.system('cls')

            if fazer == 1:
                os.system('cls')
                nome = input('Digite o nome: ')
                cpf = (input('Digite o CPF: '))
                # Essa função (re.match) verifica a validade do input do CPF e do contato.
                if not re.match(r'^\d{11}$', cpf):
                    # Só são permitidos digitos númericos e o total de digitos do input deve ser igual a 11.
                    print('CPF inválido!')
                    cpf = selecionar_cpf()
                contato = (input('Digite o número de contato: '))
                if not re.match(r'^\d{11}$', contato):
                    print(
                        'Número de contato inválido! Deve conter no mínimo 11 dígitos.')
                    contato = selecionar_contato()
                clientes['Nome'] = nome
                clientes['CPF'] = cpf
                clientes['Contato'] = contato
                lista_clientes.append(clientes.copy())
            elif fazer == 2:
                os.system('cls')
                print(len(lista_clientes))
                if len(lista_clientes) <= 0:
                    os.system('cls')
                    print("Insira alguma informação de cliente antes!")
                    print("-----------------------------------------------")
                    break
                else:
                    print('Clientes registrados até o momento:')
                    for i in range(len(lista_clientes)):
                        print(f'Número: {i}, {lista_clientes[i]}')
                    remover = int(
                        input(f'Digite o índice de 0 a {len(lista_clientes)-1} do cliente a remover: '))
                    lista_clientes.pop(remover)
            elif fazer == 3:
                os.system('cls')
                nome = input('Digite o nome do funcionário: ')
                contato = input('Digite o número de contato: ')
                if not re.match(r'^\d{11}$', contato):
                    contato = selecionar_contato()
                funcao = input('Digite a função do funcionário: ')
                funcionarios['Nome'] = nome
                funcionarios['Contato'] = contato
                funcionarios['Função'] = funcao
                lista_funcionarios.append(funcionarios.copy())
            elif fazer == 4:
                os.system('cls')
                if len(lista_funcionarios) <= 0:
                    os.system('cls')
                    print("Insira alguma informação de funcionário antes!")
                    print("-----------------------------------------------")
                    break
                else:
                    print('Funcionários registrados até o momento:')
                    for i in range(len(lista_funcionarios)):
                        print(f'Número: {i}, {lista_funcionarios[i]}')
                    remover = int(
                        input(f'Digite o índice de 0 a {len(lista_funcionarios)-1} do funcionário a remover: '))
                    lista_funcionarios.pop(remover)
            elif fazer == 5:  # Caso o usuário digite uma opção que não esteja no submenu, o sistema pedirá para que ele insira novamente.
                break
            else:
                print('Opção inválida. Digite novamente.')

    elif opcao == 3:  # Opção para sair do sistema
        os.system('cls')
        exit()

    else:  # Caso o usuário digite uma opção que não esteja no menu, o sistema pedirá para que ele insira novamente.
        os.system('cls')
        print('Opção inválida. Digite novamente.')
