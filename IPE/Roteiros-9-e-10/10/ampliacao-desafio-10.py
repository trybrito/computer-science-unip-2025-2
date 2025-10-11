def menu() -> int:
    print ('*' * 10, 'Menu', '*' * 10)
    print('\n1 - Criar um arquivo')
    print('2 - Ler um arquivo')
    print('3 - Inserir conteúdo em um arquivo')
    print('4 - Criptografar arquivo')
    print('5 - Descriptografar arquivo')
    print('6 - Sair')

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

def criptografaArquivo(arquivo, arquivoCripto, chave: int) -> None:
    file = open(f'10/{arquivo}', 'r', encoding='utf-8')
    texto = ''

    for linha in file.readlines():
        texto += linha

    texto_criptografado = ''
    start = 0

    for char in texto:
        if 'a' <= char <= 'z':
            start = ord('a')
        elif 'A' <= char <= 'Z':
            start = ord('A')
        else:
            texto_criptografado += char # Não criptografa caracteres que não são letras
            continue

        # Calcula a nova posição do caractere no alfabeto.
        # O operador ‘%’ (módulo) garante que, se a chave mover o caractere
        # além do ‘Z’ ou ‘z’, ele “volte” para o início do alfabeto (‘A’ ou ‘a’).

        nova_posicao = (ord(char) - start + chave) % 26 + start
        texto_criptografado += chr(nova_posicao)
    
    newFile = open(f'10/{arquivoCripto}', 'w', encoding='utf-8')
    newFile.write(texto_criptografado)
    newFile.close()

def descriptografaArquivo(arquivo, chave: int) -> str:
    file = open(f'10/{arquivo}', 'r', encoding='utf-8')
    texto = ''

    for linha in file.readlines():
        texto += linha.rstrip()

    texto_descriptografado = ''
    start = 0

    for char in texto:
        if 'a' <= char <= 'z':
            start = ord('a')
        elif 'A' <= char <= 'Z':
            start = ord('A')
        else:
            texto_descriptografado += char # Caracteres não-alfabéticos permanecem inalterados
            continue
        # Calcula a posição original do caractere no alfabeto.
        # Adicionamos 26 antes de aplicar o módulo para garantir que o resultado seja positivo,
        # mesmo se (ord(char) - start - chave) for negativo.

        nova_posicao = (ord(char) - start - chave + 26) % 26 + start
        texto_descriptografado += chr(nova_posicao)
    
    return texto_descriptografado

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
        case 4:
            nomeArquivo = input('Qual arquivo você quer criptografar?: ')
            nomeArquivoCripto = input('Qual será o nome do arquivo criptografado?: ')
            chave = int(input('Defina a chave para a criptografia: '))

            criptografaArquivo(f'{nomeArquivo}.txt', f'{nomeArquivoCripto}.txt', chave)
        case 5:
            nomeArquivo = input('Qual arquivo você quer descriptografar?: ')
            chave = int(input('Informe a chave para a descriptografia: '))

            print(descriptografaArquivo(f'{nomeArquivo}.txt', chave))
        case _:
            break
