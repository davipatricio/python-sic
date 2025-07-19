from __future__ import annotations
from typing import Literal, List
from enum import Enum
from produtos import ProdutoBanco, ChequeEspecialProduto
from dataclasses import dataclass, field

class TipoCliente(Enum):
  ESTUDANTE = 1
  PEP = 2
  EXPEP = 3
  FAMOSO = 4
  CLT = 5
  AUTONOMO = 6

class TipoClienteFuncionario(Enum):
  INTERNO = 1
  EXTERNO = 2
  SETOR = 3

class TipoConta(Enum):
  PJ = 1
  FISICA = 2
  CORRENTE = 3
  POUPANCA = 4
  SALARIO = 5
  CONVENIO = 6
  CONJUNTA = 7
  MENOR_BLOQ_TRANSFERENCIAS = 8
  MENOR = 9
  TEENS = 10

@dataclass
class Cliente:
  # Dados pessoais
  nome: str = ""
  cpf: str = ""
  renda: float = 0.0
  # Conta
  saldo: float = 0.0
  sede: int = 0
  agencia: int = 0
  produtosContratados: List[ProdutoBanco] = field(default_factory=list)
  tipo: Literal['cliente', 'funcionario'] = 'cliente'
  tipoCliente: TipoCliente = None
  tipoConta: TipoConta = None

  def saque(self, valor: int):
    if (self.tipoConta == TipoConta.MENOR_BLOQ_TRANSFERENCIAS):
      raise "O tipo de conta não permite saques devido ao tipo da conta do cliente. Se já possui 18 anos, considere ir em uma agência."
    
    # Cliente sem saldo
    if (valor > self.saldo):
      # Regra de negócio: cliente possui cheque especial
      cheque_especial_cliente = self.__tem_cheque_especial__()
      if cheque_especial_cliente:
        print("Cliente tem cheque especial")
        try:
          # Erro caso cliente não tenha limite
          cheque_especial_cliente.utilizar(valor-self.saldo)
          self.saldo += valor-self.saldo
        except:
          raise "Saldo do cliente é menor do que o disponível. Considere aumentar o limite do cheque especial."
      else:
        raise "Saldo do cliente é menor do que o disponível. Considere contratar um cheque especial."

    # Subtrair saldo do cliente sacando
    self.saldo -= valor

    return self

  def transferir(self, cliente: Cliente, valor: int):
    if (self == cliente):
      raise "Não é possível transferir para si mesmo."
    if (self.tipoConta == TipoConta.MENOR_BLOQ_TRANSFERENCIAS):
      raise "O tipo de conta não permite transferências bancárias devido ao tipo da conta do cliente. Se já possui 18 anos, considere ir em uma agência."
    
    # Cliente sem saldo
    if (valor > self.saldo):
      # Regra de negócio: cliente possui cheque especial
      cheque_especial_cliente = self.__tem_cheque_especial__()
      if cheque_especial_cliente:
        print("Cliente tem cheque especial")
        try:
          # Erro caso cliente não tenha limite
          cheque_especial_cliente.utilizar(valor-self.saldo)
          self.saldo += valor-self.saldo
        except:
          raise "Saldo do cliente é menor do que o disponível. Considere aumentar o limite do cheque especial."
      else:
        raise "Saldo do cliente é menor do que o disponível. Considere contratar um cheque especial."

    # Subtrair saldo do cliente transferindo, após todas regras de negócio
    self.saldo -= valor
    cliente.saldo += valor

    return self

  def depositar(self, valor: int | float):
    if (self.tipoConta != TipoConta.SALARIO or self.tipoConta != TipoConta.MENOR_BLOQ_TRANSFERENCIAS):
      raise "Só é possível depositar diretamente em contas do tipo salário ou de menor dependente."
    self.saldo = float(valor)
    return self

  def __tem_cheque_especial__(self) -> ChequeEspecialProduto | False:
    for produto in self.produtosContratados:
      if isinstance(produto, ChequeEspecialProduto) and produto.habilitado == True:
        return produto
    return False

class FuncionarioCliente(Cliente):
  tipo = 'funcionario'
  tipoCliente: TipoClienteFuncionario