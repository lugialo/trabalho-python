import os


def selecionar_opcao():
    while True:
        opcao = int(input(f'Qual opção você deseja gerenciar?'
                          f'\n1- Estoque'
                          f'\n2- Pessoas'
                          f'\n3- Sair do programa: '))
        os.system('cls')
        return opcao


def selecionar_contato():
    contato = input(f'Digite o número de contato.')
    return contato


lista_estoque = []
lista_clientes = []
lista_funcionarios = []

estoque = {}
clientes = {}
funcionarios = {}

print('--- Gerenciamento de Fruteira ---')

while True:
    opcao = selecionar_opcao()

    if opcao == 1:
        while True:
            print(f'--- Estoque ---'
                  f'\n1- Adicionar produto'
                  f'\n2- Atualizar disponibilidade'
                  f'\n3- Verificar disponibilidade'
                  f'\n4- Remover produto'
                  f'\n5- Voltar ao menu principal')
            fazer = int(input('Digite o número do que deseja fazer: '))
            os.system('cls')

            if fazer == 1:
                os.system('cls')
                prod = input('Digite o nome do produto. ')
                vali = input('Digite a validade do produto. ')
                dispon = int(input('Digite a quantidade do produto. '))
                estoque['prod'] = prod
                estoque['vali'] = vali
                estoque['dispon'] = dispon
                lista_estoque.append(estoque.copy())
                print(lista_estoque[1:])
            elif fazer == 2:
                os.system('cls')
                print(len(lista_estoque))
                atu = int(
                    input(f'Qual o índice de 1 a {len(lista_estoque)-1} a atualizar? '))
                dispon = int(input('Qual a nova quantidade? '))
                lista_estoque[atu]['dispon'] = dispon
                print(lista_estoque)
            elif fazer == 3:
                os.system('cls')
                ver = int(input(
                    f'Digite o índice de 0 a {len(lista_estoque)-1} do produto que deseja verificar a disponibilidade: '))
                print(lista_estoque[ver])
                print(lista_estoque)
            elif fazer == 4:
                os.system('cls')
                remover = int(
                    input(f'Digite o índice de 0 a {len(lista_estoque)-1} do produto a remover: '))
                lista_estoque.pop(remover)
                print(lista_estoque)
            elif fazer == 5:
                os.system('cls')
                break
            else:
                print('Opção inválida do submenu. Digite novamente.')

    elif opcao == 2:
        while True:
            print(f'--- Pessoas ---'
                  f'\n1 - Cadastrar cliente'
                  f'\n2 - Excluir cadastro do cliente'
                  f'\n3 - Cadastrar funcionário'
                  f'\n4 - Excluir cadastro do funcionário'
                  f'\n5 - Voltar ao menu principal')
            fazer = int(input('Digite o número do que deseja fazer: '))
            os.system('cls')

            if fazer == 1:
                os.system('cls')
                nome = input('Digite o nome do cliente: ')
                cpf = int(input('Digite o CPF do cliente: '))
                contato = int(input('Digite o número de contato: '))
                clientes['nome'] = nome
                clientes['cpf'] = cpf
                clientes['contato'] = contato
                lista_clientes.append(clientes.copy())
                print(lista_clientes)
            elif fazer == 2:
                os.system('cls')
                print(len(lista_clientes))
                if len(lista_clientes) <= 0:
                    os.system('cls')
                    print("Insira alguma informação do cliente antes!")
                    break
                else:
                    remover = int(
                        input(f'Digite o índice de 0 a {len(lista_clientes)-1} do cliente a remover: '))
                    lista_clientes.pop(remover)
                    print(lista_clientes)
            elif fazer == 3:
                os.system('cls')
                cracha = len(lista_funcionarios)
                contato = input('Digite o número de contato: ')
                funcao = input('Digite a função do funcionário: ')
            elif fazer == 4:
                os.system('cls')
                remover = int(
                    input(f'Digite o índice de 0 a {len(lista_funcionarios)-1} do funcionário a remover: '))
                lista_funcionarios.pop(remover)
                print(lista_funcionarios)
            elif fazer == 5:
                break
            else:
                print('Opção inválida. Digite novamente.')

    elif opcao == 3:
        os.system('cls')
        exit()

    else:
        os.system('cls')
        print('Opção inválida. Digite novamente.')
