# Faça um programa que receba um número natural maior que zero e verifique se ele é um
# número primo. Um número primo é divisível apenas por 1 e por ele mesmo.
#  Por definição, o número 1 não é primo.
#  Os primeiros números primos são: 2, 3, 5, 7, 11, 13, 17, 19, 23...
#  Dica: Você pode usar um laço for para testar divisões do número por todos os inteiros
# de 2 até o número - 1. Se encontrar algum divisor, o número não é primo.

numberChosen = int(input('Informe um número natural maior que zero: '))

if numberChosen <= 0:
    print('O número escolhido precisa ser maior que zero!')
elif numberChosen == 1:
    print('Por definição, o número 1 não é primo')
else:
    isPrimeNumber = numberChosen % numberChosen == 0

    for number in range(2, numberChosen):
        if numberChosen % number == 0:
            isPrimeNumber = False
            break

    print(isPrimeNumber)
