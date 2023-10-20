import sqlite3


conn = sqlite3.connect("bdd_imc_calculator.db")
cur = conn.cursor()

# créer la table USER
create_table_user = '''
CREATE TABLE IF NOT EXISTS user (
user_id INTEGER PRIMARY KEY,
username TEXT,
first_name TEXT,
last_name TEXT,
email TEXT,
address TEXT,
telephone INT
)
'''

# Créer la table bmi
create_table_bmi = '''
CREATE TABLE IF NOT EXISTS bmi (
bmi_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
poids INTEGER,
taille FLOAT,
imc FLOAT,
FOREIGN KEY (user_id) REFERENCES user(user_id)
)

'''

# Créer la table history
create_table_history = '''
CREATE TABLE IF NOT EXISTS history (
history_id INTEGER PRIMARY KEY,
user_id INTEGER,
previous_bmi FLOAT,
current_bmi FLOAT,
FOREIGN KEY (user_id) REFERENCES user(user_id)
)

'''

# Execute les instructions SQL en utilisant ce curseur
cur.execute(create_table_user)
cur.execute(create_table_bmi)
cur.execute(create_table_history)

conn.commit()
conn.close()


    