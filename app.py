from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'  # Путь к базе данных



# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Возвращает строки как словари
    return conn

# Создание таблицы в БД
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/", methods=('GET', 'POST'))

def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        email = request.form['email']
        
        # Подключаемся к базе данных и вставляем данные
        conn = get_db_connection()
        conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()

        # Перенаправляем обратно на главную страницу
        return redirect(url_for('index'))
    return render_template("index.html")

# Страница для просмотра данных
@app.route('/users')
def users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('users.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)