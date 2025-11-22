import sqlite3


def init_db():
    connection = sqlite3.connect('bot.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS USERS ( 
        id INTEGER PRIMARY KEY  AUTOINCREMENT, 
        username TEXT(50),
        password TEXT(50)
        ) 
    ''')

    connection.commit()
    cursor.close()
    connection.close()


def save_users(username,password):
    connection = sqlite3.connect('bot.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO USERS (username, password) VALUES (?, ?)''',
                   (username,password))
    connection.commit()
    cursor.close()
    connection.close()


def get_users():
    connection = sqlite3.connect('bot.db')
    cursor = connection.cursor()
    cursor.execute('''
    SELECT username, password FROM USERS
    ''')
    users = cursor.fetchall()

    formatted = "\n".join([f"{user[0]}, {user[1]}" for user in users])
    return formatted




