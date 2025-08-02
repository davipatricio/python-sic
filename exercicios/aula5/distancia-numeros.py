from math import sqrt

n1 = int(input("Número 1 para absoluto e distânca 1D: "))
n2 = int(input("Número 2 para absoluto e distânca 1D: "))

# Calcule o valor absoluto de dois números
print(f"\nDistância euclidiana entre dois números: {abs(n1-n2)}")


# Calcule a distância euclidiana entre dois números
dist = sqrt((n1-n2)**2)
print(f"Distância euclidiana entre dois números (1D): {dist}")

# Calcule a distância euclidiana entre dois pontos
x1=float(input("Insira a coordenada x1: "))
x2=float(input("Insira a coordenada x2: "))
y1=float(input("Insira a coordenada y1: "))
y2=float(input("Insira a coordenada y2: "))

dist = sqrt(
    (x2-x1)**2+(y2-y1)**2
)
print(f"Distância euclidiana entre dois pontos (x=({x1},{x2}),y=({y1},{y2})): {format(dist, '.2f')}")
