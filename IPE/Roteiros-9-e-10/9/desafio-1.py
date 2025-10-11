# step 1
dados = {}

dados['Endereço'] = 'Rua X, Nº Y'
dados['Telefone'] = '19999999999'

print(dados)

# step 2

dados.clear()

dados['Endereço'] = input('Digite seu endereço: ')
dados['Telefone'] = input('Agora, seu telefone: ')

print(dados)

# step 3

def ledados():
    dadosFuncao = {}

    dadosFuncao['Endereço'] = input('Digite seu endereço: ')
    dadosFuncao['Telefone'] = input('Agora, seu telefone: ')

    return dadosFuncao

print(ledados())

# step 4
agenda = {
    'Paulo': ledados()
}

print(agenda)

# step 5
print(agenda['Paulo'])

#step 6
def mostraItem(chave):
    print('Chave informada: ', chave)
    print('Informações da chave: ', agenda.get(chave, 'Não Localizado'))

mostraItem('Paulo')
mostraItem('Maria')
