import psycopg2

def conectardb():
    conexao = psycopg2.connect(database="minicursobd",
                               host="localhost",
                               user="postgres",
                               password="JwBn2020@",
                               port="5432")
    return conexao


conexao = conectardb()


def inserir_usuario(email, nome, senha):
    conexao = conectardb()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (%s, %s,  %s)", (nome, email, senha))

    conexao.commit()
    cursor.close()
    conexao.close()


def buscar_usuario(nome):
    conexao = conectardb()
    cursor = conexao.cursor()
    cursor.execute(f"SELECT email,nome FROM usuario where nome= '{nome}' ")

    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_usuarios():
    conexao = conectardb()
    cursor = conexao.cursor()
    cursor.execute(f"SELECT email,nome FROM usuario")

    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def atualizar_usuario(id, novo_nome, novo_email):
    conexao = conectardb()
    cursor = conexao.cursor()
    cursor.execute("UPDATE usuario SET nome = %s, email = %s WHERE id = %s", (novo_nome, novo_email, id))

    conexao.commit()
    cursor.close()
    conexao.close()


def deletar_usuario(id):
    conexao = conectardb()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))

    conexao.commit()
    cursor.close()
    conexao.close()

