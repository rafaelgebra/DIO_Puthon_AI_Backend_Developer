from time import sleep

menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """
usuario_altorizado = ("Rafael")
usuario_acesso = ""
opcao = ""
cont = 1
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    sleep(0.3)
    print(opcao)
    usuario_acesso = str(input("Insira o nome do usúario ou [Q] para sair: ")).strip().title()     
    if cont == 3:
            print("Conta bloqueada")
            break
    elif usuario_acesso == "Q":
         break
    
    if usuario_acesso != usuario_altorizado:
            print("Usuário não encontrado")
            cont += 1
            sleep(0.5)
    else:
        while True:
            sleep(0.5)
            opcao = input(menu)
            if opcao == 'd':
                valor = float(input("Informe o valor de deposito: "))
                if valor > 0:
                     saldo += valor
                     extrato += f"Deposito de R$ {valor:.2f}\n"
                     sleep(0.5)
                else:
                     print("Operação falhou! O valor informado é inválido.")
                     sleep(0.5)

            elif opcao == "s":
                valor = float(input("informe o valor do saque: "))
                sleep(0.5)
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saque >= LIMITE_SAQUES

                if excedeu_limite:
                    print("Operação falhou! O valor do saque excede limite. ")
                    sleep(0.5)
                    
                elif excedeu_saldo:
                    print("Operação falhou! Você não tem saldo suficiente. ")
                    sleep(0.5)

                elif excedeu_saques:
                    print("Operação falhou! Número de saque excedido. ")
                    sleep(0.5)

                elif valor >= 1:
                     saldo -= valor
                     numero_saque += 1
                     extrato += f"Saque: R$ {valor:.2f}\n"
                     sleep(0.5)

                else:
                     print("Operação falhou! O valor informado é inválido")
                     sleep(0.5)

            elif opcao == "e":  
                print("\n****************** EXTRATO ******************")
                sleep(0.3)
                print("Não foram realisadas movimentações. " if not extrato else extrato)
                sleep(0.3)
                print(f"\nSaldo: R$ {saldo:.2f} ")
                sleep(0.3)
                print("*********************************************")

            elif opcao == "q":
                break

            else:
                print("Operação inválida, Por favor selecionar novamente a operação desejada.")
    
        
