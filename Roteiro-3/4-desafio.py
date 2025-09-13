def factorial(factNumber: int) -> int | str:
    if factNumber < 0: return 'O número precisa ser positivo!'

    res = 1
    fact = 1

    while fact <= factNumber:
        res *= fact
        fact += 1
    
    return res

def combination(n: int, k: int) -> int | str:
    if n < 0 or k < 0: return 'Ambos os números precisam ser positivos'

    combination = 0
    
    if n > k:
        combination = factorial(n) / (factorial(k) * (factorial(n - k)))
    else:
        combination = factorial(k) / (factorial(n) * (factorial(k - n)))
        
    return combination

print(combination(4, 5))