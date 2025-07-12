import os
import sys
import platform

# OS data
os_data = ""

if sys.platform == "win32":
  win_ver = platform.win32_ver()[0]
  os_data = "Windows {win_ver}"
elif sys.platform == "darwin":
  macos_ver = platform.mac_ver()
  os_data = "MacOS {macos_ver}"
elif sys.platform == "linux":
  os_data = "Linux"

# Environment names
env_names = ", ".join(list(dict(os.environ).keys()))

# Loaded modules
module_names = ", ".join([mod for mod in sys.modules])

with open(file="./ambient-info.txt", mode="w", encoding="utf8") as file:
  file.write(f"Informações do sistema:\n\nSistema Operacional: {os_data}\nNome das Váriaveis de Ambiente: {env_names}\nMódulos carregados: {module_names}")