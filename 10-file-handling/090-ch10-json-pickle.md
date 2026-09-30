# Comparative Study of JSON and Pickle for Data Serialization in Python with Real-World Applications

### RESEARCH / PROJECT QUESTION

### Title: “Comparative Study of JSON and Pickle for Data Serialization in Python with Real-World Applications”

### Problem Statement

Develop a Python system to:

1. Serialize and deserialize data using:
   * JSON
   * Pickle
2. Compare:
   * Performance
   * Security
   * Portability
3. Demonstrate:
   * API-style JSON usage
   * Limitations of JSON
   * Risks of Pickle

***

### Objectives

#### A. Functional Tasks

* Store and retrieve:
  * Dictionary
  * List
  * Custom class

***

#### B. API Simulation

* Convert data → JSON string
* Simulate sending/receiving data

***

#### C. Error Handling

* Handle:
  * Invalid JSON
  * Unsupported data types

***

#### D. Security Study

* Show why Pickle is unsafe
* Show safe JSON usage

***

### ANSWER (CONCEPTUAL)

#### Key Findings

* JSON:
  * Portable, safe, widely used
* Pickle:
  * Powerful but unsafe
* APIs use JSON because:
  * Language-independent
  * Text-based

### Comparison Table

| Feature        | JSON    | Pickle | Use Case         |
| -------------- | ------- | ------ | ---------------- |
| Portability    | High    | Low    | APIs             |
| Security       | High    | Low    | Web              |
| Object Support | Limited | Full   | Python apps      |
| Speed          | Medium  | High   | Internal storage |

#### Final Insight

> Use **JSON** for:

* APIs
* Web
* Data exchange

> Use **Pickle** for:

* Python-only programs
* Complex object storage

### Script

```python

# PROJECT: JSON vs Pickle Comparison Study

import json
import pickle

# STEP 1: Define class. Custom class to demonstrate JSON and Pickle handling of complex objects
class Student:
    def __init__(self, name, marks):
        self.name = name  # Student's name
        self.marks = marks  # Student's marks

# STEP 2: Create data. A simple dictionary to be serialized using both JSON and Pickle
data = {
    "name": "Alice",  # Student's name
    "marks": 60  # Student's marks
}

# STEP 3: JSON serialization
json_str = json.dumps(data)  # Convert Python dict to JSON string
print("JSON String:", json_str)  # Output: JSON String: {"name": "Alice", "marks": 60}

# STEP 4: JSON deserialization
json_obj = json.loads(json_str)  # Convert JSON string back to Python dict
print("JSON Object:", json_obj)  # Output: JSON Object: {'name': 'Alice', 'marks': 60}

# STEP 5: Pickle serialization - writing to file
with open("data.pkl", "wb") as f:  # Open file in binary write mode
    pickle.dump(data, f)  # Serialize Python dict to binary format and write to file

# STEP 6: Pickle deserialization - reading from file
with open("data.pkl", "rb") as f:  # Open file in binary read mode
    pkl_obj = pickle.load(f)  # Deserialize binary data back to Python dict

print("Pickle Object:", pkl_obj)  # Output: Pickle Object: {'name': 'Alice', 'marks': 60}

# STEP 7: JSON limitation
student = Student("Alice", 60)  # Create an instance of Student class

# STEP 8: ERROR: JSON cannot serialize custom Python objects
# json.dumps(student)  # TypeError: Object of type Student is not JSON serializable

# Solution: Convert to dict
json_str = json.dumps(student.__dict__)
print("Converted Object:", json_str)  # Output: Converted Object: {"name": "Alice", "marks": 60}

# STEP 9: Pickle can handle custom objects
with open("student.pkl", "wb") as f:  # Open file in binary write mode
    pickle.dump(student, f)  # Serialize custom object to binary format and write to file
with open("student.pkl", "rb") as f:  # Open file in binary read mode
    loaded_student = pickle.load(f)  # Deserialize binary data back to custom object
print("Loaded Student:", loaded_student.name, loaded_student.marks) # Output: Loaded Student: Alice 60

# STEP 10: Security warning
# NEVER do this with unknown files
# pickle.load(open("unknown.pkl", "rb"))  # This can execute arbitrary code if the file is malicious. Always ensure you trust the source of the pickle file before loading it.


```

#### Flowchart

The following diagram shows the flow of execution in JSON vs pickling

![Flowchart](../resources/S10-LR-ch10-files-json-pickle.png)

**Reading the figure**

- **Step 1:** The script creates a dictionary `data` and an object of the custom class `Student`.
- **Step 2:** JSON serialization: `json.dumps(data)` turns the dictionary into a JSON string.
- **Step 3:** JSON deserialization: `json.loads()` turns the string back into a dictionary.
- **Step 4:** Pickle serialization: `pickle.dump(data, f)` writes the dictionary to `data.pkl` in binary form.
- **Step 5:** Pickle deserialization: `pickle.load(f)` reads it back as a dictionary.
- **Step 6:** Comparing the two: JSON cannot store the `Student` object directly (it needs `student.__dict__`), while pickle stores and reloads the object itself, but must never be used on untrusted files.
