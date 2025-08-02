conjuntoA_str = input("Insira o conjunto A, números separados por vírgulas: ")
conjuntoB_str = input("Insira o conjunto B, números separados por vírgulas: ")

conjuntoA = set(conjuntoA_str.split(','))
conjuntoB = set(conjuntoB_str.split(','))

# União, interseção, diferença, diferença simetrica, complemento
union = conjuntoA | conjuntoB
intersection = conjuntoA & conjuntoB
diff = conjuntoA - conjuntoB
diff_sym = conjuntoA ^ conjuntoB

complementoA = union - conjuntoA
complementoB = union - conjuntoB

print(f"União: {union}")
print(f"Intersecção: {intersection}")
print(f"Diferença: {diff}")
print(f"Diferença simétrica: {diff_sym}")
print(f"Complemento A: {complementoA}")
print(f"Complemento B: {complementoB}")
