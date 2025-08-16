# temperatura, distancia, tempo

tipo = input("O que você deseja converter: temperatura, distância, tempo? ")

if tipo not in ["temperatura", "distancia" "distância", "tempo"]:
  print("Dado ainda não suportado.")
  exit()


match tipo:
  case "temperatura":
    unit = input("Qual unidade de origem (Celsius, Fahrenheit, Kelvin)? ")
    unit_convert = input("Para qual unidade converter (Celsius, Fahrenheit, Kelvin)? ")
    temp = float(input("Qual é a temperatura? "))
    
    if unit not in ["celsius", "fahrenheit", "kelvin"] or unit_convert not in ["celsius", "fahrenheit", "kelvin"]:
      print("Unidade ainda não suportada")
      exit()
    
    if unit == 'celsius':
      if unit_convert == 'fahrenheit':
        final = temp * 1.8 + 32
        print(f"{temp}ºC em ºF é {final}")
      elif unit_convert == 'kelvin':
        final = temp + 273.15
        print(f"{temp}ºC em ºK é {final}")

    if unit == 'fahrenheit':
      if unit_convert == 'celsius':
        final = (temp-32)/(9/5)
        print(f"{temp}ºF em ºC é {final}")
      elif unit_convert == 'kelvin':
        final = (temp+459.67)*5/9
        print(f"{temp}ºF em ºK é {final}")

    if unit == 'kelvin':
      if unit_convert == 'celsius':
        final = (temp-273.15)
        print(f"{temp}ºK em ºC é {final}")
      elif unit_convert == 'fahrenheit':
        final = temp*9/5-459.67
        print(f"{temp}ºK em ºF é {final}")


  case "tempo":
    unit = input("Qual unidade de origem (segundos, minutos, horas)? ")
    unit_convert = input("Para qual unidade converter (segundos, minutos, horas)? ")
    tempo = float(input("Qual o tempo? "))
    
    if unit not in ["segundos", "minutos", "horas"] or unit_convert not in ["segundos", "minutos", "horas"]:
      print("Unidade ainda não suportada")
      exit()
    
    if unit == 'horas':
      if unit_convert == 'minutos':
        final = tempo*60
        print(f"{tempo} horas são {final} minutos")
      elif unit_convert == 'segundos':
        final = tempo*3600
        print(f"{tempo} horas são {final} segundos")

    if unit == 'minutos':
      if unit_convert == 'horas':
        final = tempo/60
        print(f"{tempo} minutos são {final} horas")
      elif unit_convert == 'segundos':
        final = tempo*60
        print(f"{tempo} minutos são {final} segundos")

    if unit == 'segundos':
      if unit_convert == 'horas':
        final = tempo/3600
        print(f"{tempo} segundos são {final} horas")
      elif unit_convert == 'minutos':
        final = tempo/60
        print(f"{tempo} segundos são {final} minutos")
