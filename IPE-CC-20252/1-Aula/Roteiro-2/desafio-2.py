# Cálculo de IMC
height = float(input('Digite sua altura: '))
weight = float(input('Ótimo, agora seu peso: '))

imc = weight / (height * height) # ou height * 2, mas assim é mais semântico.

print(f'Seu IMC é: {imc:.2f}')
