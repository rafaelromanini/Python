from datetime import datetime

tarifas = {
    "carro pequeno": {"base": 10, "adicional": 5},
    "carro grande": {"base": 15, "adicional": 10},
    "moto": {"base": 5, "adicional": 2}
}

veiculos = []

def cadastrar_tarifas():
    for tipo in tarifas.keys():
        print(f"\nCadastrando tarifas para {tipo}:")
        tarifas[tipo]["base"] = float(input("Informe o valor para o período de 3 horas: "))
        tarifas[tipo]["adicional"] = float(input("Informe o valor por hora adicional: "))

def registrar_entrada():
    placa = input("\nPlaca do veículo: ")
    tipo = input("Tipo do veículo (carro pequeno, carro grande, moto): ")
    entrada = input("Data e hora de entrada (dd/mm/aaaa hh:mm): ")
    veiculos.append({"placa": placa, "tipo": tipo, "entrada": entrada, "saida": "", "valor": 0})
    print("Veículo registrado com sucesso.")

def calcular_valor(entrada, saida, tipo):
    formato_tempo = "%d/%m/%Y %H:%M"
    tempo_entrada = datetime.strptime(entrada, formato_tempo)
    tempo_saida = datetime.strptime(saida, formato_tempo)
    duracao = (tempo_saida - tempo_entrada).total_seconds() / 3600 
    horas_extras = max(0, duracao - 3)
    valor = tarifas[tipo]["base"] + (tarifas[tipo]["adicional"] * horas_extras)
    return valor

def registrar_saida():
    placa = input("\nPlaca do veículo: ")
    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            saida = input("Data e hora de saída (dd/mm/aaaa hh:mm): ")
            veiculo["saida"] = saida
            valor_sem_desconto = calcular_valor(veiculo["entrada"], veiculo["saida"], veiculo["tipo"])
            forma_pagamento = input("Forma de pagamento (PIX/outro): ").lower()
            if forma_pagamento == "pix":
                valor_com_desconto = valor_sem_desconto * 0.95
            else:
                valor_com_desconto = valor_sem_desconto
            veiculo["valor"] = valor_com_desconto
            print(f"Valor a pagar: R${valor_com_desconto:.2f}")
            return
    print("Placa não encontrada.")

def relatorio_diario():
    total_arrecadado = sum(veiculo["valor"] for veiculo in veiculos if veiculo["valor"] > 0)
    print(f"\nTotal arrecadado: R${total_arrecadado:.2f}")

def sair():
    print("Saindo do sistema...")
    quit()

def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Tarifas")
        print("2. Registrar Entrada de Veículo")
        print("3. Registrar Saída de Veículo")
        print("4. Gerar Relatório Diário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_tarifas()
            case "2":
                registrar_entrada()
            case "3":
                registrar_saida()
            case "4":
                relatorio_diario()
            case "5":
                sair()
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    main()