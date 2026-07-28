


## Difference between Python lists and Numpy arrays 

This script demonstrates the **key differences between Python Lists and NumPy Arrays**.  
Both are used to store collections of data, but they behave differently in terms of:

1.  Memory usage
2.  Data type flexibility
3.  Speed and operations
4.  Mathematical and statistical computations

Python lists are general-purpose containers, while NumPy arrays are designed for **scientific computing and numerical processing**.

By running this script, you will observe:

-   How much memory each structure uses
-   How data types are handled
-   How operations are performed differently
-   Why NumPy is widely used in data science, machine learning, and scientific programming

----------

## Libraries, Attributes, and Methods Used in the Script

### 1. NumPy Library

`NumPy` (Numerical Python) is a powerful library used for numerical computing.

Key functions used:


  

| Function / Attribute | Purpose |
| --- | --- |
| np.array() | Creates a NumPy array |
| np.arange() | Creates an array of evenly spaced values |
| np.sqrt() | Calculates square root of each element |
| np.sum() | Calculates total sum |
| np.mean() | Calculates average value |
| np.min() | Finds minimum value |
| np.max() | Finds maximum value |
| np.std() | Calculates standard deviation |
| .dtype | Shows data type of array elements |
| .nbytes | Shows memory used by the array |





### 2. sys Module

The built-in `sys` module provides system-related information.

  

| Function | Purpose |
| --- | --- |
| sys.getsizeof() | Returns memory size of an object in bytes |

### 3. Python Concepts Used

  

| Concept | Purpose |
| --- | --- |
| list(range()) | Generates list of numbers |
| List comprehension | Compact way to create lists |
| f-strings | Formatted printing |
| Loops | Iterating over elements |


### 4. Flow of Execution of the Script

The program runs in the following sequence:

Step 1 – Import required libraries  
Step 2 – Create a Python list and NumPy array  
Step 3 – Compare memory usage  
Step 4 – Demonstrate how lists and arrays handle mixed data types  
Step 5 – Perform element-wise operations  
Step 6 – Perform mathematical operations  
Step 7 – Use NumPy aggregation functions  
Step 8 – Display results


### Script

```python

# Script: Comparison of NumPy Arrays vs Python Lists
# Purpose:
# This script compares Python lists and NumPy arrays in terms of
# (1) memory usage, (2) data type behavior, (3) operations, and (4) numerical functions.

import numpy as np
import sys   # Used to measure memory size of Python objects


# ---------------------------------------------------
# 1. MEMORY EFFICIENCY COMPARISON
# ---------------------------------------------------

# Create a Python list with values from 0 to 999
python_list = list(range(1000))

# Create a NumPy array with the same values (0 to 999)
numpy_array = np.arange(1000)

# Memory used by the list container
list_memory = sys.getsizeof(python_list)  # This gives the memory size of the list object itself

# Add approximate memory of first few elements (demonstration only)
for item in python_list[:10]:
    list_memory += sys.getsizeof(item)

# Memory used by NumPy array (actual data memory)
array_memory = numpy_array.nbytes  # This gives the total bytes consumed by the array data
print("\n--- Memory Efficiency ---")
print(f"Python List memory (approx): {list_memory:,} bytes")
print(f"NumPy Array memory: {array_memory:,} bytes")
print(f"Memory saved using NumPy: {list_memory - array_memory:,} bytes")


# ---------------------------------------------------
# 2. DATA TYPE HANDLING
# ---------------------------------------------------

print("\n--- Data Type Handling ---")

# Python list can store different data types
mixed_list = [1, "hello", 3.14, True, [1, 2]]

print("Python List (mixed types):", mixed_list)
print("Types in list:", [type(x).__name__ for x in mixed_list])  # Display the type of each element in the mixed list

# NumPy converts all elements to a common data type
mixed_array = np.array([1, "hello", 3.14, True])  # This will convert all elements to strings

print("\nNumPy Array (mixed input):", mixed_array)
print("Array data type:", mixed_array.dtype)


# ---------------------------------------------------
# 3. ELEMENT-WISE OPERATIONS
# ---------------------------------------------------

print("\n--- Element-wise Operations ---")

numbers_list = [1, 2, 3, 4, 5]
numbers_array = np.array([1, 2, 3, 4, 5])

# List requires a loop or comprehension
list_doubled = [x * 2 for x in numbers_list]  # Using list comprehension to double each element in the list
print("List doubled:", list_doubled)

# NumPy performs vectorized operation
array_doubled = numbers_array * 2  # This multiplies each element in the NumPy array by 2 in a single operation
print("Array doubled:", array_doubled)


# ---------------------------------------------------
# 4. MATHEMATICAL OPERATIONS
# ---------------------------------------------------

print("\n--- Mathematical Operations ---")

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

print("Addition:", array1 + array2)  # This adds corresponding elements of the two arrays
print("Subtraction:", array2 - array1)  # This subtracts corresponding elements of array1 from array2
print("Multiplication:", array1 * array2)  # This multiplies corresponding elements of the two arrays
print("Division:", array2 / array1)  # This divides corresponding elements of array2 by array1

# NumPy mathematical function
print("Square root of array1:", np.sqrt(array1))  # This applies the square root function to each element in array1


# ---------------------------------------------------
# 5. AGGREGATION FUNCTIONS
# ---------------------------------------------------

print("\n--- Aggregation Functions ---")

data = np.array([15, 23, 8, 42, 16, 31, 27])

print("Data:", data)
print("Sum:", np.sum(data))  # This calculates the sum of all elements in the array
print("Mean:", np.mean(data))  # This calculates the mean (average) of the array elements
print("Minimum:", np.min(data))  # This finds the minimum value in the array
print("Maximum:", np.max(data))  # This finds the maximum value in the array
print("Standard Deviation:", np.std(data))  # This calculates the standard deviation of the array elements

print("\n" + "=" * 60)


```





### Explanation of the Results

After running the script, you will observe the following important conclusions:

### 1. Memory Efficiency

NumPy arrays usually use **much less memory** than Python lists because:

-   Lists store references to objects
-   NumPy stores data in a **compact continuous block of memory**

This makes NumPy ideal for **large datasets**.

----------

### 2. Data Type Behavior

Python lists can store **mixed data types**, such as:

-   integers
-   strings
-   floats
-   booleans
-   even other lists

NumPy arrays, however, convert all elements into **one common data type** to improve performance.

----------

### 3. Operations

Operations on NumPy arrays are:

-   Faster
-   Simpler
-   More readable

Example:

`array * 2`

instead of writing loops.

This is called **vectorization**.

----------

### 4. Mathematical Capabilities

NumPy provides built-in mathematical functions such as:

-   square root
-   mean
-   sum
-   standard deviation

These are extremely useful in:

-   Data Science
-   Machine Learning
-   Statistics
-   Scientific computing

----------

### Final Conclusion

Python lists are best for:

-   General programming
-   Mixed data storage

NumPy arrays are best for:

-   Numerical computation
-   Data analysis
-   Performance-critical applications















