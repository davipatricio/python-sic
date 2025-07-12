import os
import json

with open(file="./current-env.json", mode="w") as file:
  file.write(json.dumps(dict(os.environ), indent=2))
  # ou se for apenas os nomes:
  # file.write(list(dict(os.environ).keys()), indent=2))
