import sqlite3

connection_telegram_db = sqlite3.connect('not_telegram1.db')
cursor = connection_telegram_db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(ID INTEGER PRIMARY KEY,
 username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(0, 10):
    cursor.execute(" INSERT INTO  Users (username, email, age, balance) VALUES ( ?, ?, ?, ?)",
                   (f'newuser{i + 1}', f'exemple{i + 1}@gmail.com', 10 * (i + 1), 1000))

cursor.execute('UPDATE Users SET balance = "500" WHERE id % 2 != 0 ')
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')
cursor.execute('DELETE FROM Users WHERE id = 6')
connection_telegram_db.commit()

cursor.execute('SELECT COUNT(*) FROM Users')
all_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(total_balance/all_users)
connection_telegram_db.close()
