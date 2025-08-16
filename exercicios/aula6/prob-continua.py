import numpy as np
from scipy import stats

# Simulação de dados (pressão arterial sistólica em mmHg)
np.random.seed(42)
grupo_controle = np.random.normal(loc=140, scale=10, size=30)  # Medicamento atual
grupo_teste = np.random.normal(loc=135, scale=10, size=30)     # Novo medicamento

# Estatísticas descritivas
print("Média grupo controle:", np.mean(grupo_controle))
print("Média grupo teste:", np.mean(grupo_teste))

# Teste de hipótese: t-test para duas amostras independentes
t_stat, p_value = stats.ttest_ind(grupo_controle, grupo_teste, alternative='greater')

# Resultado
print("\nResultado do teste t:")
print("Estatística t:", round(t_stat, 3))
print("Valor-p:", round(p_value, 3))

# Interpretação
alpha = 0.05
if p_value < alpha:
    print("🔬 Rejeitamos H₀: O novo medicamento é mais eficaz.")
else:
    print("✅ Não rejeitamos H₀: Não há evidência suficiente de que o novo medicamento é melhor.")