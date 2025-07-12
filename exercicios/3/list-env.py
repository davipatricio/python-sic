import os
import json

env = os.environ
kv = {}

for key in env:
    kv[key] = env[key]

with open(file="current-env.json", mode="w") as file:
    # file.write(str(kv))
    file.write(json.dumps(kv, indent=2))