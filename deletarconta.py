import sqlite3


def deletarconta():
    import sqlite3

    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()

    conta_id = int(input("Digite o número da conta que deseja deletar: "))
    cursor.execute("DELETE FROM transacoes WHERE conta_id = ?", (conta_id,))

    bancodedados.commit()
    bancodedados.close()

    print("Conta deletada com sucesso!")
