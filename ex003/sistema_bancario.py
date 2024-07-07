import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.conta = []

    def realizar_transacao(self, conta, transacao):
        transacao.reristrar(conta)

    def adicionar_conta(self, conta):
        self.conta.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historioco(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n\033[0;30;41m Operação falhou! Você não tem saldo suficiente. \033[m")

        elif valor > 0:
            self.saldo -= valor
            print("\n\033[0;30;42m Saque realizado com sucesso! \033[m")
            return True

        else:
            print("\n\033[0;30;41m Operação falhou! O valor informado é inválido. \033[m ")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n \033[0;30;42m Depósito realizado com sucesso!. \033[m")

        else:
            print("\n \033[0;30;41m Operação falhou! o valor informado é inválido. \033[m")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historioco.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limete
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n\033[0;30;41m Operação falhou! O valor do saque execeu o limit. \033[m")

        elif excedeu_saques:
            print("\n\033[0;30;41m Oparação falhou! Número máximo de saques excedido. ")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def tramsacoes(self):
        return self._transacoes
    
    def adinionar_transacoes(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-Y %H:%M:%s")
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
class Deposito(Transacao):
    def __init__(self,valor):
        self._valor - valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depoistar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    menu = """\n
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo ucuário
    [q]\tSair
    => """

    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.conta:
        print("\n\033[0;30;41m Cliente não possui conta! \033[m")
        return
    # FIXME: Não permite o cliente escolher a conta
    return cliente.contas[0]

def depoistar(cliente):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, cliente)

    if not cliente:
        print("\n \033[0;30;41m Cliente não encontrado! \033[m")
        return
    
    valor = float(input("informe o valor do depósito: "))
    Transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, Transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n\033[0;30;41m Cliente não encontrado! \033[m")

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not clientes:
        print("\n\033[0;30;41m Cliente não encontrado! \033[m")

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n=============== EXTRATO ===============")
    transacoes = conta.historico.transacoes

    extrato = ""

    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato _= f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_cliente(clientes):
    cpf = input("informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n\033[0;30;41m Já existe cliente com esse CPF\033[m")

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradura, neu - bairro - cidade/sigla estado): ")
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.appende(cliente)

    print("\nn\033[0;30;42m Cliente criado com SUCESSO! ")

def criar_conta(numero_conta, cliente, contas):
    cpf = input("Informe o CPF do Cliente: ")
    cliente = filtrar_cliente(cpf, cliente)

    if not cliente:
        print("\n\033[0;30;41m Cliente não encontrado, fluxo de criação de conta encerrado!\033[m")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n\033[0;30;42m Conta criada com seucesso! \033[m")

def listar_contas(contas):
    for conta in contas:
        print("=" * 20)
        print(textwrap.dedent(str(conta))) 

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 'd':
            depoistar(clientes)
        
        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas):

        elif opcao == "q":
            break

        else:
            print("\n\033[0;30;41m Operação Inválida, por favor selecione novamente a operação desejada. \033[m")
