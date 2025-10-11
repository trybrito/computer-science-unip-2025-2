agenda = {}

def ledados():
    dadosFuncao = {}

    dadosFuncao['Endereço'] = input('Digite seu endereço: ')
    dadosFuncao['Telefone'] = input('Agora, seu telefone: ')

    return dadosFuncao

def criaItem():
    chaveAdc = input('Qual chave será utilizada para o novo registro?: ')
    agenda[chaveAdc] = ledados()

def removeItem(chave):
    agenda.pop(chave, 'Não localizado!')

while True:
    opcao = int(input(
        '''
Menu:
    1 - Criar agenda
    2 - Mostrar item
    3 - Criar item
    4 - Remover item
    5 - Mostrar todos os itens
    6 - Sair 

    Escolha a ação a ser executada: '''))

    if opcao == 1:
        agenda.clear()
        # limpa a variável global agenda "criando" uma nova agenda
    elif opcao == 2:
        chave = input('\tPor qual nome deseja buscar?: ')
        print('\t', agenda.get(chave, 'Não localizado!'))
    elif opcao == 3:
        criaItem()
    elif opcao == 4:
        chave = input('\tQual registro será apagado?: ')
        removeItem(chave)
    elif opcao == 5:
        print(agenda)
    else:
        print('\nSaindo do menu...')
        break

print('\n', '*' * 20, 'FIM DO PROGRAMA', '*' * 20)
