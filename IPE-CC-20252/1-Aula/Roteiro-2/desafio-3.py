decimalBaseNumber = int(input('Informe um número entre 0 e 15: '))

restOfDecimalBaseNumber = decimalBaseNumber
decimalBaseNumberIntDiv = decimalBaseNumber
binaryBaseNumber = ''

while decimalBaseNumberIntDiv > 0:
    restOfDecimalBaseNumber = decimalBaseNumberIntDiv % 2
    decimalBaseNumberIntDiv = decimalBaseNumberIntDiv // 2

    binaryBaseNumber = str(restOfDecimalBaseNumber) + binaryBaseNumber

print(binaryBaseNumber)
