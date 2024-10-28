from enum import Enum
import re

class Clientes:

    clientes = []

 #definindo as caracteríscticas da classe clientes

    def __init__(self, nome, email, idade, senha):
        self.nome = nome
        self.email = email
        self.idade = int(idade)
        self.senha = senha
    def apresentar(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Idade: {self.idade}, Senha: {self.senha}"


class PlanoTipo(Enum):
    BASIC = 'basic'
    PREMIUM = 'premium'


class Plano:
    def __init__(self, nome, valor, beneficios):
        self.nome = nome
        self.valor = valor
        self.beneficios = beneficios

    @classmethod
    def planos_disponiveis(cls):
        return [plano.value for plano in PlanoTipo]


class ContratarPlano:
    def __init__(self, usuario, plano):
        self.usuario = usuario
        if plano not in Plano.planos_disponiveis():
            raise ValueError('Plano indisponível')
        self.plano = plano

    def mudar_plano(self, novo_plano):
        if novo_plano not in Plano.planos_disponiveis():
            raise ValueError('Plano inválido')
        self.plano = novo_plano


class Pagamento:
    def __init__(self, valor, forma_pagamento):
        self.valor = valor
        self.forma_pagamento = forma_pagamento

    def processar(self):
        # Lógica para processar o pagamento (integrar com gateway de pagamento, etc.)
        pass


class PagamentoCartao(Pagamento):
    def __init__(self, valor, numero_cartao, validade_cartao, cvv):
        super().__init__(valor)
        self.numero_cartao = numero_cartao
        self.validade_cartao = validade_cartao
        self.cvv = cvv

        # Validação básica (adicione mais validações conforme necessário)
        if not re.match(r'^\d{16}$', numero_cartao):
            raise ValueError("Número de cartão inválido")
        # ... outras validações


    def realizar_pagamento(self):
        print(f'Pagamento com cartão de {self.valor} realizado com sucesso')






