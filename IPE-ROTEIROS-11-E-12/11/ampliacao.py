from random import randint
from math import sqrt
from faker import Faker

def get_fake_data() -> dict[str, str | list[str] | (int) | int]:
    full_name = fake.name()
    address = fake.address()
    email = fake.email()

    st_grade = randint(0, 10)
    nd_grade = randint(0, 10)

    geometric_mean = 0

    if (st_grade > 0 and nd_grade > 0):
        geometric_mean = sqrt(st_grade * nd_grade)

    inner_fake_dict = {
        'full_name': full_name,
        'address': address.split('\n'),
        'email': email,
        'grades': (st_grade, nd_grade),
        'geometric_mean': geometric_mean,
    }

    return inner_fake_dict


fake = Faker(locale='pt-BR')

fictional_agenda = []

for i in range(0, 10):
    fake_dict = get_fake_data()

    fictional_agenda.append(fake_dict)
    print(f'Registro de {fake_dict.get('full_name')} criado com sucesso!')

    for index, value in enumerate(fictional_agenda):
        print(f'Registro {index + 1}:')
        print(f'\t\b\bNome: {value.get('full_name')}')
        print(f'\t\b\bEndereço: {' - '.join(value.get('address'))}')
        print(f'\t\b\bEmail: {value.get('email')}')
        print(f'\t\b\bNotas: {' e '.join(str(grade) for grade in value.get('grades'))}')
        print(f'\t\b\bMédia geométrica: {value.get('geometric_mean')}\n')
