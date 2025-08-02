import sys
import platform

if sys.platform == "win32":
  win_ver = platform.win32_ver()[0]
  print(f"Você está executando Windows {win_ver}.")
elif sys.platform == "darwin":
  macos_ver = platform.mac_ver()
  print(f"Você está executando MacOS {macos_ver}")
elif sys.platform == "linux":
  print("Você está executando Linux.")
else:
  print(f"Você está executando um sistema operacional ({sys.platform}).")
