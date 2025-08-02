import sys

module_names = [mod for mod in sys.modules]
str_modules = "\n".join(module_names)

print(f"Há {len(module_names)} modulos carregados atualmente.")

with open(file="./requirements.txt", mode="w") as arq:
    arq.write(str_modules)
