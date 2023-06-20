import sys
import os

def get_elemento(lista, indice):
    return lista[indice - 1]

def selecionar_opcao():
    while True: 
        opcao = int(input(f'Qual opção você deseja gerenciar?'
                  f'\n1- Estoque'
                  f'\n2- Pessoas'
                  f'\n3- Sair do programa: '))
        return opcao

def selecionar_contato():
    contato = input(f'Digite o número de contato.')
    return contato

lista = []
lista2 = []
estoque = {}
pessoas = {}

print('--- Gerenciamento de Fruteira ---')

while True:
    opcao = selecionar_opcao()

    if opcao == 1:
        while True:
            print(f'\n1- Adicionar produto'
                  f'\n2- Atualizar disponibilidade'
                  f'\n3- Verificar disponibilidade'
                  f'\n4- Remover produto'
                  f'\n5- Voltar ao menu principal')
            fazer = int(input('Digite o número do que deseja fazer: '))
            
            if fazer == 1:
                prod = input('Digite o nome do produto. ')
                vali = input('Digite a validade do produto. ')
                dispon = int(input('Digite a quantidade do produto. '))
                estoque['prod'] = prod
                estoque['vali'] = vali
                estoque['dispon'] = dispon
                lista.append(estoque.copy())
                print(lista)
            elif fazer == 2:
                atu = int(input(f'Qual o índice de 0 a {len(lista)-1} a atualizar? '))
                dispon = int(input('Qual a nova quantidade? '))
                lista[atu]['dispon'] = dispon
                print(lista)
            elif fazer == 3:
                ver = int(input(f'Digite o índice de 0 a {len(lista)-1} do produto que deseja verificar a disponibilidade: '))
                print(lista[ver])
                print(lista)
            elif fazer == 4:
                remover = int(input(f'Digite o índice de 0 a {len(lista)-1} do produto a remover: '))
                lista.pop(remover)
                print(lista)
            elif fazer == 5:
                break
            else:
                print('Opção inválida do submenu. Digite novamente.')

    elif opcao == 2:
        while True:
            print(f'\n1 - Cadastrar cliente'
                  f'\n2 - Excluir cadastro do cliente'
                  f'\n3 - Cadastrar funcionário'
                  f'\n4 - Excluir cadastro do funcionário'
                  f'\n5 - Voltar ao menu principal')
            fazer = int(input('Digite o número do que deseja fazer: '))

            if fazer == 1:
                os.system('cls')
                nome = input('Digite o nome do cliente: ')
                cpf = int(input('Digite o CPF do cliente: '))
                contato = int(input('Digite o número de contato: '))
                pessoas['nome'] = nome
                pessoas['cpf'] = cpf
                pessoas['contato'] = contato
                lista2.append(pessoas.copy())
                print(lista2)
            elif fazer == 2:
                os.system('cls')
                print(len(lista2))
                if len(lista2) >= 0:
                    print("Insira alguma informação do cliente antes!")
                    break
                else:   
                    remover = int(input(f'Digite o índice de 0 a {len(lista2)} do cliente a remover: '))
                    lista2.pop(remover)
                    print(lista2)
            elif fazer == 3:
                os.system('cls')
                cracha = input('Digite o número do crachá: ')
                contato = input('Digite o número de contato: ')
                funcao = input('Digite a função do funcionário: ')
            elif fazer == 4:
                remover = int(input(f'Digite o índice de 0 a {len(lista2)} do funcionário a remover: '))
                lista2.pop(remover)
                print(lista2)
            elif fazer == 5:
                break
            else:
                print('Opção inválida. Digite novamente.')

    elif opcao == 3:
        exit()
            
    else:
        print('Opção inválida. Digite novamente.')