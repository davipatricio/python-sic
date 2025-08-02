import pandas as pd
from faker import Faker
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import random

fake = Faker('pt-br')

cargos = {
    'Junior': ['Assistente', 'Auxiliar', 'Estagiário', 'Analista de Suporte'],
    'Pleno': ['Analista', 'Desenvolvedor', 'Especialista', 'Engenheiro de Software'],
    'Sênior': ['Gerente', 'Coordenador', 'Arquiteto de Solução', 'Líder Técnico']
}

senioridades = list(cargos.keys())
dados = []

for i in range(1000):
  # escolher uma senioridade de forma aleatória
  senioridade_escolhida = random.choice(senioridades)
  # escolher um cargo de acordo com a senioridade
  cargo = random.choice(cargos[senioridade_escolhida])

  email = ""
  tipo_email = ""

  # Pessoas com cargo senior possuem mais cahcnes de ter e-mail corporativo
  if senioridade_escolhida == 'Sênior' and random.random()<0.8:
    email = fake.company_email()
    tipo_email = 'Corporativo'
  elif senioridade_escolhida == 'Pleno' and random.random()<0.5:
    email = fake.company_email()
    tipo_email = 'Corporativo'
  else:
    email = fake.free_email()
    tipo_email = 'Pessoal'

  dados.append({
      'nome': fake.name(),
      'tipo_email': tipo_email,
      'cargo': cargo,
      'senioridade': senioridade_escolhida,
      'email': email
  })

# Converter para um dataframe do pandas
df = pd.DataFrame(dados)

# preparar os dados (pre-processamento)
print('--- Amostra dos dados gerados---')
print(df.head())
print('\n'+'='*70+'\n')

# Converte tipo_email e senioridade em numeros, pois a ia trabalha com números
le_tipo_email = LabelEncoder()
le_senioridade = LabelEncoder()

# 'X' são as caracteristicas que usamos para prever (features)
x = df[['tipo_email']].copy()
x['tipo_email_encoded'] = le_tipo_email.fit_transform(x['tipo_email'])

# 'y' é o que queremos prever (target)
y = le_senioridade.fit_transform(df['senioridade'])

# passo 1: treinar o modelo de ia - dividir os dados, 80% treinar 20% testar
x_train, x_test, y_train, y_test = train_test_split(x[['tipo_email_encoded']], y, test_size=0.2, random_state=42)

# escolher um modelo de ia simples: árvore de decisão
model = DecisionTreeClassifier(random_state=42)

# treinar o modelo
model.fit(x_train, y_train)

print('Modelo treinado com sucesso!')
print('\n'+'='*70+'\n')

x_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, x_pred)
print(f'Acurácia do modelo: {accuracy*100:.2f}%')
print('\n'+'='*70+'\n')