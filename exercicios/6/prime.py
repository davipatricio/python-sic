import os

# Calcular primos
primos = []
for n in range(1, 1000+1):
  prime = True
  for i in range(2, n):
    if n % i == 0:
     prime = False
  if prime:
    primos.append(n)

num = int(input("Digite um número (de 0 a 1000): "))
n_multiplo = float(input("Digite um número para verificar se é multiplo: "))

if num>=1000:
  print("Número muito grande.")
  os.exit(1)

if num % n_multiplo==0:
  print(f"{num} é multiplo de {n_multiplo}")
else:
  print(f"{num} não é multiplo de {n_multiplo}")

if num in primos:
  print(f"Número {num} é primo")
else:
  print(f"Número {num} não é primo")