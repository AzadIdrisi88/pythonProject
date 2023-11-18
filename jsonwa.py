import json

# Sample JSON data
json_data = '{"name": "Alice", "age": 28, "is_student": false}'

# Loading JSON data into a Python dictionary
data = json.loads(json_data)
print(data["name"])
print(data)
print(type(json_data), type(data))
json_data = json.dumps(data)
print(type(json_data), type(data))

nested_json = '{"person": {"name": "Charlie", "age": 30}}'

# Loading and accessing nested data
data = json.loads(nested_json)
print(data)
print(data["person"])
print(data["person"]["name"])

# Writing JSON data to a file
data = {"fruit": "apple", "color": "red"}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading JSON data from a file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data["color"])

import requests
import json

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q=varanasi&appid=4a1f8a61b74546825af1e0be106e797b&units=metric")
data = response.json()
print(data)

json_data1 = '{"Name":"Laalu","gender":"male","age":40,"salary":80000}'
data1 = json.loads(json_data1)
print(data1)
print(data1["salary"])
print(type(data1), type(json_data1))

d = {"name": "Arvind", "gender": "male", "age": 25}
data = json.dumps(d)
print(data)
print(type(data), type(d))

dw = {"book": "Big magic", "game": "cricket", "Tree": "mango"}
with open("dw.json", "w") as json_file1:
    json.dump(dw,json_file1)

with open("dw.json", "r") as json_file1:
    ld = json.load(json_file1)
    print(ld["book"])

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=varanasi&appid=185a5b60b5b86a369f84a06359abb723&units=metric")
data = response.json()
print(data)
