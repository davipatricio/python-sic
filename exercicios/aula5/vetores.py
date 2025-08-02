from math import sqrt
import numpy as np

type Vetor = tuple[int,int,int]

vetor1: Vetor = (16,32,64)
vetor2: Vetor = (128,256,512)

# Norma vetorial
def norma(vetor: Vetor) -> float:
  return sqrt(sum(x**2 for x in vetor))

# Produto interno
def produto(vetor1: Vetor, vetor2: Vetor) -> float:
  return np.dot(vetor1, vetor2)

# Transpose
def transpose(vetor1: Vetor, vetor2: Vetor):
  return np.transpose([vetor1, vetor2])

# Matrizes especiais
def special_matrix():
  return np.eye(3, 3)

print(norma(vetor1))
print(produto(vetor1, vetor2))
print(transpose(vetor1, vetor2))
print(special_matrix())
