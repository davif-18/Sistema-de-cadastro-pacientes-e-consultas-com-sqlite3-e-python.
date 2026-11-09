import sqlite3
import calendar

def criar_tabela_de_pacientes() -> None:
    conexao = sqlite3.connect("registro_de_pacientes.db")  
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS pacientes
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        data_de_nascimento TEXT NOT NULL,
        tipo_sanguineo TEXT NOT NULL,
        doencas_identificada TEXT NO NULL)
    
    """)

    conexao.commit()
    conexao.close()

    print("Tabela criada com sucesso!")


def criar_tabela_consultas() -> None:

    conexao = sqlite3.connect("registro_de_pacientes.db")

    cursor = conexao.cursor()
    
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS registro_de_consultas
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    diagnostico TEXT NOT NULL,
    paciente_id INTEGER, 
    FOREIGN KEY (paciente_id) REFERENCES pacientes (id)

    )""")

    conexao.commit()
    conexao.close()

def buscar_paciente(cpf) -> tuple:
  
    conexao = sqlite3.connect("registro_de_pacientes.db")
    cursor = conexao.cursor()

    query2 = "SELECT * FROM pacientes WHERE cpf == ?"
    cursor.execute(query2, (cpf,))
    dados_do_paciente = cursor.fetchall()
 
    conexao.commit()
    conexao.close()

    if dados_do_paciente:
            return dados_do_paciente
    else: 
        return False


def buscar_consulta() -> tuple:
    
    paciente = buscar_paciente()
    for tuplas in paciente:
        id = tuplas[0]

    conexao = sqlite3.connect("registro_de_pacientes.db")
    cursor = conexao.cursor()

    query = "SELECT * FROM registro_de_consultas WHERE identificacao_do_paciente == ?"
    cursor.execute(query, (id,))
    consultas = cursor.fetchall()

    if consultas == None:
        return False

    conexao.commit()
    conexao.close()

    return consultas


def cadastrar_paciente() -> None:

    nome: str = input("Digite o seu nome!\n")
    cpf: str = input("Digite o seu cpf!\n")
    data_de_nascimento = input("Digite a sua data de nascimento!\n")
    tipo_sanguineo: str = input("Digite o seu tipo sanguíneo!\n")
    doencas_conhecidas: str = input("Digite a sua doença conhecida!\n")

    conexao = sqlite3.connect("registro_de_pacientes.db")  
    cursor = conexao.cursor()

    query = """  
    INSERT INTO pacientes (nome, cpf, data_de_nascimento, tipo_sanguineo, doencas_identificada) VALUES (?, ?, ?, ?, ?)
    """

    cursor.execute(query,(nome, cpf, data_de_nascimento, tipo_sanguineo, doencas_conhecidas))
    
    conexao.commit()
    conexao.close()

    print("Paciente cadastrado com sucesso!")

def cadastrar_consulta() -> str:

    cpf_busca = input("Digite o CPF do paciente!\n")
    
    conexao = sqlite3.connect("registro_de_pacientes.db")  
    cursor = conexao.cursor()

    query_0 = "SELECT id FROM pacientes WHERE cpf == ?"
    cursor.execute(query_0, (cpf_busca,))
    id_do_paciente = cursor.fetchone()

    if id_do_paciente:
        
        data: str = input("Digite a data da consulta no formato (D/M/A)\n")
        diagnostico: str = input("Escreva aqui o diagnóstico do paciente\n")

        query_1 = "INSERT INTO registro_de_consultas (data, diagnostico, paciente_id) VALUES (?, ?, ?)"

        cursor.execute(query_1, (data, diagnostico, id_do_paciente[0]))

        conexao.commit()
        conexao.close()
        return "Consulta cadastrada com sucesso!"
    
    else: 
        conexao.close()
        return "Paciente não cadastrado. Cadastre primeiro o paciente e depois registra a consulta!"
        
    




