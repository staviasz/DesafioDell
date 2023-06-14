import sqlite3


def mesclar_contas():
    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contas (
            conta_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            saldo REAL
        )
    """
    )

    cursor.execute("SELECT conta_id, numero_conta FROM contas")
    contas = cursor.fetchall()
    print("Contas disponíveis para mesclar:")
    for conta in contas:
        print(f"{conta[0]} - {conta[1]}")

    # Solicitar ao usuário que selecione as contas a serem mescladas
    conta_origem = int(input("Selecione o número da conta de origem: "))
    conta_destino = int(input("Selecione o número da conta de destino: "))

    # Verificar se as contas selecionadas existem
    cursor.execute("SELECT COUNT(*) FROM contas WHERE conta_id = ?", (conta_origem,))
    conta_origem_existe = cursor.fetchone()[0] > 0

    cursor.execute("SELECT COUNT(*) FROM contas WHERE conta_id = ?", (conta_destino,))
    conta_destino_existe = cursor.fetchone()[0] > 0

    if not conta_origem_existe or not conta_destino_existe:
        print("Uma ou ambas as contas selecionadas não existem.")
        return

    # Obter as transações da conta de origem
    cursor.execute(
        "SELECT * FROM transacoes WHERE conta_id = ? ORDER BY data", (conta_origem,)
    )
    transacoes_origem = cursor.fetchall()

    # Atualizar o ID da conta nas transações para a conta de destino
    for transacao in transacoes_origem:
        cursor.execute(
            "UPDATE transacoes SET conta_id = ? WHERE transacao_id = ?",
            (conta_destino, transacao[0]),
        )

    # Excluir a conta de origem
    cursor.execute("DELETE FROM contas WHERE conta_id = ?", (conta_origem,))

    bancodedados.commit()
    bancodedados.close()

    print("Contas mescladas com sucesso!")
