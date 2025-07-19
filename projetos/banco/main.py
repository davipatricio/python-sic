from clientes import Cliente
from produtos import ChequeEspecialProduto, SeguroCelularProduto
from datetime import date

davi = Cliente(nome="Davi", cpf="23", agencia=1, sede=0, saldo=500)

davi.produtosContratados.extend(
  [
    ChequeEspecialProduto(habilitado=True, limite=1500),
    SeguroCelularProduto(habilitado=True, usos=0, inicioApolice=date(2025,1,1), fimApolice=date(2026,12,31), marca="Samsung", imei="123")
  ]
)

camila = Cliente(nome="Davi", agencia=1, saldo=0)

print(davi.saldo, camila.saldo)
davi.transferir(camila, 1000)

print(davi.saldo, camila.saldo)