import sqlite3


def resumo_receitas_despesas_mes():
    from datetime import datetime

    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()

    # Lib datatime usada para receber o mês e ano atual
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Obtém o total de receitas do mês atual
    cursor.execute(
        "SELECT SUM(valor) FROM transacoes WHERE strftime('%m', data) = ? AND strftime('%Y', data) = ? AND tipo_transacao = 'C'",
        (mes_atual, ano_atual),
    )
    total_receitas = cursor.fetchone()[0]
    if total_receitas is None:
        total_receitas = 0

    # Obtém o total de despesas do mês atual
    cursor.execute(
        "SELECT SUM(valor) FROM transacoes WHERE strftime('%m', data) = ? AND strftime('%Y', data) = ? AND tipo_transacao = 'D'",
        (mes_atual, ano_atual),
    )
    total_despesas = cursor.fetchone()[0]
    if total_despesas is None:
        total_despesas = 0

    print("Resumo das Receitas e Despesas do Mês:")
    print(f"Total de Receitas: R${total_receitas:.2f}")
    print(f"Total de Despesas: R${total_despesas:.2f}")

    bancodedados.close()
