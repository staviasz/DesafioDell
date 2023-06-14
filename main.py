import sqlite3
import alterartransacao
import cadastrarconta
import extratodeconta
import mesclarcontas
import resumodascontas
import resumoreceitas
import saldo6meses
import saldo12meses
import transferirfundos
import deletarconta
import cadastrartransacao
import criartabelas


def exibir_menu():
    while True:
        print("--------Gerenciador de Contas Pessoais--------")
        print("1. Cadastrar Conta")
        print("2. Remover Conta")
        print("3. Mesclar Contas")
        print("4. Extrato da Conta")
        print("5. Incluir Transação")
        print("6. Editar a última transação")
        print("7. Transferir fundos")
        print("8. Resumo das contas")
        print("9. Resumo de receitas e despesas do mês")
        print("10. Saldo geral dos últimos 6 meses")
        print("11. Saldo geral dos últimos 12 meses")
        print("12. Sair do programa.")

        escolha = 0
        while escolha != 12:
            escolha = int(input("Digite o número da opção desejada: "))

            if escolha == 1:
                print("Opção 1 selecionada.")
                cadastrarconta.cadastrarcontas()

            elif escolha == 2:
                print("Opção 2 selecionada.")
                deletarconta.deletarconta()

            elif escolha == 3:
                print("Opção 3 selecionada.")
                mesclarcontas.mesclar_contas()

            elif escolha == 4:
                print("Opção 4 selecionada.")
                extratodeconta.extratoconta()

            elif escolha == 5:
                print("Opção 5 selecionada.")
                cadastrartransacao.cadastrar_transacao()

            elif escolha == 6:
                print("Opção 6 selecionada.")
                alterartransacao.alterar_ultima_transacao()

            elif escolha == 7:
                print("Opção 7 selecionada.")
                transferirfundos.transferir_fundos()

            elif escolha == 8:
                print("Opção 8 selecionada.")
                resumodascontas.resumo_das_contas()

            elif escolha == 9:
                print("Opção 9 selecionada.")
                resumoreceitas.resumo_receitas_despesas_mes()

            elif escolha == 10:
                print("Opção 10 selecionada.")
                saldo6meses.saldo_ultimos_meses()

            elif escolha == 11:
                print("Opção 11 selecionada.")
                saldo12meses.saldo_ultimo_ano()

            else:
                print("Saindo do programa")
                return


exibir_menu()
