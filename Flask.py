from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configurações do banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Arievelo_Zurc'
app.config['MYSQL_DB'] = 'db.alpha'

# Inicializa o MySQL
mysql = MySQL(app)

# Rota de exemplo para verificar a conexão
@app.route('/')
def hello_world():
    return 'Conexão estabelecida com sucesso!'

# Rota para buscar dados do banco de dados
@app.route('/dados')
def get_dados():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM sua_tabela")  # Substitua "sua_tabela" pelo nome da tabela do seu banco
    resultados = cursor.fetchall()
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
