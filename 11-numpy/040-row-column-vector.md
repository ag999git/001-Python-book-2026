


# Chapter 11 — Research Project: Row Vectors vs. Column Vectors in NumPy and Linear Algebra

## About this chapter

This page works through a research project on **vectors** — one of the most
fundamental ideas in linear algebra, and one you'll meet constantly in data
science and machine learning. Specifically, it looks at the two ways a list
of numbers can be arranged: as a **row** (side by side) or as a **column**
(stacked vertically). The two forms hold exactly the same numbers, but as
you'll see, *orientation* changes what you can do with them mathematically
— especially once matrices and geometric transformations (like rotating or
resizing a shape) enter the picture.

By the end of this page you should be able to:

- Tell a row vector and a column vector apart, both on paper and in NumPy's `shape` output.
- Explain why a plain Python list, a NumPy 1D array, a row vector, and a column vector are all subtly different things.
- Understand *why* transformations like rotation and scaling are written as `matrix × column vector`.
- Run and modify working NumPy scripts that rotate and scale a point in 2D.

> **Quick glossary, before we start**
> - **Vector** — in this context, simply an ordered list of numbers. See
>   [Khan Academy's intro to vectors](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:vectors).
> - **Matrix** — a rectangular grid of numbers, arranged in rows and
>   columns. See [Khan Academy's intro to matrices](https://www.khanacademy.org/math/algebra-home/alg-matrices).
> - **Shape** (in NumPy) — a tuple describing an array's dimensions, e.g.
>   `(3, 1)` means 3 rows and 1 column.
> - **`reshape()`** — a NumPy method that rearranges the same values into a
>   different shape, without changing the values themselves.
> - **Matrix multiplication** — a specific way of combining two matrices
>   (or a matrix and a vector) that is *not* the same as multiplying
>   numbers one by one. See [Khan Academy's guide to matrix multiplication](https://www.khanacademy.org/math/algebra-home/alg-matrices/alg-multiplying-matrices-by-matrices/a/multiplying-matrices).
> - **Linear transformation** — a mathematical operation (like rotating,
>   scaling, or reflecting) that moves every point in space according to a
>   consistent rule, usually written as `matrix × vector`.

---

## Research / Project Question



> Study the concept of **row vectors and column vectors** in NumPy and
> linear algebra.
> Explain their structure, differences, and practical use cases in data
> science, machine learning, and mathematical transformations.
>
> Your study should include:
>
> 1. Definition and structure of row vectors and column vectors.
> 2. Comparison between:
>    - Python lists
>    - NumPy 1D arrays
>    - Row vectors
>    - Column vectors
> 3. Explanation of why many mathematical transformations use **column vectors**.
> 4. Demonstration of matrix multiplication involving:
>    - Matrix × Column vector
> 5. Implementation of geometric transformations such as:
>    - Rotation of a point in a 2D system
>    - Scaling transformation
> 6. Use NumPy scripts to demonstrate the concepts.
> 7. Include tables, diagrams, and explanations.
>
> Finally, conclude when it is preferable to use row vectors and when
> column vectors are more appropriate.

---

# Answer

## 1. Introduction

A **vector** — an ordered list of numbers — is one of the most basic
building blocks in mathematics, data science, and machine learning. In
NumPy, the same set of numbers can be arranged in more than one way, and
two of the most important arrangements are:

- the **row vector** — values laid out horizontally, and
- the **column vector** — values stacked vertically.

Both forms store identical values. What changes is their **orientation**,
and that difference turns out to matter a great deal once you start doing
matrix multiplication or geometric transformations — the same numbers,
arranged the "wrong" way, can produce a completely different (or invalid)
calculation.

![Flowchart](../resources/ch-11-numpy-august-2026-row-vs-column-vector.png)

---

## 2. Row Vector

A **row vector** arranges its values horizontally, in a single row.

Example:

`[ 3  5  7 ]`

Shape in NumPy: `(1, 3)` — meaning 1 row and 3 columns.

```python
# This script creates a ROW VECTOR: a 2D array with exactly one row.
#
# Step 1 - Import NumPy, the library used for array creation and maths.
import numpy as np

# Step 2 - Start with a plain 1D array of 3 values.
# Step 3 - reshape(1, 3) rearranges those same 3 values into a 2D shape:
#          1 row, 3 columns. No values are changed — only the arrangement is.
row_vector = np.array([3, 5, 7]).reshape(1, 3)

# Step 4 - Display the row vector and confirm its shape.
print(row_vector)             # Output: [[3 5 7]]
print("Shape:", row_vector.shape)   # Output: (1, 3) -> 1 row, 3 columns
```

---

## 3. Column Vector

A **column vector** arranges its values vertically, stacked one on top of
another.

Example:

```
[3
 5
 7]
```

Shape in NumPy: `(3, 1)` — meaning 3 rows and 1 column.

```python
# This script creates a COLUMN VECTOR: a 2D array with exactly one column.
#
# Step 1 - Import NumPy.
import numpy as np

# Step 2 - Start with the same 3 values as before.
# Step 3 - reshape(3, 1) rearranges them into a 2D shape:
#          3 rows, 1 column — the values are stacked vertically instead
#          of laid out side by side.
column_vector = np.array([3, 5, 7]).reshape(3, 1)

# Step 4 - Display the column vector and confirm its shape.
print(column_vector)
# Output:
# [[3]
#  [5]
#  [7]]

print("Shape:", column_vector.shape)   # Output: (3, 1) -> 3 rows, 1 column
```

**Interpretation:** the same three values, `3`, `5`, and `7`, are now
stacked vertically instead of laid out side by side.

---

## 4. Comparison Table: Row Vector vs. Column Vector

| Feature | Row vector | Column vector |
| --- | --- | --- |
| Shape | `(1, n)` | `(n, 1)` |
| Orientation | Horizontal | Vertical |
| Common use | Represents one data record (e.g. one row of a spreadsheet) | Used in matrix transformations and geometric calculations |
| Machine learning | Often used to represent a single input for prediction | Often used internally in model computations |
| Linear algebra | Less commonly the "default" form | The standard, conventional way to represent a vector |

---

## 5. Comparison with Python Lists and NumPy 1D Arrays

It's worth pausing on a distinction that trips up a lot of beginners: a
**plain Python list**, a **NumPy 1D array**, and a **row or column vector**
are three different things, even though a beginner might describe all
three simply as "a list of numbers."

| Feature | Python list | NumPy 1D array | NumPy row/column vector |
| --- | --- | --- | --- |
| Structure | Very flexible — can mix data types, resize freely | Structured — one data type, fixed size | Structured, **and** has an explicit 2D shape |
| Shape | Not defined (`len()` only, no `.shape`) | Defined, but only one dimension, e.g. `(3,)` | Defined with two dimensions, e.g. `(1, 3)` or `(3, 1)` |
| Supports matrix multiplication (`@`) | No | Only in a limited sense (as a 1D array) | Yes — this is exactly the form matrix maths expects |
| Performance | Slower for numeric work | Fast | Fast |

**Beginner tip:** a NumPy 1D array like `np.array([3, 5, 7])` has shape
`(3,)` — notice there's only *one* number in that tuple. It isn't yet
"officially" a row or a column; it's a flat sequence. Calling
`.reshape(1, 3)` or `.reshape(3, 1)` on it is what turns it into an
explicit row vector or column vector, with a proper 2D shape that matrix
mathematics expects.

---

## 6. Why Column Vectors Are Used in Transformations

In linear algebra, common geometric transformations — including:

- rotation,
- scaling,
- projection, and
- translation

are conventionally written as:

**`Matrix × Column Vector`**

or, in the shorthand you'll see in most textbooks:

**`y = Mx`**

where:

- `M` is the **transformation matrix** — it encodes *what* transformation is being applied,
- `x` is the **column vector** — it encodes the point (or points) being transformed, and
- `y` is the resulting column vector, after the transformation has been applied.


![Flowchart](../resources/ch-11-numpy-august-2026-row-vs-column-vector-2.png)



**Why a column, specifically?** The rule for matrix multiplication requires
the number of *columns* in the first item to match the number of *rows* in
the second. An `n × n` transformation matrix naturally lines up with an
`n × 1` column vector — that's simply the shape matrix multiplication
expects on the right-hand side. Writing the point as a row vector instead
would require flipping the whole equation around (`y = xM` with `x` as a
row vector), which is mathematically possible but is *not* the convention
most textbooks, libraries, and courses use — so column vectors have become
the standard, expected form.

---

## 7. Example: Rotation by 90 Degrees

Suppose we have a point at `(2, 1)`. We represent it as a column vector so
it's ready for matrix multiplication.

The rotation matrix for a 90° counter-clockwise turn is:

```
[ 0  -1 ]
[ 1   0 ]
```

**Why this particular matrix?** Multiplying it by a point `(x, y)` produces
`(-y, x)` — swapping the coordinates and flipping one sign — which is
exactly the geometric effect of a 90° counter-clockwise rotation around the
origin.

## 8. Script: Rotation by 90 Degrees

```python
# Rotation Transformation Example

import numpy as np

# Step 1 - Create the original point (2, 1) as a COLUMN VECTOR.
# reshape(2, 1) gives it the shape matrix multiplication expects:
# 2 rows, 1 column.
point = np.array([2, 1]).reshape(2, 1)

print("Original Point:")
print(point)

# Step 2 - Create the 90-degree rotation matrix.
# For a 90-degree counter-clockwise rotation in 2D, the matrix is:
#   [ 0  -1 ]
#   [ 1   0 ]
# because it transforms any point (x, y) into (-y, x).
rotation_matrix = np.array([
    [0, -1],
    [1,  0]
])

print("\nRotation Matrix:")
print(rotation_matrix)

# Step 3 - Perform the transformation: matrix @ column_vector.
# The @ operator performs proper matrix multiplication in Python/NumPy
# (this is NOT the same as multiplying two arrays element-by-element).
#
# By hand, this calculation is:
#   [ 0  -1 ] [2]   [ 0*2 + (-1)*1 ]   [-1]
#   [ 1   0 ] [1] = [ 1*2 +   0*1  ] = [ 2]
rotated_point = rotation_matrix @ point

print("\nRotated Point:")
print(rotated_point)
# Output:
# [[-1]
#  [ 2]]
```

**Beginner tip:** try tracing the "by hand" calculation in the comment
against the actual printed output — matching a small example like this by
hand is one of the best ways to build real confidence in matrix
multiplication, rather than just trusting that `@` does the right thing.

### The following figure shows how the point gets rotated




![2D diagram showing a point rotated 90 degrees using a rotation matrix](../resources/ch11-final-vector-rotation.png)

---


## 9. Example: Scaling Transformation

**Scaling** increases or decreases the size of a shape, stretching or
shrinking it along each axis independently.

If:

- $s_x$ = the scaling factor along the X-axis, and
- $s_y$ = the scaling factor along the Y-axis,

then the scaling matrix is a **diagonal matrix** (a matrix with values only
along its main diagonal, and zeros everywhere else):

$$
S = \begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}
$$

For example, the matrix

```
[2 0]
[0 3]
```

scales every point's `x`-coordinate by `2` and its `y`-coordinate by `3`.

## 10. Script: Scaling Transformation

```python
# Scaling Transformation Example

import numpy as np

# Step 1 - Create the original point (3, 4) as a COLUMN VECTOR.
point = np.array([3, 4]).reshape(2, 1)

# Step 2 - Create the scaling matrix.
# This is a diagonal matrix: 2 along the top-left (scales x),
# 3 along the bottom-right (scales y), and zeros elsewhere.
scaling_matrix = np.array([
    [2, 0],
    [0, 3]
])

# Step 3 - Perform the transformation: matrix @ column_vector.
# The @ operator performs matrix multiplication, applying the scaling
# factors to the point's x and y coordinates independently.
scaled_point = scaling_matrix @ point

print("Scaled Point:")
print(scaled_point)
# Output:
# [[ 6]
#  [12]]
# (x: 3 * 2 = 6,  y: 4 * 3 = 12)
```

## Figure showing scaling in 2D



![Figure showing a point scaled using a diagonal scaling matrix](../resources/ch11-scaling-matrix.png)


---

## 11. Conclusion: When to Use Row Vectors vs. Column Vectors

Bringing together everything above, here's a practical rule of thumb:

| Use a **row vector** when… | Use a **column vector** when… |
| --- | --- |
| You're representing one record/observation in a dataset (e.g. one row of a spreadsheet or CSV file) | You're representing a point, direction, or quantity that will go through matrix multiplication |
| You're feeding a single example into a machine-learning model for prediction | You're performing geometric transformations — rotation, scaling, projection, translation |
| Readability alongside tabular data matters more than matrix-multiplication conventions | You want to follow the standard linear-algebra convention (`y = Mx`) used in nearly every textbook and library |

In short: **row vectors are the natural fit for "one record of data,"**
the way you'd think of a single row in a spreadsheet, while **column
vectors are the natural fit for "one mathematical object being
transformed,"** the way you'd think of a point moving through space. When
in doubt, and especially when working with transformation matrices, the
column vector is the safer, more conventional default.

![Flowchart](../resources/ch-11-numpy-august-2026-row-vs-column-vector-3.png)


---

## Follow-up questions for practice

*(These are additional, optional questions for self-testing — they don't
replace or change the original research question above.)*

1. Take the row vector `np.array([3, 5, 7]).reshape(1, 3)` and the column
   vector `np.array([3, 5, 7]).reshape(3, 1)`. What happens if you try
   `row_vector @ column_vector`? What about `column_vector @ row_vector`?
   Predict the resulting shape *before* running the code, then check.
2. Modify the rotation script to rotate the point `(2, 1)` by 90° a second
   time (i.e. rotate the already-rotated point again). What point do you
   end up at, and how does that compare to rotating the original point by
   180° in one step?
3. Write a scaling matrix that scales `x` by `0.5` (shrinking it) and
   leaves `y` unchanged. Apply it to the point `(8, 8)` and predict the
   result before running your code.
4. A NumPy 1D array such as `np.array([3, 5, 7])` has shape `(3,)`. Why is
   this considered neither a row vector nor a column vector until it's
   reshaped? What practical problems might this cause if you forget to
   reshape it before a matrix multiplication?






