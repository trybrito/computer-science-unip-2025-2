import sqlite3

db = sqlite3.connect('./12/Banco_Dados.db')
cursor = db.cursor()

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

cursor.executemany('INSERT INTO Aluno VALUES (?, ?, ?, ?)',
                   [(1, 'Thiago', 1, 'CC'), (2, 'Vinicius', 2, 'CC'),
                    (3, 'Gabriel', 2, 'SI'), (4, 'Vinicius', 4, 'CC'),
                    (5, 'Vitor', 3, 'ADS')])
db.commit()

consulta = cursor.execute('SELECT * FROM Aluno').fetchall()

for linha in consulta:
    print(linha)

cursor.close()
db.close()
