import json

#1 Read JSON file
with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Read from JSON:", data)

#2 Convert Python to JSON string
python_dict = {
    "course": "Python",
    "topic": "Advanced",
    "year": 2026
}

json_string = json.dumps(python_dict, indent=4)
print("\nConverted to JSON string:")
print(json_string)

#3 Write JSON file
with open("new-data.json", "w") as file:
    json.dump(python_dict, file, indent=4)

print("\nNew JSON file created.")