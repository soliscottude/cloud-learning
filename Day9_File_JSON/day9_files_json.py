# Example: File and JSON handling in Python
import json

# 1️⃣ Write text data to a file
with open("study_log.txt", "w") as file:
    file.write("Scott studied Python basics today.\n")
    file.write("He learned about variables, loops, and conditions.\n")

print("✅ Text file created: study_log.txt")

# 2️⃣ Read the text file
with open("study_log.txt", "r") as file:
    content = file.read()
    print("\n📖 File content:")
    print(content)

# 3️⃣ Create a Python dictionary (like an object in JS)
data = {
    "name": "Scott",
    "day": 9,
    "topic": "File & JSON Handling",
    "hours": 4
}

# 4️⃣ Save the dictionary as a JSON file
with open("study_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("✅ JSON file created: study_data.json")

# 5️⃣ Read the JSON file back
with open("study_data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print("\n📦 Loaded data from JSON:")
    print(loaded_data)
