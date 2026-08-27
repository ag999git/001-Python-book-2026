


# Chapter 11 — Broadcasting in NumPy

## About this chapter

So far, adding two arrays together has probably meant adding two arrays of
the **same shape** — element matched to element. **Broadcasting** is the
NumPy feature that lets you go further: it allows arrays of *different*
shapes to be combined in arithmetic, by automatically "stretching" the
smaller one to match the larger one, without you writing a single loop.

This matters far beyond convenience. Broadcasting is:

- **Fast** — the stretching happens inside NumPy's optimized C code, not in
  a slow Python loop.
- **Memory-efficient** — as you'll see in Rule 4 below, NumPy doesn't
  actually duplicate the smaller array's data in memory; it reuses it
  cleverly.
- **Everywhere** — once you start using NumPy (and, later, pandas) for real
  data work, you will be relying on broadcasting constantly, often without
  even noticing — for example, subtracting the average of a column from
  every row in a table.

This chapter builds the idea up in stages: first a few concrete examples,
then the exact rules NumPy follows to decide whether two shapes are
compatible, and finally a reference table you can return to whenever
you're unsure if a particular combination of shapes will work.

> **Quick glossary, before we start**
> - **Scalar** — a single plain number, like `10`, as opposed to an array
>   of numbers.
> - **Shape** — a tuple describing an array's size along each dimension,
>   e.g. `(3, 4)` means 3 rows and 4 columns.
> - **Dimension / axis** — one "direction" of an array's shape; a `(3, 4)`
>   array has 2 dimensions (also called axes).
> - **Vectorized operation** — doing maths on a whole array at once,
>   instead of looping over it one value at a time.
> - **Stride** — an internal, low-level detail of how NumPy steps through
>   memory to read an array's values; mentioned here only to explain *why*
>   broadcasting is memory-efficient (Rule 4). See the
>   [NumPy internals guide](https://numpy.org/doc/stable/reference/arrays.ndarray.html#internal-memory-layout-of-an-ndarray)
>   if you want the full technical detail.

---

## What is broadcasting, in plain terms?

**Broadcasting** is the set of rules NumPy uses to figure out how to
combine two arrays of *different* shapes in an arithmetic operation (like
`+`, `-`, `*`, `/`), by automatically expanding the smaller one so both
sides line up.

The script below shows three increasingly interesting cases: a single
number, a row of numbers, and a column of numbers, each combined with a
full matrix.

```python
import numpy as np

# Step 1 - Broadcasting with a SCALAR (a single plain number).
# NumPy expands 10 into [10, 10, 10] behind the scenes, then adds
# element-by-element. You never see that expanded array — it's implicit.
arr = np.array([1, 2, 3])
result = arr + 10
print(result)   # Output: [11 12 13]

# Step 2 - Broadcasting a MATRIX with a ROW VECTOR.
# matrix has shape (3, 3); row_vector has shape (3,).
# NumPy "stretches" the row vector down, applying it to every row of the matrix.
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
row_vector = np.array([10, 20, 30])
result3 = matrix + row_vector
print(result3)
# Output:
# [[11 22 33]
#  [14 25 36]
#  [17 28 39]]

# Step 3 - Broadcasting a MATRIX with a COLUMN VECTOR.
# column_vector has shape (3, 1); matrix has shape (3, 3).
# NumPy "stretches" the column vector across, applying it to every column.
column_vector = np.array([
    [10],
    [20],
    [30]
])
result4 = matrix + column_vector
print(result4)
# Output:
# [[11 12 13]
#  [24 25 26]
#  [37 38 39]]
```

**In short:** NumPy broadcasts a row vector by conceptually adding more
*rows* to match the matrix, and broadcasts a column vector by conceptually
adding more *columns* — in both cases, only enough to make the shapes line
up, and (as you'll see in Rule 4) without actually copying any extra data
in memory.

### The following figure shows how broadcasting was done on a scalar in the script above:


![Broadcasting of a scalar](/resources/ch11-broadcast-scalar.png)

### The following figure shows how broadcasting was done on a row vector in the above script



![Broadcasting a row vector](/resources/ch11-broadcast-row-vector.png)

### The following figure shows how broadcasting was done on a column vector in the above script



![Broadcasting Column Vector](/resources/ch11-broadcast-column-vector.png)


---

## The Master Flowchart: How NumPy Decides

Before diving into the detailed rules, look at this decision process. Every
time you write `A + B` in NumPy, this is effectively the logic the engine
runs through.

![Broadcasting Decision Tree](/resources/ch11-broadcast-rule-flowchart.png)


Here's the same logic as a Mermaid flowchart, for quick reference or
editing:

```mermaid
flowchart TD
    A[Compare shapes of A and B] --> B{Do they have the<br/>same number of dimensions?}
    B -->|No| C[Pad the shorter shape<br/>with 1s on the LEFT]
    B -->|Yes| D[Compare dimensions,<br/>right to left]
    C --> D
    D --> E{For each pair of dimensions:<br/>equal, or one of them is 1?}
    E -->|Yes, all pairs OK| F[Stretch every dimension<br/>that is 1 to match the other]
    E -->|No, some pair mismatches| G[Raise ValueError:<br/>shapes cannot be broadcast]
    F --> H[Operation proceeds on<br/>the resulting matched shape]
```

*(Plain boxes, one diamond shape per decision, and arrows only — no
subgraphs — so this should import cleanly into
[draw.io](https://app.diagrams.net/) as well as render on GitHub/GitBook.)*

---

## Rule 1: Right-Alignment and Left-Padding (The Prepend Rule)

**The rule:** When comparing two array shapes, NumPy lines them up starting
from the **right-most (trailing) dimension** and works its way left. If one
array has fewer dimensions than the other, the *missing* dimensions on the
left are treated as if they were `1`.

**In plain terms:** it's like aligning numbers in school arithmetic — you
line up the ones column on the right, and pad a shorter number with zeros
on the left. NumPy does the same thing, but pads with `1`s instead of
zeros.

**Worked example:**

**Step 1 — the starting shapes**
- Array A shape: `(8, 1, 6, 1)` — 4 dimensions
- Array B shape: `(7, 1, 5)` — 3 dimensions

**Step 2 — pad the shorter shape on the left**

NumPy compares from the right: `1` vs `5`, `6` vs `1`, `1` vs `7` — then it
runs out of dimensions on B's side, so it pads B with a `1` at the front.

- Effective shape A: `(8, 1, 6, 1)`
- Effective shape B: `(1, 7, 1, 5)` *(the leading `1` was added by padding)*

**Step 3 — stretch every dimension that's `1`**

- Effective shape A: `(8, 7, 6, 5)`
- Effective shape B: `(8, 7, 6, 5)`

Both shapes now match exactly, so the arithmetic operation can proceed.

```mermaid
flowchart TD
    A1["A: (8, 1, 6, 1)"] --> S1["Step 2: pad B on the left with 1<br/>B becomes (1, 7, 1, 5)"]
    B1["B: (7, 1, 5)"] --> S1
    S1 --> S2["Step 3: stretch every dimension that is 1"]
    S2 --> R["Both shapes end up as (8, 7, 6, 5)<br/>Operation can proceed"]
```

### The following figure shows the steps in broadcasting of Array A shape `(8, 1, 6, 1)` and Array B shape `(7, 1, 5)`


![Flow chart showing broadcasting of A (8,1,6,1) and B (7,1,5)](/resources/ch11-broadcast-2-matrices-different-dimensions.png)


**Do's and don'ts:**

- **DO** rely on this rule for adding a 1D vector to a 2D matrix: `(3, 4) + (4,)` becomes `(3, 4) + (1, 4)`.
- **DON'T** assume padding happens on the *right*. `(3,) + (3, 4)` will **fail** — B is not silently padded to `(3, 4, 1)`; instead, A is padded to `(1, 3)`, which then clashes with B's trailing `4`.

---

## Rule 2: The "One or Equal" Rule (The Stretching Rule)

**The rule:** Two dimensions are compatible for broadcasting if they are
**exactly equal**, or if **one of them is exactly `1`**.

**In plain terms:** if you're comparing a dimension of size `5` with
another dimension of size `5`, they already match — nothing needs to
change. If you're comparing a dimension of size `1` against size `5`,
NumPy can stretch that single `1` to size `5` to make it fit.

**Examples:**

- Comparing `1` vs `4` → **Compatible.** The `1` stretches to `4`.
- Comparing `6` vs `6` → **Compatible.** They're already identical.
- Comparing `3` vs `4` → **Incompatible.** (See Rule 3, next.)

**Do's and don'ts:**

- **DO** use a shape like `(3, 1)` to apply an operation across every column of a `(3, 4)` matrix — the `1` stretches to `4`.
- **DON'T** forget that the *result's* shape takes the larger of the two dimensions being compared. `(5, 1) + (1, 5)` produces a `(5, 5)` result — not `(1, 1)`.

---

## Rule 3: The Incompatibility Error (The Failure Rule)

**The rule:** If two dimensions are **not equal**, and **neither one is
`1`**, broadcasting is impossible, and NumPy raises
`ValueError: operands could not be broadcast together`.

**In plain terms:** if you have a box of size `3` and a box of size `4`,
NumPy won't guess how to force them together. It won't stretch `3` up to
`4` (that would invent data that was never there) and it won't cut `4`
down to `3` (that would silently throw data away).

**Example:**

```python
import numpy as np

A = np.zeros((3, 4))
B = np.zeros((4, 3))
print(A + B)
# ValueError: operands could not be broadcast together with shapes (3,4) (4,3)
```

Right-alignment here compares `4` (A's last dimension) against `3` (B's
last dimension). Neither is `1`, and they aren't equal — so NumPy raises
the error immediately, before doing any calculation.

**Do's and don'ts:**

- **DO** use `.reshape()` or `.T` (transpose) to fix a mismatched dimension order before adding two arrays.
- **DON'T** wrap the operation in `try/except` purely to hide the error — a broadcasting `ValueError` almost always means there's a genuine mistake in your data's shape or logic, and hiding it just delays finding that mistake.

---

## Rule 4: Virtual Stretching (The Memory Rule)

**The rule:** When one array has a dimension of size `1`, NumPy does
**not** physically copy its data in memory to match the larger array. It
is "virtually" stretched using an internal memory technique called
**strides** — essentially, NumPy just reuses (reads again) the same small
block of memory multiple times, rather than duplicating it.

**In plain terms:** if you broadcast a `(1, 1_000_000)` array against a
`(1000, 1_000_000)` array, NumPy does **not** create a new one-billion-cell
copy behind the scenes. It reuses the same million cells over and over,
via a clever pointer trick at the C level — saving an enormous amount of
memory.

**Example — proving no memory copy happens:**

```python
import numpy as np

# Step 1 - Set up two arrays of very different sizes.
A = np.ones((5, 4))          # 20 elements: 5 rows x 4 columns
B = np.array([1, 2, 3, 4])   # 4 elements

# Step 2 - Check how much memory each one uses BEFORE broadcasting.
# A: 5 x 4 x 8 bytes per float64 = 160 bytes (exact size depends on dtype)
# B: 4 x 8 bytes per int64 = 32 bytes (exact size depends on dtype)
print(f"A size: {A.nbytes} bytes")
print(f"B size: {B.nbytes} bytes")

# Step 3 - Perform the broadcasted addition.
# NumPy does NOT create a (5, 4) copy of B to match A's shape — it reuses
# B's original 4 values, one row of A at a time, via internal "strides."
C = A + B

# Step 4 - Confirm the result's memory matches what a genuine (5, 4)
# array would need — proving no separate, duplicated copy of B was made.
print(f"Result C size: {C.nbytes} bytes")
```

This is a direct demonstration of why broadcasting is so efficient: the
memory used by the *operation* stays close to the memory used by the two
*original* arrays, not the memory a fully-expanded copy would need.

### Step-by-step: what happens under the hood

**1. Understanding the shapes**

- **Array A** has shape `(5, 4)` — a 2D matrix, 5 rows and 4 columns, filled with `1`.
- **Array B** has shape `(4,)` — a 1D vector with 4 elements: `[1, 2, 3, 4]`.

**2. Applying the broadcasting rule**

Comparing from the **right-most** dimension:

- **Columns:** A has 4, B has 4 — they match, so this is fine.
- **Rows:** A has 5, B effectively has none (treated as `1` after left-padding).

To make the shapes line up, NumPy conceptually stretches B down across 5
rows.

**3. The maths, conceptually**

```
Array A (5x4):                Array B (conceptually stretched to 5x4):
[[1, 1, 1, 1],                [[1, 2, 3, 4],
 [1, 1, 1, 1],                 [1, 2, 3, 4],
 [1, 1, 1, 1],       +         [1, 2, 3, 4],
 [1, 1, 1, 1],                 [1, 2, 3, 4],
 [1, 1, 1, 1]]                 [1, 2, 3, 4]]

Result C (5x4):
[[2, 3, 4, 5],
 [2, 3, 4, 5],
 [2, 3, 4, 5],
 [2, 3, 4, 5],
 [2, 3, 4, 5]]
```

**4. The memory trick behind the maths**

If you were doing this by hand in ordinary Python, you'd likely build the
full `(5, 4)` copy of B before adding it — genuinely duplicating that data
in memory. **NumPy skips this step entirely.** Using strides, it reads B's
original 4 values again for each of A's 5 rows, without ever allocating a
second, expanded copy. In short: NumPy uses roughly `160 + 32` bytes here,
not `160 + 160`.

**Do's and don'ts:**

- **DO** use broadcasting confidently, even on very large arrays — it won't blow up your memory usage the way a manual "expand, then add" approach would.
- **DON'T** manually call `np.tile()` or `np.repeat()` just to force two arrays to the same shape before adding them — doing so defeats the entire memory-saving point of broadcasting.

---

## Master Comparison Table: Shapes and Results

This table shows the broadcasting outcomes you'll run into most often.

| Array A shape | Array B shape | Compatible? | Reasoning | Final output shape |
| --- | --- | --- | --- | --- |
| `(5, 4)` | `(4,)` | Yes | B is padded to `(1, 4)`; the `1` stretches to `5` | `(5, 4)` |
| `(5, 4)` | `(5, 1)` | Yes | The `1` in B stretches to `4` | `(5, 4)` |
| `(5, 4)` | `(1, 4)` | Yes | The `1` in B stretches to `5` | `(5, 4)` |
| `(5, 1, 4)` | `(1, 4)` | Yes | B is padded to `(1, 1, 4)`; both `1`s stretch | `(5, 1, 4)` |
| `(5, 4, 1)` | `(4, 1)` | Yes | B is padded to `(1, 4, 1)`; both `1`s stretch | `(5, 4, 1)` |
| `(5,)` | `(5, 4)` | No | A is padded to `(1, 5)`; comparing `5` vs `4` fails | `ValueError` |
| `(3, 4)` | `(4, 3)` | No | Comparing `4` vs `3` fails | `ValueError` |

**Beginner tip:** when in doubt, work through the table's "Reasoning"
column yourself, one dimension at a time, starting from the right — it's
exactly the same right-to-left comparison process described in Rule 1, and
it's a habit worth building rather than memorising the table by rote.

---

## Summary

| Rule | One-line takeaway |
| --- | --- |
| Rule 1 — Prepend | Shapes are compared right to left; a shorter shape is padded with `1`s on the left |
| Rule 2 — One or Equal | Two dimensions can combine if they're equal, or if one of them is `1` |
| Rule 3 — Incompatibility | If dimensions differ and neither is `1`, NumPy raises a `ValueError` rather than guessing |
| Rule 4 — Virtual Stretching | A dimension of `1` is never physically copied — NumPy reuses the existing memory via strides |

---

## Follow-up questions for practice

*(These are additional, optional questions for self-testing.)*

1. Would `np.zeros((3, 1, 5)) + np.zeros((4, 5))` broadcast successfully?
   Work out the effective shapes by hand using Rule 1 before checking with
   code.
2. Using the Master Comparison Table as a model, predict the output shape
   (or error) for `(6, 1) + (1, 6)`, then verify it in code. Does the
   result surprise you?
3. In the Rule 4 memory example, what would you expect `C.nbytes` to equal
   if `A` had shape `(500, 4)` instead of `(5, 4)`? Would `B`'s memory
   usage change at all?
4. Rewrite the scalar-broadcasting example (`arr + 10`) using a manual
   `for` loop instead, to build the same `[11, 12, 13]` result without
   broadcasting. Which version is easier to read, and which would run
   faster on a very large array?






