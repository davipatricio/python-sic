from math import pi

def tipo(n: float | str) -> str:
  if isinstance(n, str):
    try:
      n = float(n)
    except ValueError:
      complex(n)
      return "complexo"
          
  # natural ou inteiro
  if int(n) == float(n):
    if n >= 0:  # pyright: ignore[reportOperatorIssue]
      return "natural"
    else:
      return "inteiro"
  # racional ou irracional
  else:
    # detectar se há mais de 6 casas decimais
    len_casas = len(str(n).split('.')[1])
    if len_casas >= 6:
      return "irracional"

  return "racional"

print(f"10j: {tipo("10j")}")
print(f'10: {tipo("10")}')
print(f'2/4: {tipo(2/4)}')
print(f'7/8: {tipo(7/8)}')
print(f'10.512983: {tipo(10.512983)}')
print(f'19.02: {tipo(19.02)}')
print(f'Pi: {tipo(pi)}')
print(f'-5: {tipo(-5)}')
print(f'-5: {tipo(-5)}')
print(f'-43: {tipo(-43)}')
print(f'-66.6: {tipo(-66.6)}')