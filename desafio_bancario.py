menu='''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>'''

saldo=0
limite_saque=500
extrato=f"Extrato".center(50,"*")
numeros_saque=0
LIMITES_SAQUES=3
valor_saque=1000
valor_deposito=0
quantidade_depositos=0
quantidade_saque=0

while True:
    opcao=input(menu)

    if opcao=="d":
        valor_deposito=0
        confirmacao=input("Você escolheu depositar, correto? Digite \n 1, se sim, \n 2, se não.\n")
        if confirmacao=="1":
            while valor_deposito<=0:
                valor_deposito=float(input("Quanto deseja depositar? (Favor digitar um valor positivo.)\n"))
                if valor_deposito>0:
                    saldo=saldo+valor_deposito
                    quantidade_depositos=quantidade_depositos+1
                    extrato=extrato+f"\nDepósito ({quantidade_depositos}): R${valor_deposito:.2f}.\n Saldo: R${saldo:.2f}.\n"
                    confirmacao_viualizacao_saldo=input(f"Você depositou: R${valor_deposito}. \n Deseja saber seu saldo? \n 1: Sim \n 2: Não \n")
                    if confirmacao_viualizacao_saldo=="1" or confirmacao_viualizacao_saldo=="Sim":
                        print(f"Seu saldo é: R${saldo: .2f}")
                    else:
                        print("Até mais.")
        else:
            print("Irei dar as opções novamente, para que você possa escolher a opção que realmente deseja.")                
    elif opcao=="s":
        confirmacao=input("Você escolheu sacar, correto? Digite \n 1, se sim, \n 2, se não.\n")
        if confirmacao=="1" and LIMITES_SAQUES!=0:
            valor_saque=float(input("Quanto deseja sacar? (Favor digitar um valor positivo e menor ou igual ao dinheiro em sua conta.)\n"))
            if valor_saque>0 and valor_saque<=saldo and valor_saque<=limite_saque:
                saldo=saldo-valor_saque
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
                print("Você não tem saldo suficiente.")
        elif LIMITES_SAQUES<=0:
            print(f"Você excedeu a quantia de saques.")
        else:
            print(f"Irei dar as opções novamente, para que você possa escolher a opção que realmente deseja.")
    elif opcao=="e":
        confirmacao=input("Você escolheu o extrato, correto? Digite \n 1, se sim, \n 2, se não.\n")
        if confirmacao=="1":
            if LIMITES_SAQUES==3 and quantidade_depositos==0:
                print(extrato)
                print("Você não fez nenhuma nenhuma movimentação ou operação em sua conta.")
            else:
                print(extrato)
        elif confirmacao=="2":
            print(f"Irei dar as opções novamente, para que você possa escolher a opção que realmente deseja.")
        else:
            print("Não escolheu nada.")
    elif opcao=="q":
        print(f"Você escolheu sair da operação.")
        break
    else:
        print("Opção inválida, por favor selecione novamente e, de preferência, um valor(letra) válido(válida).")

