# Simule um sensor de transito para um semaforo que toma decisão com base na presença de carros e dos pedestres

num_pedestres = 150
num_carros = 150

prioridade = "pedestres"

if num_pedestres == 0:
  prioridade = "carros"

elif num_carros == 0 and num_pedestres == 0:
  prioridade = "pedestres"

elif num_carros >= num_pedestres:
  print(num_carros/num_pedestres)
  if num_carros/num_pedestres>=1.9:
    prioridade = 'pedestres'
  else:
    prioridade = "carros"

elif num_pedestres >= num_carros:
  print(num_pedestres/num_carros)
  if num_pedestres/num_carros>=5:
    prioridade = 'carros'
  else:
    prioridade = "pedestres"

print(f"Numa rua com {num_pedestres} pedestres e {num_carros} carros, seria melhor prioziar {prioridade}")
