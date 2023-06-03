import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def confirmar(confirmacao):
    if (confirmacao=="1" or confirmacao=="Sim" or "sim"):
        return True
    elif confirmacao=="2" or confirmacao=="2":
        return False
    else:
                print("Não escolheu nada.")

def depositar(saldo,valor_deposito,extrato,quantidade_depositos):
    if valor_deposito>0:
        saldo=saldo+valor_deposito
        extrato=extrato+f"\nDepósito ({quantidade_depositos}): R${valor_deposito:.2f}.\n Saldo: R${saldo:.2f}.\n"
        confirmacao_viualizacao_saldo=input(f"Você depositou: R${valor_deposito}. \n Deseja saber seu saldo? \n 1: Sim \n 2: Não \n")
        if confirmar(confirmacao_viualizacao_saldo)==True:
            print(f"Seu saldo é: R${saldo: .2f}")
        else:
            print("Até mais.")
    return saldo,extrato

def sacar(*, saldo, valor_saque, extrato, limite_saque, quantidade_saque):
    '''excedeu_saldo=valor_saque>saldo
    excedeu_numero_saque:quantidade_saque==limite_saques
    excedeu_limite:valor_saque>limite_saque

    if excedeu_saldo:
        print("Excedeu limite de saque")'''
    if valor_saque>0 and valor_saque<=saldo and valor_saque<=limite_saque:
        saldo=saldo-valor_saque
        quantidade_saque=quantidade_saque+1
        extrato=extrato+f"Saque({quantidade_saque}): R${valor_saque}.\n Saldo: R${saldo}.\n"
        print(f"Seu saldo agora é: R${saldo: .2f}. \n Você sacou: R${valor_saque:.2f}")
    elif valor_saque<0:
        print("Você digitou um valor negativo(inválido).")
    elif valor_saque>limite_saque and valor_saque>saldo:
        print(f"Você excedeu o limite de saque {limite_saque} e não tem saldo suficiente.")
    elif valor_saque>saldo:
        print(f"Você não tem saldo suficiente.")
    elif valor_saque>limite_saque:
        print("Você excedeu o limite de saque.")
    else:
        print("Você não tem saldo suficiente.")
    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato,quantidade_saque,quantidade_depositos):
    if quantidade_saque==0 and quantidade_depositos==0:
                    print(extrato)
                    print("Você não fez nenhuma nenhuma movimentação ou operação em sua conta.")
    else:
                    print(extrato)
                    print(f"Seus saldo é {saldo: .2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("=== Usuário criado com sucesso! ===")
    
def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados=[usuario for usuario in usuarios if usuarios["cpf"]==cpf] #se dentro de algum valor de usuários já existir o cpf dado, esse primeiro usuário encontrado é guardado na lista usuarios_filtrados
    return usuarios_filtrados[0] if usuarios_filtrados else None #A parte if usuarios_filtrados é uma condição que verifica se a lista usuarios_filtrados está vazia ou não. Se a lista estiver vazia, a condição é considerada falsa e o valor retornado será None.

def criar_contas(agencia, numero_conta, usuarios):
    cpf=input("Informe seu CPF: ")
    usuario=filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    print("Usuário não encontrado. Crie um antes de tentar criar uma conta.")

def listar_contas(contas):
    for conta in contas:
        linha=f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
def main():
    AGENCIA="0001"
    LIMITES_SAQUES=3

    saldo=0
    limite_saque=500
    extrato=f"Extrato".center(50,"*")
    valor_saque=1000
    valor_deposito=0
    quantidade_depositos=0
    quantidade_saque=0
    usuarios = []
    contas = []

    while True:
        opcao=menu()

        if opcao=="d":
            valor_deposito=0
            confirmacao=input("Você escolheu depositar, correto? Digite \n 1, se sim, \n 2, se não.\n")
            if confirmar(confirmacao)==True:
                while valor_deposito<=0:
                    valor_deposito=input("Quanto deseja depositar? (Favor digitar um valor positivo.)\n")
                    try:
                        valor_deposito=float(valor_deposito)
                        if valor_deposito>0:
                            quantidade_depositos=quantidade_depositos+1
                            saldo,extrato=depositar(saldo,float(valor_deposito),extrato,quantidade_depositos)
                        else:
                            print("Digite um número positivo.")
                    except:
                        print("Isso não é um número.")
                        valor_deposito=0
                        continue
            else:
                print("Irei dar as opções novamente, para que você possa escolher a opção que realmente deseja.")               

        elif opcao=="s":
            confirmacao=input("Você escolheu sacar, correto? Digite \n 1, se sim, \n 2, se não.\n")
            try:
                if confirmar(confirmacao)==True and LIMITES_SAQUES>=quantidade_saque:
                    valor_saque=input(f"Quanto deseja sacar? (Favor digitar um valor positivo e menor ou igual ao dinheiro em sua conta.)\n")
                    
                    valor_saque=float(valor_saque)
                    #if valor_saque>0 and valor_saque<=saldo and valor_saque<=limite_saque:
                    saldo,extrato=sacar(saldo=saldo,
                    valor_saque=valor_saque,
                    extrato=extrato,
                    limite_saque=limite_saque,
                    quantidade_saque=quantidade_saque,)
                    #else:
                    #print("Digite um número positivo.")
                    
                    #if valor_saque>0 and valor_saque<=saldo and valor_saque<=limite_saque:
                    ''' saldo=saldo-valor_saque
                        quantidade_saque=quantidade_saque+1
                        extrato=extrato+f"Saque({quantidade_saque}): R${valor_saque}.\n Saldo: R${saldo}.\n"
                        LIMITES_SAQUES=LIMITES_SAQUES-1
                        print(f"Seu saldo agora é: R${saldo: .2f}. \n Você sacou: R${valor_saque:.2f}")
                    elif valor_saque<0:
                        print("Você digitou um valor negativo(inválido).")
                    elif valor_saque>limite_saque and valor_saque>saldo:
                        print(f"Você excedeu o limite de saque {limite_saque} e não tem saldo suficiente.")
                    elif valor_saque>saldo:
                        print(f"Você não tem saldo suficiente.")
                    elif valor_saque>limite_saque:
                        print("Você excedeu o limite de saque.")
                    else:
                        print("Você não tem saldo suficiente.")'''
                elif LIMITES_SAQUES==quantidade_saque:
                    print(f"Você excedeu a quantia de saques.")
                else:
                    print(f"Irei dar as opções novamente, para que você possa escolher a opção que realmente deseja.")
            except ValueError:
                print(f"Você não digitou um valor válido.")

        elif opcao=="e":
            if confirmar(input("Você escolheu o extrato, correto? Digite \n 1, se sim, \n 2, se não.\n")):
                exibir_extrato(saldo,extrato=extrato,quantidade_saque=quantidade_saque,quantidade_depositos=quantidade_depositos)
            elif confirmar(confirmacao):
                print(f"Irei dar as opções novamente, para que você possa escolher a opção que realmente deseja.")
            else:
                print("Não escolheu nada.")
        
        elif opcao=="nu":
            criar_usuario(usuarios)

        elif opcao=="nc":
            numero_conta=len(contas)+1
            conta=criar_contas(AGENCIA,numero_conta,usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao=="q":
            print(f"Você escolheu sair da operação.")
            break
        
        else:
            print("Opção inválida, por favor selecione novamente e, de preferência, um valor(letra) válido(válida).")

main()