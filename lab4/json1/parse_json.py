import json
import os

# Получаем текущую директорию
current_dir = os.path.dirname(os.path.abspath(__file__))

# Формируем полный путь к файлу JSON
file_path = os.path.join(current_dir, 'sample-data.json')

with open(file_path, 'r') as file:
    data = json.load(file)

array = []

for item in data['imdata']:
    if "l1PhysIf" in item:
        array.append(item["l1PhysIf"])

for i in range(3):
    print(
        array[i]["attributes"]["dn"], 
        array[i]["attributes"]["speed"], 
        array[i]["attributes"]["mtu"]
)