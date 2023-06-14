import sqlite3


def alterar_ultima_transacao():
    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()
    conta_id = input("Digite o ID da conta: ")

    # Obtendo a última transação da conta escolhida
    cursor.execute(
        "SELECT * FROM transacoes WHERE conta_id = ? ORDER BY data DESC LIMIT 1",
        (conta_id,),
    )
    ultima_transacao = cursor.fetchone()

    # Verificando se a transação foi encontrada
    if ultima_transacao is None:
        print("Não há transações para esta conta.")
        bancodedados.close()
        return

    # Exibindo os detalhes da última transação
    print("Detalhes da última transação:")
    print("ID:", ultima_transacao[0])
    print("Tipo de transação:", ultima_transacao[2])
    print("Categoria:", ultima_transacao[3])
    print("Descrição:", ultima_transacao[4])
    print("Valor:", ultima_transacao[5])
    print("Data:", ultima_transacao[6])

    # Solicitando a alteração desejada
    print("\nDigite os novos valores:")
    tipo_transacao = input("Tipo de transação: ")
    categoria = input("Categoria: ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    data = input("Data (formato DD/MM/AAAA): ")

    # Atualizando os valores da última transação
    cursor.execute(
        "UPDATE transacoes SET tipo_transacao = ?, categoria = ?, descricao = ?, valor = ?, data = ? WHERE ID = ?",
        (tipo_transacao, categoria, descricao, valor, data, ultima_transacao[0]),
    )
    bancodedados.commit()

    print("Transação atualizada com sucesso!")
    bancodedados.close()
