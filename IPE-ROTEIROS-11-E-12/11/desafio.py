import random
from faker import Faker

fake = Faker(locale="pt-BR")

print(fake.name(), f'\n{fake.address()}', f'\n{fake.email()}')


print(f'Nota 1: {random.randint(0, 10):.2f}', 
      f'\nNota 2: {random.randint(0, 10):.2f}')
