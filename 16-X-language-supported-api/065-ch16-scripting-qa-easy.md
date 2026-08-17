



## Chapter 16 — Scripting Questions
Python Libraries for Data Structures and Algorithms
These 20 scripting questions are drawn directly from the topics in Chapter 17. Full answer scripts are provided below each question and are intended for the accompanying online resource. 

Tip: For each answer script, copy the code to a .py file and run it to see the output.

## 1. Linear Search Timing

**Create a script to implement linear search on randomly generated lists of different sizes and show how time increases with `n`.**

Answer:

```python
import random
import time

# Step 1: Define linear search
# It checks every item one by one.
def linear_search(numbers, target):

    # Step 2: Compare target with every element
    for item in numbers:
        if item == target:
            return True

    # Step 3: If loop finishes, item was not found
    return False

# Step 4: Different input sizes
sizes = [1000, 10000, 100000, 500000]
times = []

# Step 5: Use a missing target
# This forces worst case:
# every item must be checked
target = -1

for n in sizes:
    # Step 6: Create list of n random numbers
    numbers = []
    for i in range(n):
        numbers.append(random.randint(1, 100000))

    # Step 7: Start timer
    start = time.perf_counter()
    linear_search(numbers, target)

    # Step 8: Stop timer
    end = time.perf_counter()
    elapsed = end - start
    times.append(elapsed)
    print("Items:", n, " Time:", elapsed)
```

#### Output
```python
Items: 1000  Time: 2.370000584051013e-05
Items: 10000  Time: 0.00032460002694278955
Items: 100000  Time: 0.0019552999874576926
Items: 500000  Time: 0.011179200024344027
```


---

## 2. Binary Search

**Create a script to perform binary search on a sorted list and count comparisons.**

Answer:

```python
# Step 1: Binary search needs sorted data
numbers = [10,20,30,40,50,60,70]

def binary_search(numbers, target):
    left = 0
    right = len(numbers)-1
    comparisons = 0

    # Step 2: Continue while search area exists
    while left <= right:
        middle = (left + right)//2
        comparisons += 1

        # Step 3: Check middle item
        if numbers[middle] == target:
            return middle, comparisons

        # Step 4: Search right half
        elif target > numbers[middle]:
            left = middle + 1

        # Step 5: Search left half
        else:
            right = middle - 1

    return -1, comparisons

index, count = binary_search(numbers, 70)
print("Index:", index)
print("Comparisons:", count)
```
#### Output
```python
Index: 6
Comparisons: 3
```
---

## 3. Bubble Sort Implementation

**Implement bubble sort and display the list after every pass.**

Answer:

```python
def bubble_sort(numbers):

    n = len(numbers)

    # Step 1:
    # Each pass places one largest item
    # at the correct position
    for pass_no in range(n-1):

        # Step 2:
        # Compare neighbouring items
        for i in range(n-pass_no-1):

            # Step 3:
            # Swap if wrong order
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = (numbers[i+1], numbers[i])

        print("After pass", pass_no+1, numbers)

numbers = [6,5,4,3,2,1]
print("Original:", numbers)
bubble_sort(numbers)
print("Sorted:", numbers)
```
#### Output
```python
Original: [6, 5, 4, 3, 2, 1]
After pass 1 [5, 4, 3, 2, 1, 6]
After pass 2 [4, 3, 2, 1, 5, 6]
After pass 3 [3, 2, 1, 4, 5, 6]
After pass 4 [2, 1, 3, 4, 5, 6]
After pass 5 [1, 2, 3, 4, 5, 6]
Sorted: [1, 2, 3, 4, 5, 6]
```
---

## 4. Insertion Sort

**Implement insertion sort by moving the current item into the correct position.**

Answer:

```python
def insertion_sort(numbers):

    # Step 1:
    # First item is already sorted
    for key_index in range(1,len(numbers)):

        # Step 2:
        # Store current item
        key = numbers[key_index]
        position = key_index - 1

        # Step 3:
        # Shift bigger items right
        while position >= 0 and numbers[position] > key:
            numbers[position+1] = numbers[position]
            position -= 1

        # Step 4:
        # Insert key at empty position
        numbers[position+1] = key

numbers=[5,4,2,3]
print(numbers)
insertion_sort(numbers)
print(numbers)
```
#### Output
```python
[5, 4, 2, 3]
[2, 3, 4, 5]
```
---

## 5. Selection Sort

**Create a selection sort script which finds the smallest item and places it at the beginning.**

Answer:

```python
def selection_sort(numbers):
    n = len(numbers)

    # Step 1:
    # Each pass fixes one position
    for position in range(n-1):
        # Assume current position
        # contains smallest value
        min_index = position

        # Step 2:
        # Search remaining list
        for i in range(position+1,n):
            if numbers[i] < numbers[min_index]:
                min_index = i

        # Step 3:
        # Exchange only if needed
        if min_index != position:

            numbers[position], numbers[min_index] = (
                numbers[min_index],
                numbers[position]
            )

numbers=[7,1,4,2,0]
selection_sort(numbers)
print(numbers)
```

#### Output
```python
[0, 1, 2, 4, 7]
```
---

## 6. Stack using List

**Implement stack operations using a Python list.**

Answer:

```python
# Step 1:
# List works naturally as stack
# because append and pop work at the end
stack=[]

# Step 2:
# PUSH operation
stack.append("Book 1")
stack.append("Book 2")
stack.append("Book 3")
print(stack)

# Step 3:
# POP removes latest item
item = stack.pop()
print("Removed:", item)
print(stack)
```
#### Output
```python
['Book 1', 'Book 2', 'Book 3']
Removed: Book 3
['Book 1', 'Book 2']
```
---

## 7. Queue using deque

**Create a queue using `collections.deque` and process items in FIFO order.**

Answer:

```python
from collections import deque

# Step 1:
# deque supports fast operations
# from both ends
queue = deque()

# Step 2:
# Add items
queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

# Step 3:
# Remove oldest item
while queue:
    print(queue.popleft())
```

#### Output
```python
Task 1
Task 2
Task 3
```
---

## 8. Counter

**Count frequency of words using `Counter`.**

Answer:

```python
from collections import Counter

# Step 1:
# Data to analyse
words=["python", "java", "python", "python", "java"]

# Step 2:
# Counter automatically counts
count = Counter(words)
print(count)

# Step 3:
# Most common item
print(count.most_common(1))
```

#### Output
```python
Counter({'python': 3, 'java': 2})
[('python', 3)]
```
---

## 9. defaultdict

**Group students by subject using `defaultdict`.**

Answer:

```python
from collections import defaultdict

# Step 1:
# Automatically create empty list
students = defaultdict(list)

# Step 2:
# Add values
students["Python"].append("Amit")
students["Python"].append("Riya")
students["Math"].append("John")
print(students)
```

#### Output
```python
defaultdict(<class 'list'>, {'Python': ['Amit', 'Riya'], 'Math': ['John']})
```
---

## 10. namedtuple

**Create a record using `namedtuple` instead of normal tuple indexing.**

Answer:

```python
from collections import namedtuple

# Step 1:
# Create a record structure
Student = namedtuple("Student", ["name","age"])

# Step 2:
# Create object
s1 = Student("Anita", 20)

# Step 3:
# Access using names
print(s1.name)
print(s1.age)
```

#### Output
```python
Anita
20
```
---

## 11. `ChainMap`: 
**Combine user settings with default settings: Create a configuration system where user settings override default settings using `ChainMap`.**

Answer:

```python
from collections import ChainMap

# Step 1: Create default settings
# These values are used when the user has not provided a value
default_settings = {"theme": "light", "font_size": 12, "language": "English"}

# Step 2: Create user-specific settings
# User settings should get higher priority
user_settings = {"theme": "dark"}

# Step 3: Combine dictionaries using ChainMap
# ChainMap searches the first dictionary first
# If key is not found, it checks the next dictionary
settings = ChainMap(user_settings, default_settings)

# Step 4: Access values
print("Theme:", settings["theme"])
# Found in user_settings
print("Font size:", settings["font_size"])
# Not present in user_settings
# So value comes from default_settings
print("Language:", settings["language"])
```

#### Output
```python
Theme: dark
Font size: 12
Language: English
```
---

# **12. `heapq`: Process tasks according to priority**

**Question 12. Use `heapq` to create a priority based task manager.**

Answer:

```python
import heapq

# Step 1: Create an empty heap
# heapq always keeps the smallest item at the top
tasks = []

# Step 2: Add tasks
# Tuple format:
# (priority, task_name)
# Smaller priority number means higher importance
heapq.heappush(tasks, (3, "Read book"))
heapq.heappush(tasks, (1, "Fix error"))
heapq.heappush(tasks, (2, "Reply email"))

# Step 3: Remove tasks in priority order
while tasks:

    # heappop removes the smallest priority item
    priority, task = heapq.heappop(tasks)

    print(f"Priority {priority}: {task}")
```

#### Output
```python
Priority 1: Fix error
Priority 2: Reply email
Priority 3: Read book
```
---

# **13. `bisect`: Insert item into sorted list**

**Question 13. Maintain a sorted list by inserting a new value using `bisect`.**

Answer:

```python
import bisect

# Step 1:
# List must already be sorted
marks = [40, 55, 70, 85, 95]
new_mark = 75

# Step 2:
# Find correct insertion position
position = bisect.bisect_left(marks, new_mark)

# Step 3:
# Insert while keeping list sorted
bisect.insort(marks, new_mark)
print("Inserted at index:", position)
print("Updated marks:", marks)
```

#### Output
```python
Inserted at index: 3
Updated marks: [40, 55, 70, 75, 85, 95]
```
---

# **14. `queue.Queue`: First In First Out processing**

**Question 14. Simulate a customer service queue using `Queue`.**

Answer:

```python
import queue

# Step 1:
# Create FIFO queue
# First customer entering is served first
customers = queue.Queue()

# Step 2:
# Add customers
customers.put("Customer A")
customers.put("Customer B")
customers.put("Customer C")

# Step 3:
# Remove customers in order
while not customers.empty():
    customer = customers.get()

    print("Serving:", customer)
```

#### Output
```python
Serving: Customer A
Serving: Customer B
Serving: Customer C
```

---

# **15. `LifoQueue`: Undo operation**

**Question 15. Implement a simple undo system using `LifoQueue`.**

Answer:

```python
import queue

# Step 1:
# LifoQueue works like a stack
# Last inserted item comes out first
history = queue.LifoQueue()

# Step 2:
# Store actions
history.put("Typed Hello")
history.put("Added Python")
history.put("Deleted Python")

# Step 3:
# Undo removes most recent action
while not history.empty():
    action = history.get()
    print("Undo:", action)
```

#### Output
```python
Undo: Deleted Python
Undo: Added Python
Undo: Typed Hello
```
---

# **16. `PriorityQueue`: Hospital emergency queue**

**Question 16. Create an emergency queue where patients are served by priority.**

Answer:

```python
import queue

# Step 1:
# Create PriorityQueue
patients = queue.PriorityQueue()

# Step 2:
# Add patients
# Lower number = higher priority

patients.put((1, "Critical patient"))

patients.put((3, "Normal patient"))

patients.put((2, "Urgent patient"))

# Step 3:
# Serve according to priority
while not patients.empty():
    priority, patient = patients.get()
    print(priority, patient)
```

#### Output
```python
1 Critical patient
2 Urgent patient
3 Normal patient
```
---

# **17. `Enum`: Represent fixed choices**

**Question 17. Use `Enum` to represent HTTP status codes.**

Answer:

```python
from enum import Enum

# Step 1:
# Create meaningful names
# instead of using random numbers

class Status(Enum):
    SUCCESS = 200
    NOT_FOUND = 404
    ERROR = 500

# Step 2:
# Function receives enum value
def show_status(status):
    if status == Status.SUCCESS:
        print("Request successful")

    elif status == Status.NOT_FOUND:
        print("Page missing")

    else:
        print("Server error")

# Step 3:
show_status(Status.NOT_FOUND)
```

#### Output
```python
Page missing
```
---

# **18. `dataclass`: Store structured data**

**Question 18. Create a `dataclass` for storing student information.**

Answer:

```python
from dataclasses import dataclass

# Step 1:
# dataclass automatically creates:
# __init__, __repr__, comparison methods etc.

@dataclass
class Student:
    name: str
    marks: int
    passed: bool = True

# Step 2:
# Create objects easily

s1 = Student("Alice", 85)
s2 = Student("Bob", 40, False)

# Step 3:
# Print objects
print(s1)
print(s2)
```

#### Output
```python
Student(name='Alice', marks=85, passed=True)
Student(name='Bob', marks=40, passed=False)
```
---

# **19. `lru_cache`: Avoid repeated calculations**

**Question 19. Use `lru_cache` to cache expensive function results.**

Answer:

```python
from functools import lru_cache
import time

# Step 1:
# Cache stores previous results
@lru_cache(maxsize=None)
def calculate_square(number):
    print("Calculating...")
    # Simulate slow operation
    time.sleep(1)
    return number * number

# Step 2:
# First call calculates
print(calculate_square(10))

# Step 3:
# Second call uses stored result
print(calculate_square(10))
```

#### Output
```python
Calculating...
100
100
```
---

# **20. `partial` + `itertools` + `json/pickle`**

**Question 20. Demonstrate function customization, sequence processing and object storage.**

Answer:

```python
from functools import partial
from itertools import chain
import json
import pickle

# PART 1: partial()
def display(message, level):
    print(level, message)

# Fix one argument permanently
error_message = partial(display, level="ERROR")
error_message("File missing")

# PART 2: itertools.chain
numbers = [
    [1,2],
    [3,4]
]

# Combine multiple lists
for item in chain.from_iterable(numbers):
    print(item)

# PART 3: json
data = {"name": "Alice", "marks": 90}
# Convert Python object to JSON string
json_text = json.dumps(data)
print(json_text)

# PART 4: pickle
# Save Python object in binary format

with open("student.pkl", "wb") as file:
    pickle.dump(data, file)

print("Object saved")
```


#### Output
```python
ERROR File missing
1
2
3
4
{"name": "Alice", "marks": 90}
Object saved
```

---
