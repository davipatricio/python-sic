from dataclasses import dataclass
from datetime import date

@dataclass
class ProdutoBanco:
  habilitado: bool = False

@dataclass
class ChequeEspecialProduto(ProdutoBanco):
  limite: float = 0

  def utilizar(self, valor: float):
    if (valor > self.limite):
      raise "Limite indisponível"

    self.limite -= valor
    return True

  def tem_limite(self):
    if (self.limite >= 1):
      return True
    return False

@dataclass
class BaseSeguroProduto(ProdutoBanco):
  usos: int = 0
  inicioApolice: date = None
  fimApolice: date = None

@dataclass
class SeguroVidaProduto(BaseSeguroProduto):
  pass

@dataclass
class SeguroCelularProduto(BaseSeguroProduto):
  marca: str = None
  imei: str = None
  pass

@dataclass
class SeguroAutomovelProduto(BaseSeguroProduto):
  pass