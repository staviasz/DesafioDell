import sqlite3

bancodedados = sqlite3.connect("bancodell.db")
import sqlite3


def cadastrarcontas():
    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_conta INTEGER
        );
    """
    )

    numero_conta = input("Digite o número da conta a ser cadastrada: ")
    cursor.execute(f"INSERT INTO contas (numero_conta) VALUES ({numero_conta});")

    bancodedados.commit()
    bancodedados.close()

    print("Dados inseridos com sucesso!")
