import requests
import json


r = requests.get("https://yandex.ru")
s = {"test": 2, "test2":3}
data = json.dumps(s)
print(data)
with open("req.txt", "w") as f:
    f.write(data)