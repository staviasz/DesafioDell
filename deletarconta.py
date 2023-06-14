import sqlite3


def deletarconta():

    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()

    conta_id = int(input("Digite o número da conta que deseja deletar: "))
    cursor.execute(f"DELETE FROM contas WHERE numero_conta = {conta_id}")

    bancodedados.commit()
    bancodedados.close()

    print("Conta deletada com sucesso!")
