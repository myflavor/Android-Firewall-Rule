import json
import os

components = ["activities", "receivers", "services"]
data = {
    "activities": [],
    "receivers": [],
    "services": []
}
for component in components:
    path = "LibChecker-Rules/"+component + "-libs/"
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(path + file):
            with open(path + file, encoding='utf-8') as f:
                try:
                    package = file.removesuffix(".json")
                    info = json.load(f)
                    info["name"] = package
                    data[component].append(info)
                except:
                    print(end="")
result = json.dumps(data, ensure_ascii=False)
with open("LibChecker-Rules.json", 'w') as f:
    f.write(result)
    f.close()
