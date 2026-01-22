from dotenv import load_dotenv
import os

import psycopg2

# Load environment variables
load_dotenv()

dbname = os.getenv("DATABASE_NAME")
user = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")


try:
    # Connect to your postgres DB
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    print(f"Connected to database {dbname} successfully.")
except Exception as e:
    print(f"An error occurred while connecting to the database {dbname}: {e}")

# Verificar se a tabela 'clientes' existe
try:
    cursor = conn.cursor()
    
    # Se a tabela não existe, executar o script de criação
    create_table_query = '''CREATE TABLE IF NOT EXISTS clientes (
                            cod_cliente VARCHAR(100),
                            sexo VARCHAR(100),
                            estado_civil VARCHAR(100),
                            dependentes VARCHAR(100),
                            educacao VARCHAR(100),
                            empregado VARCHAR(100),
                            renda INTEGER,
                            renda_conjuge VARCHAR(100),
                            emprestimo FLOAT,
                            prestacao_mensal FLOAT,
                            historico_credito FLOAT,
                            imovel VARCHAR(100),
                            aprovacao_emprestimo VARCHAR(100)
                            );'''
    cursor.execute(create_table_query)
    conn.commit()
    print("Tabela 'clientes' criada com sucesso!")
    
except psycopg2.Error as e:
    conn.rollback()  # Desfaz a transação em caso de erro
    print("Erro ao verificar/criar tabela:", e)