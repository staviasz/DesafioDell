import sqlite3

bancodedados = sqlite3.connect("bancodell.db")
cursor = bancodedados.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS transacoes  (\
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            conta_id INTEGER,\
            tipo_transacao TEXT,\
            categoria TEXT,\
            descricao TEXT,\
            valor REAL,\
            data DATE\
            );"
)

cursor.execute(
    "CREATE TABLE IF NOT EXISTS contas (\
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            numero_conta INTEGER\
            );"
)
bancodedados.commit()
