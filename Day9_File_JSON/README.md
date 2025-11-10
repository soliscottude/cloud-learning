# Day 9 – File and JSON Handling in Python

## 🎯 Goals
- Learn how to read and write files in Python.
- Understand JSON data structure and how to save/load it.
- Build the foundation for AWS boto3 automation.

---

## 🧠 What I Learned
### 1️⃣ File Handling (`open()`, `read()`, `write()`)
- Created a text file `study_log.txt` and wrote log entries using `with open(..., "w")`.
- Read the file contents using `read()` and printed them to the console.
- Learned why `with open()` is safer than manual `close()`.

### 2️⃣ JSON Handling (`json.dump()`, `json.load()`)
- Created a Python dictionary `data` and exported it to `study_data.json`.
- Loaded the JSON file back into Python as a dictionary for further use.
- Understood the difference between the file name and the file object (e.g. `f`).

---

## 🧪 Sample Output

```
✅ Text file created: study_log.txt

📖 File content:
Scott studied Python basics today.
He learned about variables, loops, and conditions.

✅ JSON file created: study_data.json

📦 Loaded data from JSON:
{'name': 'Scott', 'day': 9, 'topic': 'File & JSON Handling', 'hours': 4}
```