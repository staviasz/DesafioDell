import sqlite3


def transferir_fundos():
    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()

    conta_origem = int(input(" Digite a conta de origem :"))
    conta_destino = int(input("Digite a conta destino :"))
    saldo_origem = int(input("Digite o valor da transferência: "))
    valor = int

    # Verificar se as contas existem
    cursor.execute(
        "SELECT COUNT(*) FROM transacoes WHERE conta_id = ?", (conta_origem,)
    )
    conta_origem_existente = cursor.fetchone()[0]
    cursor.execute(
        "SELECT COUNT(*) FROM transacoes WHERE conta_id = ?", (conta_destino,)
    )
    conta_destino_existente = cursor.fetchone()[0]

    if conta_origem_existente == 0:
        print("A conta de origem não existe.")
        bancodedados.close()
        return
    elif conta_destino_existente == 0:
        print("A conta de destino não existe.")
        bancodedados.close()
        return

    # Verificar saldo da conta de origem
    cursor.execute(
        "SELECT SUM(valor) FROM transacoes WHERE conta_id = ?", (conta_origem,)
    )
    saldo_origem = cursor.fetchone()[0]

    if saldo_origem is None:
        saldo_origem = 0

    # Verificar se o saldo é suficiente para a transferência
    if saldo_origem < valor:
        print("Saldo insuficiente para a transferência.")
        bancodedados.close()
        return

    # Realizar transferência
    try:
        bancodedados.execute("BEGIN")

        # Inserir transação de débito na conta de origem
        cursor.execute(
            "INSERT INTO transacoes (conta_id, tipo_transacao, categoria, descricao, valor, data) VALUES (?, ?, ?, ?, ?, date('now'))",
            (
                conta_origem,
                "Débito",
                "Transferência",
                f"Transferência para conta {conta_destino}",
                -valor,
            ),
        )

        # Inserir transação de crédito na conta de destino
        cursor.execute(
            "INSERT INTO transacoes (conta_id, tipo_transacao, categoria, descricao, valor, data) VALUES (?, ?, ?, ?, ?, date('now'))",
            (
                conta_destino,
                "Crédito",
                "Transferência",
                f"Transferência da conta {conta_origem}",
                valor,
            ),
        )

        bancodedados.commit()
        print("Transferência de fundos realizada com sucesso!")

    except sqlite3.Error as e:
        print("Ocorreu um erro ao realizar a transferência de fundos:", e)
        bancodedados.rollback()

    finally:
        bancodedados.close()
