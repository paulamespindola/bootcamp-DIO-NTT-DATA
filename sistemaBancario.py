saldoTotal = 0
oprDepositos = []
oprSaques = []
saquesRealizados = 0
limiteSaqueDiario = 3
limitePorSaque = 500.00

def imprimir_transacao(tipo, valor, indice):
    print(f'{indice}° {tipo}: {valor}')

def formatar_valor(valor):
    return f'R${valor:.2f}'

def deposito(valor):
    global saldoTotal
    if valor > 0:
        saldoTotal += valor
        oprDepositos.append(valor)
    else:
        print("ERRO!!\nPor favor, digite um valor positivo")

def saque(valor):
    global saldoTotal, saquesRealizados
    if saquesRealizados < limiteSaqueDiario:
        if valor > 0 and valor <= saldoTotal and valor <= limitePorSaque:
            saldoTotal -= valor
            oprSaques.append(valor)
            saquesRealizados += 1
        else:
            print("ERRO!!\nValor inválido ou excede o limite por saque")
    else:
        print("ERRO!!\nLimite diário de saques atingido")

def extrato():
    print('---------- Extrato -----------')
    if not oprDepositos and not oprSaques:
        print("Não foram realizadas movimentações.")
    else:
        if oprDepositos:
            print('Depósitos:')
            for i, valor in enumerate(oprDepositos, start=1):
                imprimir_transacao('Depósito', formatar_valor(valor), i)
        if oprSaques:
            print('Saques:')
            for i, valor in enumerate(oprSaques, start=1):
                imprimir_transacao('Saque', f'-{formatar_valor(valor)}', i)
        print(f'Saldo atual: {formatar_valor(saldoTotal)}')

def obter_valor(mensagem, valor_minimo=0, valor_maximo=None):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= valor_minimo:
                print(f"ERRO!!\nO valor deve ser maior que {valor_minimo:.2f}")
            elif valor_maximo is not None and valor > valor_maximo:
                print(f"ERRO!!\nO valor máximo permitido é {valor_maximo:.2f}")
            else:
                return valor
        except ValueError:
            print("ERRO!!\nEntrada inválida. Digite um número válido.")

def main():
    global saquesRealizados
    saquesRealizados = 0
    while True:
        print('----------- Sistema Bancário ------------')
        print('1 - Depositar')
        print('2 - Sacar')
        print('3 - Extrato')
        print('4 - Sair')

        opcao = obter_valor('Digite a opção desejada: ', valor_minimo=0, valor_maximo=4)

        if opcao == 1:
            valor = obter_valor('Digite o valor do depósito: ', valor_minimo=0)
            deposito(valor)
        elif opcao == 2:
            valor = obter_valor('Digite o valor do saque: ', valor_minimo=0, valor_maximo=limitePorSaque)
            saque(valor)
        elif opcao == 3:
            extrato()
        elif opcao == 4:
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
