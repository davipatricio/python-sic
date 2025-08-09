from scipy.stats import norm
import numpy as np
mu, sigma=0,1
p = norm.cdf(1.96,mu,sigma)
print(p)

dados=[10,15,20,25,30]
print("Média", np.mean(dados))
print("Mediana", np.median(dados))
print("Desvio", np.std(dados))