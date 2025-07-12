import os
import sys
import platform

win_ver = platform.win32_ver()[0]
os_data = f"Windows {win_ver}"

env_names = ", ".join(list(dict(os.environ).keys()))
loaded_modules = ", ".join([mod for mod in sys.modules])

with open(file="./ambient-info.txt", mode="w", encoding="utf8") as file:
  file.write(f"Informações do sistema:\n\nSistema Operacional: {os_data}\nNome das Váriaveis de Ambiente: {env_names}\nMódulos carregados: {loaded_modules}")


'''
elif sys.platform == "darwin":
  macos_ver = platform.mac_ver()
  os_data = f"MacOS {macos_ver}"
elif sys.platform == "linux":
  os_data = "Linux"
'''
