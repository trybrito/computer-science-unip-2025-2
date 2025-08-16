# Decompondo um número de três dígitos
number = int(input('Digite um número de três dígitos: '))

unit = number % 10
ten = number // 10 % 10
hundred = number // 100

print("Unidade:", unit)
print("Dezena:", ten)
print("Centena:", hundred)