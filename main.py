from abc import ABC, abstractmethod
from datetime import datetime


class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass 

    @property
    @abstractmethod
    def valor(self):
        pass 


class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        
        self._saldo = saldo
        self._numero = numero 
        self._agencia = agencia 
        self._cliente = cliente 
        self._historico = Historico()
    
    def saldo(self):
        return self._saldo 

    @classmethod
    def nova_conta(cls, Cliente, numero):
        return cls(Cliente, numero) 

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    def sacar(self, valor):

        if valor > self.saldo:
            print("Valor e maior do que seu saldo, tente com outro valor.")
        
        elif valor < 0:
            print("Valor invalido, tente novamente.")
        
        else:
            return True 


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor 
            print("Deposito realizado com sucesso.") 
        
        else:
            print("Houve um problema ao realizar seu deposito, tente novamente.")

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor 
    
    @property
    def valor(self):
        return self._valor 
    
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor 
    
    @property
    def valor(self):
        return self._valor 
    
    def registrar(self, conta):
        return super().registrar(conta)
    
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta._historico.adicionar_transacao(self)

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_de_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_de_saques = limite_de_saques

class Historico:
    def __init__(self):
        self.transacoes = []
    
    @property
    def transacoes(self):
        return self.transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__nome__,
            "valor": transacao.valor, 
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
        })

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def contas(self):
        return self._contas 


    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_de_nascimento, endereco):
        super().__init__(self, endereco)
        self._cpf = cpf 
        self._nome = nome 
        self._data_de_nascimento = data_de_nascimento
        


