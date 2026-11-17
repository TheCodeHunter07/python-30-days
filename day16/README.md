# Day 16 – File Handling

## 📚 Topics Covered

- Opening files safely using `with`.
- Understanding file modes:
  - `r` – Read
  - `w` – Write
  - `a` – Append
- Reading files line by line.
- Writing and reading CSV files using the `csv` module.
- Working with JSON data using the `json` module.
- Saving and loading structured data.

## 📝 Assignments

### 1. Diary – diary.py

Created a simple diary application that:

- Accepts daily diary entries.
- Adds dates to entries.
- Appends new entries to a text file.
- Reads and displays previously saved entries.

### 2. CSV Report – csv_report.py

Created a student report application using Python's `csv` module.

Features:
- Writes 10 students and their marks into a CSV file.
- Reads student records from the CSV file.
- Calculates and displays average marks.

### 3. Settings – settings.py

Created a program using Python's `json` module.

Features:
- Stores application settings in a Python dictionary.
- Saves dictionary data into a JSON file.
- Loads JSON data back into Python.

### 4. Stretch Assignment – phonebook_json.py

Upgraded the Day 9 phonebook application to support JSON file storage.

Features:
- Saves contact information into a JSON file.
- Loads previously saved contacts.
- Maintains contact information between program executions.

## 🎯 Learning Outcomes

- Learned how to read, write, and append files.
- Understood safe file handling using context managers.
- Practiced working with CSV files.
- Learned how to serialize and deserialize data using JSON.
- Built applications that store and retrieve data permanently.