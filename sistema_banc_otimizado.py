def menu():
    menu = """\n
    ======================= MENU =======================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuário
    [7] Sair
    => """
    return int(input(menu))

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("\n@@@ O valor informado é inválido. @@@")
    else:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("\n==== Depósito realizado com sucesso! ====")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > limite:
        print("\n@@@ O valor informado ultrapassa o limite. @@@")
    elif numero_saques >= limite_saques:
        print("\n@@@ O limite de saques diário foi atingido. @@@")
    elif valor > saldo:
        print("\n@@@ O valor informado ultrapassa o valor do saldo em conta. @@@")
    elif valor <= 0:
        print("\n@@@ Informe um valor válido. @@@")
    else:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
        print("\n==== Saque realizado com sucesso! ====")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================== EXTRATO ==================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR${saldo:.2f}")
    print("==============================================")

def criar_usuario(usuarios):
    cpf = input("Informe seu cpf (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Usuário já existente! @@@")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: (Logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n==== Conta criada com sucesso! ====")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}    
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    LIMITE = 500

    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor_deposito = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)
        elif opcao == 2:
            valor_saque = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor_saque,
                extrato=extrato,
                limite=LIMITE,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 4:
            criar_usuario(usuarios)
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 7:
            break
        else:
            print("Selecione uma opção válida.")

main()