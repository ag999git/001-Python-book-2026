



# Chapter 11 — Project: Understanding 3D Arrays and Axis Operations in NumPy

## About this chapter

Up to now, you've mostly worked with 1D arrays (a simple list of numbers)
and 2D arrays (a grid of rows and columns). This project takes the natural
next step: **3D arrays** — arrays with a third dimension, best pictured as
several 2D grids stacked on top of one another, like pages in a notebook or
layers in a cake.

The real point of this project isn't just building a 3D array — it's
understanding **axes**, and specifically what happens when you tell NumPy
to "sum along axis 0," "axis 1," or "axis 2." 

This single idea —
**collapsing one axis while keeping the others** — is the same idea behind
almost every "reduce this data down" operation you'll later use in NumPy
and pandas (totals, averages, counts, and so on).

> **Glossary of common terms**
> - **Dimension / axis** — a "direction" along which an array's data is
>   arranged. A 2D array has 2 axes (rows and columns); a 3D array has 3
>   axes. See the [NumPy guide to array basics](https://numpy.org/doc/stable/user/absolute_beginners.html#understanding-data-types).
> - **Shape** — a tuple telling you the array's size along each axis, e.g.
>   `(2, 2, 2)` means "2 along axis 0, 2 along axis 1, 2 along axis 2."
> - **`sum(axis=...)`** — adds up values *along* the axis you specify,
>   effectively collapsing (removing) that axis from the result. Explained
>   step by step below.
> - **Collapsing an axis** — the everyday way to describe what
>   `sum(axis=...)` (or `mean()`, `max()`, etc.) does: that axis
>   "disappears" from the result's shape because its values have been
>   combined into one.

---

## Objective

To understand:

- The structure of 3D arrays
- The meaning of axes (`0`, `1`, `2`)
- How `sum(axis=...)` works
- How multi-dimensional data is reduced

---

# PART A — CONCEPTUAL STUDY

## Study Questions


1. What is the shape of a 3D array?
2. What do the three indices represent?
3. What do the three indices represent?
4. What does each axis correspond to?
5. What does it mean to "collapse an axis"?

> **Note:** questions 2 and 3 in the printed book both ask "What do the
> three indices represent?" — that repetition is preserved above exactly
> as printed, rather than silently corrected, since the original questions
> can't be changed. Question 4 below treats it as a single question and
> answers it once.

### Suggested answers:

**1. What is the shape of a 3D array?**

A 3D array's shape is a tuple of **three numbers**, written as
`(depth, rows, columns)`. For example, a shape of `(2, 2, 2)` means: 2
separate 2×2 grids, stacked one behind another. You can check any array's
shape at any time with `arr.shape`.

**2–3. What do the three indices represent?**

Each element in a 3D array is located using **three index numbers**,
written `arr[i, j, k]`:

| Index | Common name in this project | What it selects |
| --- | --- | --- |
| `i` (1st index) | Layer / depth | *Which* 2D grid (layer) you're looking at |
| `j` (2nd index) | Row | *Which row* within that layer |
| `k` (3rd index) | Column | *Which column* within that row |

So `arr[1, 0, 1]` means: "go to layer `1`, then row `0` within that layer,
then column `1` within that row."

**4. What does each axis correspond to?**

An **axis** is simply the direction associated with one of those indices.
For a 3D array shaped `(layers, rows, columns)`:

| Axis | Direction it moves along | Colloquially |
| --- | --- | --- |
| `axis=0` | Between layers | "Depth" — moving from one layer to the next |
| `axis=1` | Between rows, within a layer | "Down" — moving from one row to the next |
| `axis=2` | Between columns, within a row | "Across" — moving from one column to the next |

**5. What does it mean to "collapse an axis"?**

When you run an operation like `arr.sum(axis=0)`, NumPy combines
(adds together, in this case) every value **along** axis 0, and that axis
disappears from the resulting shape — it has been "collapsed" into a
single combined value at each remaining position. This is exactly why
summing a `(2, 2, 2)` array along `axis=0` leaves you with a `(2, 2)`
result: one dimension has been removed, and the other two survive
unchanged.

![Flowchart](/resources/ch-11-numpy-august-2026-3D-arrays-axis-ops.png)

---

# Visualizing a 3D Array

Given a 3D array:

```python
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
```

### Its shape = `(2, 2, 2)`

Read as: **2 layers**, each with **2 rows**, each row having **2
columns**.

---

## There are several ways to picture the same array

### Representation 1: Two stacked layers

```
Layer 0:
[[1 2]
 [3 4]]

Layer 1:
[[5 6]
 [7 8]]
```

![Flowchart](/resources/ch-11-numpy-august-2026-3D-arrays-2.png)



### Representation 2: Indexed view — `arr[i, j, k]`

```
arr[0,0,0] = 1   arr[0,0,1] = 2
arr[0,1,0] = 3   arr[0,1,1] = 4

arr[1,0,0] = 5   arr[1,0,1] = 6
arr[1,1,0] = 7   arr[1,1,1] = 8
```

### Representation 3: Coordinates → value

```
(0,0,0) → 1
(1,1,1) → 8
```

**Beginner tip:** all three representations above describe the *exact same
array* — they're just different ways of looking at it. If you can
translate confidently between "layer 0, row 1, column 0" and `arr[0,1,0]`
and "the value `3`," you've understood the core idea behind 3D indexing.

---

## Part B: Task



Write a script that:

1. Creates the 3D array
2. Displays it in multiple forms
3. Computes:
   - `sum(axis=0)`
   - `sum(axis=1)`
   - `sum(axis=2)`
4. Explains each result

### HINTS

- Use loops to print layers
- Print shapes after each operation
- Compare results carefully

---

## Script

Every stage of the script below is labelled with a `# Step N -` comment,
matching the four-part task above, so you can follow along without losing
your place. 
Comments have also been added inline for easy understanding of the script.

```python
# 3D Array Axis Exploration
import numpy as np

# Step 1 - Create the array, and think of it as 2 "layers" of 2x2 grids.
arr = np.array([
    [   # Layer 0
        [1, 2],
        [3, 4]
    ],
    [   # Layer 1
        [5, 6],
        [7, 8]
    ]
])

print("Array shape:", arr.shape)   # (2, 2, 2) -> 2 layers, each 2 rows x 2 columns
print("Array:->\n", arr)
# Output:
# Array:->
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]


# Step 2 - Display the array one layer at a time.
# arr[0] gives the whole first layer as a 2x2 grid, arr[1] gives the second.
for i in range(arr.shape[0]):
    print(f"\nLayer-> {i}:\n", arr[i])
# Output:
# Layer-> 0:
# [[1 2]
#  [3 4]]
# Layer-> 1:
# [[5 6]
#  [7 8]]


# Step 3 - Sum along axis=0: this COLLAPSES THE LAYERS, adding
# corresponding positions from Layer 0 and Layer 1 together.
# Explanation, position by position:
#   sum0[0,0] = arr[0,0,0] + arr[1,0,0] = 1 + 5 = 6
#   sum0[0,1] = arr[0,0,1] + arr[1,0,1] = 2 + 6 = 8
#   sum0[1,0] = arr[0,1,0] + arr[1,1,0] = 3 + 7 = 10
#   sum0[1,1] = arr[0,1,1] + arr[1,1,1] = 4 + 8 = 12
sum0 = arr.sum(axis=0)
print("\nSum axis=0 (collapses layers), shape", sum0.shape, ":\n", sum0)
# Output:
# [[ 6  8]
#  [10 12]]


# Step 4 - Sum along axis=1: this COLLAPSES THE ROWS within each layer,
# adding each layer's row 0 and row 1 together, column by column.
# Explanation, position by position:
#   Layer 0, column 0: sum1[0,0] = arr[0,0,0] + arr[0,1,0] = 1 + 3 = 4
#   Layer 0, column 1: sum1[0,1] = arr[0,0,1] + arr[0,1,1] = 2 + 4 = 6
#   Layer 1, column 0: sum1[1,0] = arr[1,0,0] + arr[1,1,0] = 5 + 7 = 12
#   Layer 1, column 1: sum1[1,1] = arr[1,0,1] + arr[1,1,1] = 6 + 8 = 14
sum1 = arr.sum(axis=1)
print("\nSum axis=1 (collapses rows), shape", sum1.shape, ":\n", sum1)
# Output:
# [[ 4  6]
#  [12 14]]


# Step 5 - Sum along axis=2: this COLLAPSES THE COLUMNS within each row,
# adding each row's two values together.
# Explanation, position by position:
#   Layer 0, row 0: sum2[0,0] = arr[0,0,0] + arr[0,0,1] = 1 + 2 = 3
#   Layer 0, row 1: sum2[0,1] = arr[0,1,0] + arr[0,1,1] = 3 + 4 = 7
#   Layer 1, row 0: sum2[1,0] = arr[1,0,0] + arr[1,0,1] = 5 + 6 = 11
#   Layer 1, row 1: sum2[1,1] = arr[1,1,0] + arr[1,1,1] = 7 + 8 = 15
sum2 = arr.sum(axis=2)
print("\nSum axis=2 (collapses columns), shape", sum2.shape, ":\n", sum2)
# Output:
# [[ 3  7]
#  [11 15]]


# Step 6 - Overall conclusion, printed as a quick reference.
print("\nSummary:")
print("axis=0 -> combines LAYERS  (depth disappears from the result)")
print("axis=1 -> combines ROWS    (row dimension disappears from the result)")
print("axis=2 -> combines COLUMNS (column dimension disappears from the result)")
```

---

## Summary table: what each axis collapses

| `axis=` value | What gets combined | What survives in the result | Result shape (from this example) |
| --- | --- | --- | --- |
| `0` | Values across **layers** | Rows and columns | `(2, 2)` |
| `1` | Values across **rows**, within each layer | Layers and columns | `(2, 2)` |
| `2` | Values across **columns**, within each row | Layers and rows | `(2, 2)` |

**Beginner tip:** a quick way to sanity-check any `axis=` result is to
count the dimensions. The original array had 3 dimensions (shape length 3);
after summing along any single axis, exactly **one** dimension disappears,
so the result always has 2 dimensions in this example — never zero, and
never three.

---

## Follow-up questions for practice

*(These are additional, optional questions for self-testing)

1. What would `arr.sum(axis=0).sum(axis=0)` give you — i.e. collapsing
   axis 0 twice in a row? What single number do you expect, and why?
2. If you called `arr.sum()` with **no** `axis` argument at all, what do
   you think happens, and what shape would the result have? Try it and
   check.
3. Extend the array to 3 layers instead of 2 (you'll need to add a third
   2×2 grid, and the array's shape will become `(3, 2, 2)`). Which
   `sum(axis=...)` calls change shape as a result, and which stay the
   same?
4. Using `arr.mean(axis=1)` instead of `arr.sum(axis=1)`, work out by hand
   what you'd expect the result to be for this project's original array,
   then confirm it with code.






