menu = """
        ########## MENU ##########

        [1] Depósito
        [2] Saque
        [3] Extrato
        [0] Sair
        
        ########## MENU ##########
"""

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Informe o valor do depósito: "))

        if deposito < 0:
            print("Não é possível depositar um valor negativo.")
        else:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print("Saldo: ", saldo)

    elif opcao == 2:
        saque = float(input("Informe o valor do saque: "))

        if saldo < saque:
            print("Você não possui esse valor em sua conta, seu saldo atual é: ", saldo)
        elif saque <= 0:
            print("Tente um valor positivo.")
        elif saque > 500:
            print("O limite do valor de saque é: ", LIMITE)
        elif numero_saques == LIMITE_SAQUES:
            print("Você atingiu o máximo de saques diários.")
        else:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1
            print("Saldo: ", saldo)

    elif opcao == 3:
        
        if extrato == "":
            print("############## EXTRATO ##############")
            print("Não foram realizadas movimentações.\n")
            print(f"Saldo atual da conta: R${saldo:.2f}")
            print("#####################################")
        else:
            print("############## EXTRATO ##############")
            print(extrato)
            print(f"Saldo atual da conta: R${saldo:.2f}")
            print("#####################################")
            

    elif opcao == 0:
        break
    else:
        print("Operação invalida, tente novamente.")