import os
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
 def selecionar_opcao():
    while True: 
        opcao = int(input(f'Qual opção você deseja gerenciar?'
                  f'\n1- Estoque'
                  f'\n2- Pessoas'
                  f'\n3- Sair do programa: '))
        clear_screen()
        return opcao
 def adicionar_produto():
    prod = input('Digite o nome do produto. ')
    vali = input('Digite a validade do produto. ')
    dispon = int(input('Digite a quantidade do produto. '))
    return {'prod': prod, 'vali': vali, 'dispon': dispon}
 def atualizar_disponibilidade(estoque):
    atu = int(input(f'Qual o índice de 1 a {len(estoque)} a atualizar? '))
    dispon = int(input('Qual a nova quantidade? '))
    estoque[atu]['dispon'] = dispon
 def verificar_disponibilidade(estoque):
    ver = int(input(f'Digite o índice de 0 a {len(estoque)-1} do produto que deseja verificar a disponibilidade: '))
    return estoque[ver]
 def remover_produto(estoque):
    remover = int(input(f'Digite o índice de 0 a {len(estoque)-1} do produto a remover: '))
    estoque.pop(remover)
 def cadastrar_cliente():
    nome = input('Digite o nome do cliente: ')
    cpf = int(input('Digite o CPF do cliente: '))
    contato = int(input('Digite o número de contato: '))
    return {'nome': nome, 'cpf': cpf, 'contato': contato}
 def excluir_cliente(clientes):
    remover = int(input(f'Digite o índice de 0 a {len(clientes)-1} do cliente a remover: '))
    clientes.pop(remover)
 def cadastrar_funcionario():
    cracha = len(lista_funcionarios)
    contato = input('Digite o número de contato: ')
    funcao = input('Digite a função do funcionário: ')
    return {'cracha': cracha, 'contato': contato, 'funcao': funcao}
 def excluir_funcionario(funcionarios):
    remover = int(input(f'Digite o índice de 0 a {len(funcionarios)-1} do funcionário a remover: '))
    funcionarios.pop(remover)
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
            clear_screen()
             if fazer == 1:
                produto = adicionar_produto()
                estoque[len(estoque)+1] = produto
            elif fazer == 2:
                atualizar_disponibilidade(estoque)
            elif fazer == 3:
                produto = verificar_disponibilidade(estoque)
                print(produto)
            elif fazer == 4:
                remover_produto(estoque)
            elif fazer == 5:
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
            clear_screen()
             if fazer == 1:
                cliente = cadastrar_cliente()
                clientes[len(clientes)+1] = cliente
            elif fazer == 2:
                excluir_cliente(clientes)
            elif fazer == 3:
                funcionario = cadastrar_funcionario()
                funcionarios[len(funcionarios)+1] = funcionario
            elif fazer == 4:
                excluir_funcionario(funcionarios)
            elif fazer == 5:
                break
            else:
                print('Opção inválida. Digite novamente.')
     elif opcao == 3:
        exit()
    else:
        print('Opção inválida. Digite novamente.')