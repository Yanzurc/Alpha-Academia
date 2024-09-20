import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Conexão bem-sucedida!")
    except Error as e:
        print(f"Erro '{e}' ocorreu.")

    return connection


host = "localhost"  
user = "root"
password = "Arievelo_Zurc"
database = "db.alpha"

conn = create_connection(host, user, password, database)

