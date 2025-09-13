numberChosen = int(input('Informe um número: '))
sum = 0

for n in range(numberChosen + 1):
   sum += n

print(f'A soma de todos os números até o número escolhido (inclusive) é {sum}')