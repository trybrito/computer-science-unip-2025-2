name = input('Informe seu nome: ')
age = int(input('Digite sua idade: '))
favColor = input('Digite sua cor favorita: ')

print(f'Que legal, {name}! Então você tem {age} anos e adora a cor {favColor}.')
print(f'\nQue legal, {name.capitalize()}!', end=' *-* ')
print('Então você tem:')
print(f'\t-> {age} anos', f'e adora a cor "{favColor}"', sep=' - ')
