import sqlite3
from datetime import datetime, timedelta


def saldo_ultimos_meses():

    bancodedados = sqlite3.connect("bancodell.db")
    cursor = bancodedados.cursor()

    # Obter a data de 6 meses atrás a partir do mês atual
    data_atual = datetime.now().date()
    data_inicio = data_atual - timedelta(days=180)

    # Iterar pelos últimos 6 meses
    for i in range(6):
        data_final = data_inicio + timedelta(days=30)  # Assumindo 30 dias para cada mês
        data_inicio_formatada = '01'+ data_inicio.strftime('/%m/%Y')
        data_final_formatada = '30' + data_final.strftime('/%m/%Y')
        # Obter o saldo total do mês atual
        # print(data_inicio, data_final)
        print(data_inicio_formatada, data_final_formatada)
        cursor.execute(
            "SELECT SUM(valor) FROM transacoes WHERE data >=  ? AND data < ?",
            (data_inicio_formatada, data_final_formatada),
        )
        saldo = cursor.fetchone()[0]
        if saldo is None:
            saldo = 0

        # Exibir o saldo do mês atual
        mes = data_inicio.strftime("%B")  # Obtém o nome do mês
        ano = data_inicio.year
        print(f"Saldo de {mes} {ano}: R${saldo:.2f}")

        # Atualizar as datas para o próximo mês
        data_inicio = data_inicio + timedelta(days=30)
        print(data_inicio)

    bancodedados.close()
