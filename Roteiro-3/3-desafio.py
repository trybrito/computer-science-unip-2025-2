def factorial(factNumber: int) -> int | str:
    if factNumber < 0: return 'O número precisa ser positivo!'

    res = 1
    for number in range (2, factNumber + 1):
        res *= number
    
    return res

print(factorial(5))
print(factorial(4))
print(factorial(0))
print(factorial(-1))