



# Chapter 11 — Python Lists vs. NumPy Arrays

## About this chapter

Once you're comfortable storing data in a Python `list`, the natural next
question is: *is a list always the right tool?* This chapter answers that
question by introducing **NumPy arrays** — the data structure almost every
data-science, machine-learning, and scientific-computing library in Python
is built on top of — and comparing them directly against the plain list you
already know.

The comparison is organised around four practical questions a beginner
should be able to answer after working through this page:

1. Which one uses **less memory**, and why does that matter?
2. What happens when you put **different types of data** (numbers, text,
   `True`/`False`) into each one?
3. How do **calculations** (like doubling every number) differ between the
   two?
4. What extra **maths and statistics tools** does NumPy give you that a
   plain list doesn't?

A single runnable script demonstrates all four points. The explanation
after it walks through *why* the results come out the way they do.
The explaination is initially in plain language followed by technical terms explained briefly and linked for
anyone who wants to go deeper.

> **Quick glossary, before we start**
> - **Library** — a collection of ready-made code someone else wrote, that
>   you can `import` and reuse instead of writing everything yourself. See
>   [Python's own explanation of modules](https://docs.python.org/3/tutorial/modules.html).
> - **Array** — in NumPy, a grid of values, all of the *same type*, stored
>   very compactly. See the [official NumPy array basics guide](https://numpy.org/doc/stable/user/absolute_beginners.html).
> - **Vectorization** — doing an operation on *every* value in a collection
>   at once (like `array * 2`), instead of writing a loop. Explained further
>   below.

---

## Why compare lists and arrays at all?

A Python `list` is wonderfully flexible: you can mix numbers, text, and
even other lists inside it, and resize it freely. But that flexibility has
a cost — Python has to keep extra bookkeeping information for every single
item, since it has no way of knowing in advance what type each item will
be.

A **NumPy array** trades away some of that flexibility for **speed and
compactness**. Every item in a NumPy array must be the same type (all
integers, all decimals, and so on), which lets NumPy store the data in one
tightly packed block of memory and perform calculations on the whole block
at once, instead of one item at a time.

Neither one is "better" in every situation — they're suited to different
jobs, which is exactly what this chapter's script demonstrates.

![Flowchart](/resources/ch-11-numpy-august-2026-numpy-array-vs-list.png)

---

## Libraries, attributes, and methods used in the script

### 1. The NumPy library

`NumPy` (short for **Num**erical **Py**thon) is a library — meaning code
that's already been written for you — built specifically for fast,
large-scale numerical calculations. It's not part of "plain" Python; it's
installed separately (`pip install numpy`) and then brought into a script
with `import numpy as np`. ([Official NumPy documentation](https://numpy.org/doc/stable/))

| Function / attribute | What it does, in plain words |
| --- | --- |
| `np.array()` | Turns a normal Python list into a NumPy array |
| `np.arange()` | Creates an array counting up in equal steps (like a numeric `range()`) |
| `np.sqrt()` | Works out the square root of every number in the array, all at once |
| `np.sum()` | Adds up every value in the array |
| `np.mean()` | Works out the average of the values |
| `np.min()` | Finds the smallest value |
| `np.max()` | Finds the largest value |
| `np.std()` | Works out the **standard deviation** — a measure of how spread out the values are. ([Plain-language explanation of standard deviation](https://www.mathsisfun.com/data/standard-deviation.html)) |
| `.dtype` | Tells you what type of data the array holds (e.g. whole numbers, decimals, text) |
| `.nbytes` | Tells you exactly how many bytes of memory the array's data occupies |

### 2. The `sys` module

`sys` is part of Python's own **standard library** — meaning it comes
built in, with nothing extra to install. Here it's used purely to measure
memory. ([Official `sys` module docs](https://docs.python.org/3/library/sys.html))

| Function | What it does |
| --- | --- |
| `sys.getsizeof()` | Reports how many bytes of memory a given Python object takes up |

### 3. Everyday Python tools used alongside NumPy

| Concept | What it's for | Learn more |
| --- | --- | --- |
| `list(range(...))` | Quickly builds a list of numbers | [`range()` docs](https://docs.python.org/3/library/stdtypes.html#range) |
| List comprehension | A short, one-line way to build a new list from an existing one | [List comprehensions tutorial](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) |
| f-strings | A convenient way to insert values into printed text | [f-string docs](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) |
| Loops (`for`) | Repeating an action once for every item in a collection | [`for` loop tutorial](https://docs.python.org/3/tutorial/controlflow.html#for-statements) |

### 4. How the script runs, step by step

| Step | What happens |
| --- | --- |
| 1 | Import the libraries the script needs (`numpy`, `sys`) |
| 2 | Create one Python list and one NumPy array holding the same numbers |
| 3 | Compare how much memory each one uses |
| 4 | Put mixed data types into a list, and into an array, and see the difference |
| 5 | Double every number — once the "list way," once the "array way" |
| 6 | Perform basic maths (`+ − × ÷`) directly on two arrays |
| 7 | Use NumPy's built-in statistics functions on an array |
| 8 | Print everything so the results can be compared side by side |

---

## The script

Every major section below is labelled with a `# Step N —` comment that
matches the step table above, so you can follow along without losing your
place.

```python
# Script: Comparison of NumPy Arrays vs Python Lists
# Purpose:
# This script compares Python lists and NumPy arrays in terms of
# (1) memory usage, (2) data type behavior, (3) operations, and (4) numerical functions.

# Step 1 - Import the libraries this script needs.
import numpy as np   # NumPy: fast numerical arrays
import sys            # sys: lets us measure how much memory an object uses


# ---------------------------------------------------
# Step 2 & 3 - Create a list and an array, then compare their memory use
# ---------------------------------------------------

# Create a Python list with values from 0 to 999
python_list = list(range(1000))

# Create a NumPy array holding the same values (0 to 999)
numpy_array = np.arange(1000)

# sys.getsizeof() gives the memory used by the LIST CONTAINER itself
# (not the individual numbers inside it — Python lists store items as
# separate objects elsewhere in memory, referenced from the list).
list_memory = sys.getsizeof(python_list)

# To make the comparison a little fairer, add the approximate memory used
# by a handful of the individual number objects too (just the first 10,
# purely as a demonstration — a full count would need every item).
for item in python_list[:10]:
    list_memory += sys.getsizeof(item)

# For a NumPy array, .nbytes directly reports the memory used by the
# actual numeric data, since NumPy stores it all in one compact block.
array_memory = numpy_array.nbytes

print("\n--- Memory Efficiency ---")
print(f"Python List memory (approx): {list_memory:,} bytes")
print(f"NumPy Array memory: {array_memory:,} bytes")
print(f"Memory saved using NumPy: {list_memory - array_memory:,} bytes")


# ---------------------------------------------------
# Step 4 - See how each structure handles MIXED data types
# ---------------------------------------------------

print("\n--- Data Type Handling ---")

# A Python list is happy to hold several different types side by side.
mixed_list = [1, "hello", 3.14, True, [1, 2]]

print("Python List (mixed types):", mixed_list)
# Show the type of each item, one by one, using a list comprehension
print("Types in list:", [type(x).__name__ for x in mixed_list])

# A NumPy array insists that every element share ONE common type.
# Since a text string is included here, NumPy converts everything
# (including the numbers) into strings so they can all match.
mixed_array = np.array([1, "hello", 3.14, True])

print("\nNumPy Array (mixed input):", mixed_array)
print("Array data type:", mixed_array.dtype)


# ---------------------------------------------------
# Step 5 - Double every number: the "list way" vs the "array way"
# ---------------------------------------------------

print("\n--- Element-wise Operations ---")

numbers_list = [1, 2, 3, 4, 5]
numbers_array = np.array([1, 2, 3, 4, 5])

# A plain list has no built-in idea of "multiply every item" — you must
# process the items one at a time, typically with a list comprehension.
list_doubled = [x * 2 for x in numbers_list]
print("List doubled:", list_doubled)

# A NumPy array lets you apply the operation to the WHOLE array in one go.
# This shortcut is called "vectorization" — see the glossary note above.
array_doubled = numbers_array * 2
print("Array doubled:", array_doubled)


# ---------------------------------------------------
# Step 6 - Basic maths directly on two arrays
# ---------------------------------------------------

print("\n--- Mathematical Operations ---")

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

# Each of these lines works on EVERY matching pair of numbers at once —
# there is no loop anywhere in this section.
print("Addition:", array1 + array2)          # adds matching elements together
print("Subtraction:", array2 - array1)       # subtracts matching elements
print("Multiplication:", array1 * array2)    # multiplies matching elements
print("Division:", array2 / array1)          # divides matching elements

# NumPy also provides ready-made mathematical functions, such as square root
print("Square root of array1:", np.sqrt(array1))


# ---------------------------------------------------
# Step 7 - Built-in statistics functions
# ---------------------------------------------------

print("\n--- Aggregation Functions ---")

data = np.array([15, 23, 8, 42, 16, 31, 27])

print("Data:", data)
print("Sum:", np.sum(data))                  # total of all the values
print("Mean:", np.mean(data))                # average value
print("Minimum:", np.min(data))              # smallest value
print("Maximum:", np.max(data))              # largest value
print("Standard Deviation:", np.std(data))   # how spread out the values are

# Step 8 - A closing divider so the console output is easy to read
print("\n" + "=" * 60)
```

**Sample output (values may vary slightly by machine/Python version):**

```
--- Memory Efficiency ---
Python List memory (approx): 8,320 bytes
NumPy Array memory: 8,000 bytes
Memory saved using NumPy: 320 bytes

--- Data Type Handling ---
Python List (mixed types): [1, 'hello', 3.14, True, [1, 2]]
Types in list: ['int', 'str', 'float', 'bool', 'list']

NumPy Array (mixed input): ['1' 'hello' '3.14' 'True']
Array data type: <U32

--- Element-wise Operations ---
List doubled: [2, 4, 6, 8, 10]
Array doubled: [ 2  4  6  8 10]

--- Mathematical Operations ---
Addition: [11 22 33 44 55]
Subtraction: [ 9 18 27 36 44]
Multiplication: [ 10  40  90 160 250]
Division: [10. 10. 10. 10. 10.]
Square root of array1: [1.         1.41421356 1.73205081 2.         2.23606798]

--- Aggregation Functions ---
Data: [15 23  8 42 16 31 27]
Sum: 162
Mean: 23.142857142857142
Minimum: 8
Maximum: 42
Standard Deviation: 10.605998987428
```

**Beginner tip:** Notice the memory saving in this particular run is
modest — that's because a list of only 1,000 small whole numbers isn't
very large to begin with. Try changing `1000` to `1_000_000` in Steps 2–3
and re-running: the *percentage* difference in memory use becomes far more
dramatic as the data grows, which is exactly why NumPy matters so much more
once you're working with large, real-world datasets.

---

## Making sense of the results

### 1. Memory efficiency

NumPy arrays typically use **noticeably less memory** than Python lists
holding the same numbers, because:

- A Python list stores a separate reference to each item — the items
  themselves live elsewhere in memory, each with their own small amount of
  overhead.
- A NumPy array stores its data in **one continuous block**, with no
  per-item overhead, since every item is guaranteed to be the same type and
  size.

This is exactly why NumPy (and libraries built on it, like pandas) is the
standard choice once a dataset gets large.

### 2. Data type behaviour

A Python list will happily hold a mix of:

- whole numbers,
- decimal numbers,
- text,
- `True`/`False` values, and
- even other lists, nested inside.

A NumPy array, by contrast, **converts everything to one shared type** the
moment it's created. In the script above, including a text string forced
NumPy to convert every value — even the numbers — into text, so they could
all live together in the same array.

### 3. Operations

Where a list needs an explicit loop (or a list comprehension standing in
for one) to process every item, a NumPy array lets you write the operation
once — `array * 2` — and have it apply to every element automatically. This
shortcut is called **vectorization**, and besides being shorter to write,
it also runs meaningfully faster, since NumPy performs the repetition in
efficient, pre-compiled code rather than in the Python interpreter's own
slower loop.

### 4. Mathematical and statistical tools

NumPy comes with a large library of ready-made numerical tools — square
root, sum, mean, standard deviation, and many more — that a plain list
simply doesn't have built in. This is a big part of why NumPy underpins
almost the entire Python data-science ecosystem (including pandas,
scikit-learn, and TensorFlow).

---

## Final takeaway

| Use a Python list when… | Use a NumPy array when… |
| --- | --- |
| You need to mix different data types together | Every value is the same type (typically numbers) |
| The collection is small, or changes shape/size often | You're doing maths on large amounts of numeric data |
| You want maximum flexibility and simplicity | You want speed, compact memory use, and built-in numerical tools |

Python lists remain the right everyday tool for general-purpose
programming. NumPy arrays become the better tool the moment your work turns
numerical, especially at scale — which is why they form the foundation for
data analysis, machine learning, and scientific computing throughout the
Python ecosystem.

---

## Follow-up questions for practice

*(These are additional, optional questions to test your understanding —
they don't replace or change any of the printed book's original content.)*

1. If you increase the list/array size in the script from `1000` to
   `100_000`, what do you expect to happen to the memory-saving figure, and
   why?
2. What data type (`.dtype`) would you expect if you created a NumPy array
   from `[1, 2, 3.5]` — a mix of whole numbers and one decimal, but **no**
   text? Try it and check your prediction.
3. Rewrite the "list doubled" step using a plain `for` loop instead of a
   list comprehension. Does the output change? Does the *readability*
   change?
4. `np.std()` measures how spread out a set of values is. Without changing
   any values, what would happen to the standard deviation if you added
   one more number to `data` that was very far from the others (e.g.
   `500`)? Try it and see if your intuition matches the result.





