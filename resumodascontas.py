import sqlite3


def resumo_das_contas():
    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()

    # Recupera todas as contas do banco de dados
    cursor.execute("SELECT conta_id, numero_conta FROM contas")
    contas = cursor.fetchall()

    saldo_total = 0

    print("Resumo das Contas:")
    for conta in contas:
        conta_id = conta[0]
        conta_nome = conta[1]

        # Calcula o saldo da conta
        cursor.execute(
            "SELECT SUM(valor) FROM transacoes WHERE conta_id = ?", (conta_id,)
        )
        saldo = cursor.fetchone()[0]
        if saldo is None:
            saldo = 0

        print(f"Conta: {conta_nome} - Saldo: R${saldo:.2f}")
        saldo_total += saldo

    print(f"Saldo Total: R${saldo_total:.2f}")

    bancodedados.close()
