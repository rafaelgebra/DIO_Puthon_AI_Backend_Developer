import textwrap
from time import sleep


def menu():
        
        menu = """\n
        ===================== MENU =====================  
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
        => """

        return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: \tR$ {valor:.2f}\n"
        print("\n\033[0;30;42m Deposito realizado com sucesso! \033[m ")
    else:
        print("\n\033[0;30;41m Operação falhou! O valor informado é inválido. \033[m")

    return saldo, extrato
    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n\033[0;30;41m Operação falhou! Você não tem saldo suficiente. \033[m")
    
    elif excedeu_limite:
        print("\n\033[0;30;41m Opração falhou! O valor do saque excedeu o limite. \033[m")

    elif excedeu_saques:
        print("\n\033[0;30;41m Operação falhou! Número máximo de saques excedido. \033[m")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\t R$ {valor:.2f}\n"
        numero_saques += 1
        #print(numero_saques)
        print("\n\033[0;30;42m Saque realizado com sucesso! \033[m")
        
    else:
        print("\n\033[0;30;41m Operação falhou! O valor informado é inválido. \033[m")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}")
    print("\n=======================================")


def criar_usuario(usuarios):
    ""

def filtrar_usuario(cpf, usuario):
    ""

def criar_conta(agencia, numero_conta, usuarios):
    ""

def listar_contas(contas):
    ""

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        sleep(1)
        if opcao == "d":
            valor = float(input("informe o valor do depódito: "))

            saldo, extrato = (depositar(saldo, valor, extrato))

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                conta.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("\n\033[0;30;41sm Operação inválida, por favor selecione novamente a operação desejada \033[m")
main()