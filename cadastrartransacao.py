import sqlite3


def cadastrar_transacao():
    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()

    conta_id = int(input("Digite o número da conta: "))
    tipo_transacao = input("Digite o tipo de transação DEBITO ou CREDITO")
    categoria = input("Digite a categoria da transação ex: casa")
    descricao = input("Digite uma descrição para a transação: ")
    valor = float(input("Digite o valor :"))
    data = input("Digite a data em formato DD/MM/AAA :")

    cursor.execute(
        "INSERT INTO transacoes (conta_id, tipo_transacao, categoria, descricao, valor, data) VALUES (?, ?, ?, ?, ?, ?)",
        (conta_id, tipo_transacao, categoria, descricao, valor, data),
    )

    print("Transação cadastrada com sucesso!")
    bancodedados.commit()
    bancodedados.close()
