import json
import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"views": 1000, "likes": 100, "name": "ariful"},
#         {"views": 1100, "likes": 101, "name": "SMN"},
#         {"views": 1200, "likes": 102, "name": "Sumon"}]

# for i in range(len(data)):
#     response = requests.put(
#         BASE + "video/"+str(i), headers={'Content-Type': 'application/json'}, data=json.dumps(data[i]))
#     print(response.json())

# response = requests.delete(BASE + "video/2")
# input()
response = requests.get(BASE + "video/1")
print(response.json())
