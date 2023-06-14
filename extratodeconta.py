import sqlite3


def extratoconta():
    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()
    cursor.execute("SELECT numero_conta FROM contas")
    contas = (
        cursor.fetchall()
    )  # Aqui usei um método fetchall para que retorne os resultados como uma lista de tuplas,
    # facilitando assim a iteração do for, já que a variável estará como uma lista,

    print("Digite o número da conta - As Contas disponíveis são:")
    for conta in contas:
        print(conta[0])

    conta_id = int(input("Digite o número da conta: "))
    cursor.execute(
        "SELECT * FROM transacoes WHERE conta_id = ? ORDER BY data", (conta_id,)
    )
    transacoes = cursor.fetchall()

    # Verificando se existem transações para a conta
    if len(transacoes) == 0:
        print("Não há transações para esta conta.")
        bancodedados.close()
        return

    saldo = 0.0
    print("Extrato da conta:")
    for transacao in transacoes:
        transacao_id = transacao[0]
        tipo_transacao = transacao[2]
        categoria = transacao[3]
        descricao = transacao[4]
        valor = transacao[5]
        data = transacao[6]
        saldo += valor

        print(f"ID: {transacao_id}")
        print(f"Tipo de transação: {tipo_transacao}")
        print(f"Categoria: {categoria}")
        print(f"Descrição: {descricao}")
        print(f"Valor: {valor}")
        print(f"Data: {data}")
        print(f"Saldo: {saldo}\n")

    bancodedados.close()
