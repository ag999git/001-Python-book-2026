


# PROJECT: Golden Rules of Vectorization in NumPy

## Objective: The goal of this project is to:

-   Understand the concept of **vectorization in NumPy**
-   Compare **loop-based vs vectorized approaches**
-   Learn and apply the **Golden Rules of Vectorization**
-   Analyze **performance, readability, and memory efficiency**
-   Write clean, efficient NumPy code

----------

## PART A — THEORY TASK (Research-Based)

### Task Instructions

Write a detailed note covering:

### 1. What is Vectorization?

-   Definition
-   Why it is important in NumPy
-   Difference from traditional Python loops

----------

### 2. The Golden Rules of Vectorization

Explain each of the following in detail:

1.  Avoid loops for numerical operations
2.  Avoid `np.append()` in loops
3.  Use Boolean masking instead of `if/else`
4.  Use NumPy ufuncs instead of Python `math` functions

For each rule, include:

-   Explanation
-   Example
-   Why the wrong approach is inefficient

----------

### 3. Performance Analysis

-   Why vectorization is faster
-   Role of C-level execution
-   Memory efficiency (no repeated copying)

----------

### 4. Comparison Table

Create a table comparing:

-   Loop-based approach
-   Vectorized approach

----------

### 5. Real-World Applications

Explain where vectorization is used:

-   Machine Learning
-   Data Analysis
-   Image Processing

----------

## PART B — SCRIPT TASK (Implementation)

## Task Instructions

Write a Python script that:

1.  Demonstrates each golden rule
2.  Shows:
    -   Wrong approach
    -   Correct approach
3.  Measures execution time
4.  Displays results clearly
5.  Includes **detailed comments**

----------

# ANSWER — THEORY

### 1. What is Vectorization?

Vectorization is the process of performing operations on entire arrays at once instead of using loops.
### Example:

```python

# Loop approach
result = []
for i in range(len(arr)):
    result.append(arr[i] * 2)

# Vectorized approach
result = arr * 2

```

## 2. Golden Rules Explained

### Rule 1: Avoid Loops

```python
# Dont do Loop:
for i in range(len(a)):
    c[i] = a[i] + b[i]

# Vectorized:
c = a + b

# Reason: Python loops are slow
```

### Rule 2: Avoid np.append()

```python

# Wrong:

arr = np.array([])
for i in range(1000):
    arr = np.append(arr, i)

#Problem: Creates new array every time → O(n²)

# Correct:

temp = []
for i in range(1000):
    temp.append(i)

arr = np.array(temp)

```

### Rule 3: Boolean Masking

```python

# Wrong:

result = []
for x in arr:
    if x > 10:
        result.append(x)

# Correct:

result = arr[arr > 10]
```

### Rule 4: Use Ufuncs

```python

# Wrong:

import math
[math.sqrt(x) for x in arr]

# Correct:

np.sqrt(arr)

```

## 3. Why Vectorization is Faster

  

| Reason | Explanation |
| --- | --- |
| C-level execution | NumPy runs in optimized C code |
| No Python loops | Avoid interpreter overhead |
| Memory efficiency | No repeated allocations |
| SIMD optimization | CPU-level parallelism |


## 4. Comparison Table


| Aspect | Loop Approach | Vectorized Approach |
| --- | --- | --- |
| Speed | Slow | Fast |
| Readability | Low | High |
| Memory | Inefficient | Efficient |
| Code Length | Long | Short |


## Script (Showing the rules)

```python
# SCRIPT: Golden Rules of Vectorization

import numpy as np
import time
import math

# RULE 1: AVOID LOOPS FOR ELEMENT-WISE OPERATIONS

a = np.arange(1000000)  # Creates an array with 1 million elements: [0, 1, 2, ..., 999999]
b = np.arange(1000000)  # Creates another array with 1 million elements: [0, 1, 2, ..., 999999]

# Don't Loop
start = time.time()  # Start the timer
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
print("Loop Time:", time.time() - start)  
# Output: Loop Time: 0.1 seconds (varies based on machine)

# Do Vectorize
start = time.time()
result = a + b
print("Vectorized Time:", time.time() - start)  
# Output: Vectorized Time: 0.001 seconds (varies based on machine)

# RULE 2: AVOID np.append IN LOOPS

# Dont do this (Bad)
start = time.time()
arr = np.array([])
for i in range(5000):  # This will create a new array every time, which is inefficient
    arr = np.append(arr, i)
print("np.append Time:", time.time() - start)
# Output: np.append Time: 0.5 seconds (varies based on machine)

# Do this (Good)
start = time.time()
temp = []
for i in range(5000):  # This will create a new list element every time, which is efficient
    temp.append(i)
arr = np.array(temp)
print("List Conversion Time:", time.time() - start)
# Output: List Conversion Time: 0.001 seconds (varies based on machine)

# RULE 3: BOOLEAN MASKING

data = np.array([5, 15, 25, 10, 30])  # Creates an array with 5 elements: [5, 15, 25, 10, 30]

# Don't Loop
start = time.time()
result = []
for x in data:  # Loop through each element in the array
    if x > 15:
        result.append(x)
print("Loop Result:", result)
# Output: Loop Result: [25, 30]
print("Loop Time:", time.time() - start)
# Output: Loop Time: 0.0001 seconds (varies based on machine)

# Do Vectorize
start = time.time()
result = data[data > 15]  # Creates a boolean mask where the condition is True and returns the corresponding elements
print("Masked Result:", result)
print("Vectorized Time:", time.time() - start)
# Output: Vectorized Time: 0.00001 seconds (varies based on machine)

# RULE 4: USE UFUNCS

data = np.array([1,4,9,16])

# Don't Loop
start = time.time()
result = []
for x in data:
    result.append(math.sqrt(x))  # math.sqrt is not vectorized, so it operates on each element individually
print("math.sqrt:", result)
# Output: math.sqrt: [1.0, 2.0, 3.0, 4.0]
print("Loop Time:", time.time() - start)
# Output: Loop Time: 0.0001 seconds (varies based on machine)

# Error example
# math.sqrt(data)  # TypeError

# Do Vectorize
start = time.time()
result = np.sqrt(data)
print("np.sqrt:", result)
# Output: np.sqrt: [1. 2. 3. 4.]
print("Vectorized Time:", time.time() - start)
# Output: Vectorized Time: 0.00001 seconds (varies based on machine)

```

### RULE 2: Why `np.append()` in a loop is BAD
First Understand What You Think is Happening

When you write:

```python

arr = np.array([])
for i in range(5):
    arr = np.append(arr, i)
```

You might think: “I am just adding one element to the same array”

What is Actually Happening Internally

NumPy arrays are fixed-size (like a fixed container).

So every time you do:

`arr = np.append(arr, i)`

NumPy does this:

Step 1: Create a NEW array of bigger size
Step 2: Copy ALL old elements into it
Step 3: Add new element
Step 4: Delete old array

Step-by-Step Example

Let’s simulate:

```python

Iteration 1:
[] → [0]
Iteration 2:
[0] → create new array → [0,1]
Iteration 3:
[0,1] → create new array → [0,1,2]
Iteration 4:
[0,1,2] → create new array → [0,1,2,3]
Each time → copy entire array again
Total work becomes:
1 + 2 + 3 + ... + n  → O(n²)
```


### Why Python List is Better

Python lists are dynamic (resizable).

`temp = []`
`temp.append(i)`

**What happens:**

>List has extra space reserved
>No copying every time
>Occasional resizing only

### So complexity is: O(n) instead of O(n²)

**Correct Approach Flow**

```python

temp = []          # Fast growing structure
for i in range(5000):
    temp.append(i)

arr = np.array(temp)   # Convert once
```

### Key Idea
-    NumPy arrays = fixed size → expensive to grow
-    Lists = flexible → cheap to grow


  


### RULE 3: Boolean Masking (Most Important Concept)
What You Are Doing in Loop

```python

result = []
for x in data:
    if x > 15:
        result.append(x)

```
#### You are doing 2 things:

-    Check condition
-    Select elements

NumPy does Both at once
data[data > 15]

Let’s break this into steps.

```python
# Step 1: Create Boolean Mask
data = np.array([5, 15, 25, 10, 30])

mask = data > 15

# Result: mask = [False, False, True, False, True]
# This is called a Boolean mask

# Step 2: Use Mask to Filter Data
data[mask]

# Result: [25, 30] because 5, 15 and 10 get removed because of False
# Combine Both Steps
data[data > 15]

# Same as:

mask = data > 15
result = data[mask]
```

### Why this is powerful  

| Loop Version | NumPy Version |
| --- | --- |
| Check each element manually | Done internally |
| Append manually | Done automatically |
| Python execution | C-level execution |


Visual Explanation

```python

data:   [ 5   15   25   10   30 ]
mask:   [ F    F    T    F    T ]

Result → pick only where mask = True

Final:  [25, 30]
```

**Why Boolean Masking is Faster**

Because:
-    No Python loop
-    No repeated append
-    Entire operation runs in optimized C code


### Additional possibility with mask: Modify Data Using Mask
`data[data > 15] = 100`

Result:

`[5, 15, 100, 10, 100]`

This is very powerful and not possible easily with loops


### Final Comparison
  

| Concept | Loop Approach | NumPy Approach |
| --- | --- | --- |
| Building array | append repeatedly | build list → convert |
| Filtering | if condition inside loop | boolean mask |
| Speed | slow | very fast |
| Code | long | short |


















