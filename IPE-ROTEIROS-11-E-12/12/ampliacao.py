import sqlite3

db = sqlite3.connect('./12/Banco_Dados_Ampliacao.db')
cursor = db.cursor()

def create_students_table():
    sql_script_create_aluno = '''
    DROP TABLE IF EXISTS Aluno;

    CREATE TABLE Aluno (
        Codigo INTEGER PRIMARY KEY,
        Nome CHAR(15),
        Semestre INTEGER,
        Curso CHAR(10)
    )
    '''

    cursor.executescript(sql_script_create_aluno)
    db.commit()

create_students_table()

def list_all_students():
    query = cursor.execute('SELECT * FROM Aluno').fetchall()

    print()

    for line in query:
        print(line)

    print('\nSem mais registros!')

def add_new_student(student_cod, student_name, student_semester, istudent_course):
    cursor.execute('INSERT INTO Aluno VALUES (?, ?, ?, ?)', (student_cod, student_name, student_semester, istudent_course))
    db.commit()

    print(f'\nAluno(a) {name} salvo(a) com sucesso!!!')

def update_student_semester(student_code, new_semester):
    cursor.execute('UPDATE Aluno SET Semestre = ? WHERE Codigo = ?', (new_semester, student_code))
    db.commit()

    print('\nSemestre atualizado com sucesso!!!')

def delete_student(student_code):
    cursor.execute('DELETE FROM Aluno WHERE Codigo = ?', (student_code,))
    db.commit()

    print('\nEstudante deletado com sucesso!!!')

def search_student_by_name(student_name):
    query = cursor.execute("SELECT * FROM Aluno WHERE Nome LIKE '%' || ? || '%'", (student_name,)).fetchall()

    print()

    for line in query:
        print(line)

    print('\nSem mais registros!')

while True:
    print('*' * 20, 'Menú', '*' * 20)
    print('\n\t\b\b\b\b[1] Listar todos os alunos')
    print('\t\b\b\b\b[2] Adicionar um novo aluno')
    print('\t\b\b\b\b[3] Atualizar o semestre de um aluno')
    print('\t\b\b\b\b[4] Remover um aluno')
    print('\t\b\b\b\b[5] Buscar aluno por nome')
    print('\t\b\b\b\b[6] Sair')

    user_choice = int(input('\nEscolha uma opção: '))

    if user_choice == 6:
        cursor.close()
        db.close()

        print('\nSaindo do programa...')
        break

    match (user_choice):
        case 1:
            list_all_students()
            continue
        case 2:
            cod = int(input('\nInforme o código do aluno: '))
            name = input('Informe o nome do aluno: ')
            semester = int(input('Informe o semestre que o aluno está cursando: '))
            course = input('Informe o curso: ')

            add_new_student(cod, name, semester, course)
            continue
        case 3:
            cod = int(input('\nInforme o código do aluno: '))
            semester = int(input('Informe o novo semestre: '))

            update_student_semester(cod, semester)

            continue
        case 4:
            cod = int(input('\nInforme o código do aluno que será DELETADO: '))
            delete_student(cod)

            continue
        case 5:
            name = input('Qual o nome do aluno (ou parte dele)? ')
            search_student_by_name(name)

            continue
        case _:
            print('\nInforme uma opção válida!!!\n')
            continue
