import numpy as np
import matplotlib.pyplot as plt

inicio = float(input("Início: "))
fim = float(input("Fim: "))
   
x = np.linspace(inicio,fim,1001)

def f(x) -> float | int:
  return x**2

y = f(x)

plt.plot(x,y)
plt.show()