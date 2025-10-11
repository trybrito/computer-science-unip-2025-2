def menu() -> int:
    print ('*' * 10, 'Menu', '*' * 10)
    print('\n1 - Criar um arquivo')
    print('2 - Ler um arquivo')
    print('3 - Inserir conteúdo em um arquivo')
    print('4 - Sair')

    return int(input('Escolha uma das opções: '))

def criaArquivo(arquivo: str) -> None:
    file = open(f'10/{arquivo}', 'w', encoding='utf-8')
    file.close()

def leArquivo(arquivo: str) -> str:
    file = open(f'10/{arquivo}', 'r', encoding='utf-8')

    for linha in file.readlines():
        print(linha.rstrip())

    file.close()

def inserirConteudoArquivo(arquivo: str, dado: str) -> None:
    file = open(f'10/{arquivo}', 'a', encoding='utf-8')
    file.write(f'{dado}\n')
    file.close()


while True:
    opcao = menu()

    match opcao:
        case 1:
            nomeArquivo = input('Qual o nome do arquivo que você quer criar?: ')
            criaArquivo(f'{nomeArquivo}.txt')
        case 2:
            nomeArquivo = input('Qual o nome do arquivo que você quer ler?: ')
            leArquivo(f'{nomeArquivo}.txt')
        case 3:
            nomeArquivo = input('Qual o nome do arquivo em que você quer adicionar informações?: ')
            conteudo = input('O quê você quer adicionar? [coloque o texto aqui]: ')

            inserirConteudoArquivo(f'{nomeArquivo}.txt', conteudo)
        case _:
            break
