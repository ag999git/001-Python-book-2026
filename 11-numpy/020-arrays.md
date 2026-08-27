


# Chapter 11 — Creating NumPy Arrays: A Complete Reference

## About this reference

NumPy is the library almost every numerical, data-science, and
machine-learning tool in Python is built on. Before you can do anything
useful with it — maths, statistics, image processing, plotting — you first
need an **array** to work with. This page is a reference for **every common
way to create one**, organised into three levels so you can learn them in a
sensible order rather than all at once:

- **Beginner** — the everyday, "I just need an array" functions you'll use
  constantly (`np.array()`, `np.zeros()`, `np.arange()`, and similar).
- **Intermediate** — functions for copying the *shape* of an existing array,
  building identity/diagonal matrices, and creating coordinate grids.
- **Advanced** — more specialised tools: building arrays from generators or
  formulas, converting data efficiently, and generating random numbers for
  simulations or machine-learning datasets.

Each function is described the same way — what it's for, what you feed it,
what you get back, and any mistake beginners commonly make with it — so you
can also use this page as a quick lookup later, not just a first read.

> **Quick glossary, before we start**
> - **Array / `ndarray`** — NumPy's core data structure: a grid of values,
>   all the same type. See the [NumPy absolute-beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html).
> - **`shape`** — the size of an array along each dimension, written as a
>   tuple, e.g. `(2, 3)` means 2 rows and 3 columns.
> - **`dtype`** — short for "data type"; tells you (or tells NumPy) whether
>   the values are whole numbers, decimals, text, etc. See the
>   [NumPy data types guide](https://numpy.org/doc/stable/reference/arrays.dtypes.html).
> - **Vectorized** — an operation applied to a whole array at once, instead
>   of one value at a time in a loop.
> - **Identity matrix** — a square grid of numbers with `1`s down the main
>   diagonal and `0`s everywhere else; important in linear algebra. See
>   [Khan Academy's explanation](https://www.khanacademy.org/math/algebra-home/alg-matrices/alg-identity-inverse-matrices/a/intro-to-identity-matrices).
> - **Random seed / distribution** — "distribution" describes the *pattern*
>   random numbers follow (e.g. every value equally likely, versus most
>   values clustering near an average). See the
>   [NumPy random sampling guide](https://numpy.org/doc/stable/reference/random/index.html).


![Flowchart](/resources/ch-11-numpy-august-2026-numpy-array-creation-beginner-to-advanced.png)


---

# BEGINNER LEVEL FUNCTIONS

These eight functions cover the great majority of everyday array creation.
If you only remember a handful of NumPy functions, make it these.

## 1. `np.array()`

**Signature**

`np.array(object, dtype=None, copy=True, ndmin=0)`

**Parameters**

- `object` → the data you already have: a list, tuple, or nested list
- `dtype` → the data type to force (optional — NumPy will guess if you leave this out)
- `copy` → whether to make a fresh copy of the data (`True` by default)
- `ndmin` → the minimum number of dimensions the result should have

**Output**

A NumPy array (technically an `ndarray`).

Example output:

`array([1, 2, 3])`

**Common usage**

- Turning a Python list into a NumPy array
- Building matrices from nested lists

**Possible errors**

`ValueError: setting an array element with a sequence` — this happens when
the inner lists of a nested list don't all have the same length, so NumPy
can't arrange them into a neat rectangular grid.

**Important notes**

- NumPy automatically works out the data type for you if you don't specify one
- This is the single most commonly used array-creation function

---

## 2. `np.zeros()`

**Signature**

`np.zeros(shape, dtype=float)`

**Parameters**

- `shape` → a tuple describing the array's dimensions, e.g. `(2, 3)`
- `dtype` → the data type of the values (defaults to decimal/`float`)

**Output**

An array of the given shape, filled entirely with `0`.

**Common usage**

- Setting up an empty matrix before filling it in a loop
- Creating a "blank slate" placeholder array

**Possible errors**

`TypeError: 'int' object is not iterable` — this happens if you pass a
single plain number instead of a tuple for `shape` where NumPy expects one
(e.g. writing `np.zeros(2, 3)` instead of `np.zeros((2, 3))`).

---

## 3. `np.ones()`

**Signature**

`np.ones(shape, dtype=float)`

**Output**

An array of the given shape, filled entirely with `1`.

**Common usage**

- Starting weights in a simple machine-learning model
- General matrix operations where an all-ones starting point is useful

---

## 4. `np.full()`

**Signature**

`np.full(shape, fill_value, dtype=None)`

**Parameters**

- `shape` → the dimensions of the array
- `fill_value` → the single value used to fill every position

**Output**

An array of the given shape, filled entirely with `fill_value`.

---

## 5. `np.arange()`

**Signature**

`np.arange(start, stop, step, dtype=None)`

**Output**

A one-dimensional array counting from `start` up to (but **not including**)
`stop`, in steps of `step` — the same idea as Python's built-in `range()`,
but producing a NumPy array.

Example:

`array([0, 2, 4, 6, 8])`

**Common usage**

Generating a numeric sequence, e.g. for looping or for x-axis values on a
chart.

**Common error**

Using a decimal (floating-point) `step` can sometimes produce one extra or
one fewer value than you expect, because of how computers represent
decimals internally. If you need an *exact* number of evenly spaced values,
prefer `np.linspace()` below instead.

---

## 6. `np.linspace()`

**Signature**

`np.linspace(start, stop, num=50)`

**Output**

An array of exactly `num` evenly spaced values between `start` and `stop`.

**Important note**

Unlike `np.arange()`, `np.linspace()` **includes** the `stop` value by
default. This is the key difference to remember between the two: use
`np.arange()` when you care about the *step size*, and `np.linspace()` when
you care about the *exact number of values*.

---

## 7. `np.eye()`

**Signature**

`np.eye(N, M=None, k=0)`

**Parameters**

- `N` → number of rows
- `M` → number of columns (defaults to the same as `N`, making a square matrix)
- `k` → which diagonal gets the `1`s: `0` is the main diagonal, positive
  values shift it up-and-right, negative values shift it down-and-left

**Output**

An identity-style matrix — `1`s along the chosen diagonal, `0`s everywhere
else.

---

## 8. `np.random.rand()`

**Signature**

`np.random.rand(d0, d1, ..., dn)`

**Output**

An array of the given shape, filled with random decimal values between `0`
(inclusive) and `1` (exclusive), each equally likely — what statisticians
call a **uniform distribution**.

---

## Table (Beginner Level)

| # | Method | Purpose | Example | Input | Output | Key concept | When to use | Important note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `np.array()` | Convert existing data to a NumPy array | `np.array([1,2,3])` | List / tuple | n-D array | Basic conversion | Almost always your first step | Creates a new array by default |
| 2 | `np.zeros()` | Create an array of zeros | `np.zeros((2,3))` | Shape | Numeric array | Initialization | Starting point before filling in values | `dtype` defaults to `float` |
| 3 | `np.ones()` | Create an array of ones | `np.ones((3,3))` | Shape | Numeric array | Matrix creation | ML weight init / matrix maths | Efficient, common starting point |
| 4 | `np.full()` | Create an array of one repeated value | `np.full((2,2),7)` | Shape + value | Numeric array | Constant arrays | Any fixed default value | Flexible `dtype` |
| 5 | `np.arange()` | Create a sequence with a fixed step | `np.arange(0,10,2)` | Start/stop/step | 1D array | Range generation | Loops, simple sequences | `stop` value is excluded |
| 6 | `np.linspace()` | Create a fixed *count* of evenly spaced values | `np.linspace(0,1,5)` | Start/stop/count | 1D array | Fixed number of values | Plotting axes | `stop` value is included |
| 7 | `np.eye()` | Create an identity-style matrix | `np.eye(3)` | Size | Square matrix | Linear algebra basics | Matrix maths | Supports a diagonal offset (`k`) |
| 8 | `np.random.rand()` | Create random decimals between 0 and 1 | `np.random.rand(2,2)` | Dimensions | Numeric array | Random generation | Simulations, quick test data | Uniform distribution |

## Script (Beginner)

```python
# NumPy Array Creation Examples
# Beginner level
import numpy as np

# Step 1 - np.array(): build a NumPy array directly from a Python list.
# All elements here are integers, so NumPy stores them as one integer array.
a = np.array([1, 2, 3])
print(a)

# Possible error to be aware of:
# np.array([[1, 2], [3, 4, 5]])
# This raises a ValueError, because the two inner lists have different
# lengths (2 items vs. 3 items). NumPy needs every row of a 2D array to
# have the same number of columns.

# Step 2 - np.zeros(): create an array filled entirely with zeros.
# The shape (2, 3) means 2 rows and 3 columns.
b = np.zeros((2, 3))
print(b)

# Step 3 - np.ones(): create an array filled entirely with ones.
# The shape (3, 3) means 3 rows and 3 columns.
c = np.ones((3, 3))
print(c)

# Step 4 - np.full(): create an array filled with one chosen value.
# First argument is the shape, second argument is the fill value (7 here).
d = np.full((2, 2), 7)
print(d)

# Step 5 - np.arange(): create a sequence of numbers with a fixed step size.
# Counts from 0 up to (but not including) 10, in steps of 2.
e = np.arange(0, 10, 2)
print(e)

# Step 6 - np.linspace(): create a fixed NUMBER of evenly spaced values.
# 5 values spread evenly between 0 and 1, INCLUDING both endpoints.
f = np.linspace(0, 1, 5)
print(f)

# Step 7 - np.eye(): create an identity matrix (1s on the diagonal, 0s elsewhere).
# The argument (3) is the size — a 3x3 square matrix.
g = np.eye(3)
print(g)

# Step 8 - np.random.rand(): create random decimals between 0 and 1.
# The shape (2, 2) is given as two separate arguments, not a tuple.
h = np.random.rand(2, 2)
print(h)
```

---

# INTERMEDIATE LEVEL FUNCTIONS

These functions build on the beginner set — copying the shape of an
existing array, creating diagonal/identity matrices in more ways, and
generating coordinate grids for plotting or image work.

## 9. `np.empty()`

**Signature**

`np.empty(shape, dtype=float)`

**Output**

An array of the given shape whose values are **not** set to anything in
particular.

**Important**

Whatever happens to already be sitting in that block of memory is what you
see — it is *not* guaranteed to be zero, and will look different (and
essentially random) each time you run it.

**Common error**

Don't assume `np.empty()` gives you zeros — it doesn't. Use `np.zeros()`
instead if you specifically want zeros; use `np.empty()` only when you plan
to immediately overwrite every value yourself and just want the fastest
possible allocation.

---

## 10. `np.zeros_like()`

**Signature**

`np.zeros_like(a)`

Creates a new array of zeros that automatically matches the **shape and
data type** of an existing array `a`, so you don't have to work those out
and type them in yourself.

---

## 11. `np.ones_like()`

Same idea as `np.zeros_like()`, but fills the new array with `1` instead of
`0`.

---

## 12. `np.full_like()`

Same idea again, but fills the new array (matching the shape/type of an
existing array) with any constant value you choose.

---

## 13. `np.identity()`

A simpler, square-only version of `np.eye()` — just give it the size, and
it returns an `N x N` identity matrix. Use `np.eye()` instead if you need a
non-square matrix or a diagonal offset.

---

## 14. `np.diag()`

Does one of **two different things**, depending on what you give it:

- Given a **1D array/list**, it builds a full square matrix with those
  values placed along the diagonal.
- Given a **2D array/matrix**, it does the reverse — it *extracts* the
  diagonal values and returns them as a 1D array.

**Common confusion:** because the same function name does two opposite
things depending on its input's shape, it's easy to call it expecting one
behaviour and get the other. Always check whether what you're passing in
is 1D or 2D.

---

## 15. `np.logspace()`

Like `np.linspace()`, but the values are spaced evenly on a **logarithmic**
scale rather than a plain linear one — useful whenever a quantity spans
several orders of magnitude (very small to very large), which comes up
often in scientific and engineering work.

---

## 16. `np.meshgrid()`

Takes two 1D arrays representing x-coordinates and y-coordinates, and
expands them into two full 2D grids — one holding the x-value and one
holding the y-value at every point on the grid. This is the standard way
to prepare data for plotting a 3D surface or a contour map.

---

## 17. `np.indices()`

Builds an array of the **row and column index numbers** for a grid of a
given shape — handy any time you need to know *where* (not just *what*) a
value sits, such as in image processing or custom matrix maths.

---

## Table (Intermediate Level)

| # | Method | Purpose | Example | Input | Output | Shape rule | Key feature | Typical use | Important note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | `np.empty()` | Allocate an array without setting its values | `np.empty((3,3))` | Shape | Numeric array | User-defined | Very fast allocation | Performance-critical code | Contains leftover "garbage" values |
| 10 | `np.zeros_like()` | Copy another array's shape, filled with zeros | `np.zeros_like(A)` | Array | Same-shape array | Matches input | Ready-made template | Algorithms needing a same-sized buffer | Keeps the same shape and dtype |
| 11 | `np.ones_like()` | Copy another array's shape, filled with ones | `np.ones_like(A)` | Array | Same shape | Same as source | Efficient replication | ML model setup | Keeps the same dtype |
| 12 | `np.full_like()` | Copy another array's shape, filled with a constant | `np.full_like(A,9)` | Array | Same shape | Based on input | Structured duplication | Building matrix templates | Keeps the shape consistent |
| 13 | `np.identity()` | Create a square identity matrix | `np.identity(4)` | Size | Square matrix | `n × n` | Simpler syntax than `eye()` | Linear algebra | No diagonal-offset option (use `eye()` for that) |
| 14 | `np.diag()` | Create OR extract a diagonal | `np.diag([1,2,3])` | Array | Matrix or vector | Depends on input | Works two opposite ways | Matrix operations | Check whether your input is 1D or 2D |
| 15 | `np.logspace()` | Create values spaced on a log scale | `np.logspace(1,3,5)` | Start/stop exponent, count | 1D array | Fixed length | Logarithmic progression | Scientific/engineering ranges | Values span orders of magnitude |
| 16 | `np.meshgrid()` | Build a coordinate grid from two axes | `np.meshgrid(x,y)` | Two 1D arrays | Two 2D grid arrays | Expanded grid | Pairs up every x with every y | 3D surface plotting | Mainly a visualization tool |
| 17 | `np.indices()` | Build an array of row/column index numbers | `np.indices((3,3))` | Shape | Index arrays | Multi-dimensional | Reveals *position*, not value | Image processing, custom indexing | A more advanced/less common tool |

## Script (Intermediate)

```python
# NumPy Array Creation Examples
# Intermediate level
import numpy as np

# Step 9 - np.empty(): allocate space for an array WITHOUT setting values.
# Whatever numbers show up are just whatever was already in that memory —
# don't rely on them being zero, or on them looking the same twice.
a = np.empty((3, 3))
print("np.empty():->\n", a)

# Step 10 - np.zeros_like(): create a same-shaped array of zeros, copying
# the shape and dtype of 'a' automatically.
b = np.zeros_like(a)
print("np.zeros_like():->\n", b)

# Step 11 - np.ones_like(): same idea, but filled with ones instead.
c = np.ones_like(a)
print("np.ones_like():->\n", c)

# Step 12 - np.full_like(): same idea again, but filled with a chosen
# constant value (9 here) instead of zeros or ones.
d = np.full_like(a, 9)
print("np.full_like():->\n", d)

# Step 13 - np.identity(): a simpler way to build a square identity matrix.
# The single argument (4) gives a 4x4 matrix.
e = np.identity(4)
print("np.identity():->\n", e)

# Step 14 - np.diag(): given a 1D list, BUILDS a matrix with those values
# on the diagonal (and zeros everywhere else).
f = np.diag([1, 2, 3])   # produces a 3x3 array with 1, 2, 3 on the diagonal
print("np.diag() [build mode]:->\n", f)

# np.diag() also works the OPPOSITE way: given a 2D matrix, it EXTRACTS
# just the diagonal values as a 1D array. Here it pulls [1, 2, 3] back out
# of the matrix we just built.
print("np.diag(f) [extract mode]:->\n", np.diag(f))

# Step 15 - np.logspace(): 5 values spaced evenly on a LOG scale,
# from 10^1 (=10) to 10^3 (=1000).
g = np.logspace(1, 3, 5)
print("np.logspace():->\n", g)

# Step 16 - np.meshgrid(): build a coordinate grid from two axis arrays.
x = np.arange(3)          # x-coordinates: [0, 1, 2]
y = np.arange(3)          # y-coordinates: [0, 1, 2]
X, Y = np.meshgrid(x, y)  # X and Y together describe every (x, y) point on the grid
print("np.meshgrid() X:->\n", X)
print("np.meshgrid() Y:->\n", Y)

# Step 17 - np.indices(): build the row-index and column-index grids for
# a 2x2 shape. The first sub-array is the row number of each cell; the
# second sub-array is the column number of each cell.
print("np.indices():->\n", np.indices((2, 2)))
```

---

# ADVANCED LEVEL FUNCTIONS

These tools are more specialised: building arrays from generators or
formulas, converting existing data efficiently, and generating random
numbers for simulations, testing, or machine-learning datasets.

## 18. `np.fromiter()`

**Signature**

`np.fromiter(iterable, dtype)`

Builds an array directly from any Python iterable (such as a generator),
one value at a time — useful when your data is a stream that would be
wasteful to first convert into a full list.

---

## 19. `np.fromfunction()`

**Signature**

`np.fromfunction(function, shape)`

Builds an array by calling `function` once for every position, passing in
that position's row/column indices — a compact way to generate an array
straight from a mathematical formula.

---

## 20. `np.asarray()`

Converts input into an array, **without making an unnecessary copy** if the
input is already a compatible NumPy array. This makes it a memory-efficient
alternative to `np.array()` when you're not sure whether your input is
already an array.

---

## 21. `np.asanyarray()`

Behaves like `np.asarray()`, but if the input is already a *subclass* of
NumPy's array type (a specialised variant), it preserves that subclass
instead of converting it down to a plain array. This distinction rarely
matters for beginners — it's mainly relevant once you start working with
specialised array types.

---

## 22. `np.random.randint()`

Generates random **whole numbers** within a given range — useful whenever
you need discrete random values rather than decimals.

---

## 23. `np.random.randn()`

Generates random numbers from the **standard normal distribution** (the
classic "bell curve," centred on `0` with a standard deviation of `1`) —
as opposed to `np.random.rand()`, which spreads values evenly rather than
clustering them near a centre.

---

## 24. `np.random.choice()`

Randomly samples values **from an existing collection** you provide,
rather than generating brand-new numbers — useful for shuffling, sampling
a dataset, or simulating a dice roll from a specific set of outcomes.

---

## 25. `np.random.uniform()`

Generates random decimal numbers evenly spread across a range you choose —
essentially `np.random.rand()` but letting you set your own lower and
upper bounds instead of being fixed to `0`–`1`.

---

## Table (Advanced Level)

| # | Method | Purpose | Example | Input | Output | Key idea | Performance benefit | Typical use | Important note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18 | `np.fromiter()` | Build an array from an iterator/generator | `np.fromiter(range(5), int)` | Iterable | 1D array | Stream processing | Memory efficient for large streams | Large or lazy data sources | `dtype` must be given |
| 19 | `np.fromfunction()` | Generate an array from a formula | `np.fromfunction(lambda i,j:i+j,(3,3))` | Function + shape | Computed array | Index-based creation | Vectorized generation | Mathematical modeling | Very flexible, slightly harder to read |
| 20 | `np.asarray()` | Convert to array without copying unnecessarily | `np.asarray(data)` | Sequence | Array | Memory sharing | Avoids duplicate data | Performance-sensitive conversions | Faster than `np.array()` when input is already an array |
| 21 | `np.asanyarray()` | Convert to array, preserving subclasses | `np.asanyarray(data)` | Array-like | Array or subclass | Flexible conversion | Keeps specialised array types intact | Advanced/specialised workflows | Rarely needed as a beginner |
| 22 | `np.random.randint()` | Random whole numbers | `np.random.randint(0,10,(3,3))` | Range + shape | Integer array | Discrete random values | — | Simulations, test datasets | Upper bound is excluded |
| 23 | `np.random.randn()` | Random numbers, bell-curve distributed | `np.random.randn(3,3)` | Shape | Numeric array | Normal ("Gaussian") distribution | — | Statistical modeling, ML init | Centred on 0, standard deviation 1 |
| 24 | `np.random.choice()` | Randomly sample from existing values | `np.random.choice(a,5)` | Dataset | Random array | Sampling | Supports weighted probabilities | Data science, shuffling | Can sample with or without replacement |
| 25 | `np.random.uniform()` | Random decimals in a chosen range | `np.random.uniform(0,5,10)` | Range + size | Numeric array | Continuous, evenly spread | Flexible range | Simulations, statistics | Range is fully under your control |

## Script (Advanced)

```python
# NumPy Array Creation Examples
# Advanced level
import numpy as np

# Step 18 - np.fromiter(): build an array from a Python iterable (here, a
# range object) one value at a time. dtype must always be specified.
a = np.fromiter(range(5), dtype=int)
print("np.fromiter():->\n", a)

# Step 19 - np.fromfunction(): build an array by calling a function once
# per position. The lambda receives the (row, column) indices i, j and
# returns the value that belongs at that position — here, simply i + j.
b = np.fromfunction(lambda i, j: i + j, (3, 3))
print("np.fromfunction():->\n", b)

# Step 20 - np.asarray(): convert a list into an array. If the input were
# already a NumPy array, this would return it as-is rather than copying it.
c = np.asarray([1, 2, 3])
print("np.asarray():->\n", c)

# Step 21 - np.asanyarray(): behaves like asarray() here since 'c' is
# already a plain ndarray — so it's simply returned unchanged.
d = np.asanyarray(c)
print("np.asanyarray():->\n", d)

# Step 22 - np.random.randint(): random WHOLE numbers from 0 up to
# (not including) 10, arranged in a 3x3 shape.
e = np.random.randint(0, 10, (3, 3))
print("np.random.randint():->\n", e)

# Step 23 - np.random.randn(): random numbers from the standard normal
# ("bell curve") distribution — most values land close to 0.
# Re-running this line will give different numbers every time.
f = np.random.randn(3, 3)
print("np.random.randn():->\n", f)

# Step 24 - np.random.choice(): randomly PICK 5 values out of the given
# list [10, 20, 30] (with repeats allowed by default).
g = np.random.choice([10, 20, 30], 5)
print("np.random.choice():->\n", g)

# Step 25 - np.random.uniform(): 10 random decimal numbers, evenly spread
# between 0 (inclusive) and 5 (exclusive).
h = np.random.uniform(0, 5, 10)
print("np.random.uniform():->\n", h)
```

---

## Complete NumPy Array-Creation Map

The tree below groups every array-creation tool by *what kind of input it
starts from* — useful as a "which function do I actually want?" lookup.

![Flowchart](/resources/ch-11-numpy-august-2026-numpy-array-creation-complete-map.png)




For reference, here is the same map in its original plain-text tree form:

```text
NumPy Array Creation
│
├── From Existing Data
│   ├── array
│   ├── asarray
│   ├── asanyarray
│   ├── fromiter
│   ├── fromfunction
│   ├── frombuffer
│   ├── loadtxt
│   ├── genfromtxt
│
├── Basic Arrays
│   ├── zeros
│   ├── ones
│   ├── full
│   ├── empty
│
├── Template-Based Arrays
│   ├── zeros_like
│   ├── ones_like
│   ├── full_like
│   ├── empty_like
│
├── Sequence Arrays
│   ├── arange
│   ├── linspace
│   ├── logspace
│   ├── geomspace
│
├── Matrix / Diagonal Arrays
│   ├── eye
│   ├── identity
│   ├── diag
│   ├── diagflat
│   ├── tri
│   ├── tril
│   ├── triu
│
├── Grid / Coordinate Arrays
│   ├── meshgrid
│   ├── indices
│   ├── mgrid
│   ├── ogrid
│
├── Random Arrays
│   ├── rand
│   ├── randn
│   ├── randint
│   ├── random
│   ├── random_sample
│   ├── choice
│   ├── uniform
│   ├── normal
│
├── Structured / Special Arrays
│   ├── copy
│   ├── tile
│   ├── repeat
│
└── File / External Data Arrays
    ├── load
    ├── savez
    ├── savez_compressed
    ├── fromfile
```

---

## Summary: choosing the right function

| If you want to… | Reach for… |
| --- | --- |
| Turn a list you already have into an array | `np.array()` or `np.asarray()` |
| Start with a blank array of a given size | `np.zeros()`, `np.ones()`, or `np.full()` |
| Match the shape of an array you already have | `np.zeros_like()`, `np.ones_like()`, `np.full_like()` |
| Count up in equal steps | `np.arange()` (fixed step) or `np.linspace()` (fixed count) |
| Build a matrix for linear algebra | `np.eye()`, `np.identity()`, `np.diag()` |
| Prepare coordinates for plotting | `np.meshgrid()`, `np.indices()` |
| Generate random test data | `np.random.rand()`, `randint()`, `randn()`, `choice()`, `uniform()` |
| Build an array from a formula or generator | `np.fromfunction()`, `np.fromiter()` |

---

## Follow-up questions for practice

*(These are additional, optional questions for self-testing — they don't
replace or change any of the original reference content above.)*

1. What's the practical difference between `np.arange(0, 1, 0.1)` and
   `np.linspace(0, 1, 10)`? Run both and compare the exact number of values
   each one produces.
2. `np.zeros((3,3))` and `np.empty((3,3))` both create a 3×3 array — what's
   the one important difference in what you'll actually see when you print
   them?
3. Using `np.diag()`, first build a matrix from the list `[4, 5, 6]`, then
   feed that matrix straight back into `np.diag()` again. What do you get,
   and why does the same function produce two different kinds of results?
4. Why does `np.random.randn()` tend to produce values clustered close to
   `0`, while `np.random.rand()` spreads its values evenly between `0` and
   `1`? (Hint: look up "normal distribution" vs. "uniform distribution" in
   the glossary links above.)
5. Given an existing array `A`, write one line using a `_like()` function
   that creates a same-shaped array filled with the value `-1`.






