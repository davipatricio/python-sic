categories = ["animacao", "drama", "aventura"]

age = int(input("Qual sua idade? "))
favorite_category = str(input("Entre animação, drama e aventura, qual seu gênero de filme favorito? "))

if favorite_category not in categories:
  print(f"A categoria {favorite_category} é inválida. Deve ser uma entre: {', '.join(categories)}")
  exit()

if age <= 5:
  print("Saia das telas.")
  exit()


if favorite_category == "drama":
  print("\nFilmes de drama que você talvez possa gostar baseado em sua idade e interesse:")
  if age >= 17:
    print(" - Ainda Estou Aqui (2024)\n - Vitória (2025)\n - Que Horas Ela Volta? (2015)")
  else:
    print(" - Querido Menino\n - Não Atire\n - O Filho de Jean")


if favorite_category == "aventura":
  print("\nFilmes de aventura que você talvez possa gostar baseado em sua idade e interesse:")
  if age >= 17:
    print(" - Avatar (2022)\n - The Beekeper (2024)\n - Jogos Vorazes: Em Chamas (2013)")
  else:
    print(" - Detetives do Prédio Azul\n - Tainá 2\n - Turma da Mônica em Uma Aventura no Tempo")

if favorite_category == "animacao":
  print("\nFilmes de animação que você talvez possa gostar baseado em sua idade e interesse:")
  if age >= 17:
    print(" - Como Treinar seu Dragão (2025)\n - O Rei Leão (2019)\n - Toy Story 4 (2019)")
  else:
    print(" - Lilo & Stitch\n - Flow\n - Jurassic World")
