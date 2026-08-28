


# Chapter 11 — Project: Matrix–Vector Multiplication as Transformations

## About this chapter

This project is the hands-on companion to the previous chapter's matrix
theory: instead of studying the mathematics of scaling, reflection, and
rotation formula by formula, this project builds **one single script**
that applies every transformation to the same starting vector, so you can
compare all of them side by side and see the pattern that connects them.

The core idea worth carrying forward from this project: **every one of
these different-looking transformations — stretching, flipping, turning —
is really just `matrix @ vector`.** The only thing that changes between
them is *which numbers* go into the matrix. Once that clicks, scaling,
reflection, and rotation stop feeling like three separate topics to
memorise, and start feeling like three examples of the same underlying
operation.

> **Glossary of terms**
> - **Vector** — an ordered list of numbers; here, a simple 2D point like `[1, 2]`.
> - **Matrix** — a rectangular grid of numbers, used here to transform a vector when multiplied against it.
> - **Diagonal matrix** — a matrix whose only non-zero values sit along its main diagonal; the basis for every scaling matrix in this project.
> - **Transformation** — the general term for what happens when a matrix changes a vector's values (and sometimes its dimensions) through multiplication.
> - **`@` operator** — NumPy's operator for genuine matrix multiplication (as opposed to `*`, which multiplies element-by-element). See the [NumPy matmul documentation](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html).

---

## Objective



To explore how matrix–vector multiplication:

- transforms vectors
- performs scaling, reflection, rotation
- is used in data science and ML

---

## PART A — Research Questions



### Conceptual

1. What is a vector in NumPy?
2. What happens when a matrix multiplies a vector?
3. Why is matrix multiplication called a "transformation"?
4. What is a diagonal matrix and how does it affect a vector?
5. How do matrices represent:
   - scaling
   - reflection
   - rotation

### Suggested answers

**1. What is a vector in NumPy?**

In NumPy, a vector is simply a 1D array — a flat sequence of numbers, such
as `np.array([1, 2])`. Mathematically, it's usually *interpreted* as a
column of values (see the previous chapter's discussion of row vs. column
vectors), but as plain NumPy code, it's stored as a flat array with shape
`(n,)`.

**2. What happens when a matrix multiplies a vector?**

The matrix transforms the vector into a **new** vector, following the
rule `y = M @ x`. Every value in the resulting vector `y` is a weighted
combination of the *original* vector's values, where the weights come from
the matrix's rows. The practical effect (stretching, flipping, rotating,
or some mix of these) depends entirely on which numbers are inside the
matrix.

**3. Why is matrix multiplication called a "transformation"?**

Because it takes an existing vector and turns it into a genuinely new one
— not just tweaking its values, but potentially also changing its
dimensions (see the shape rule in the Solution section below). "Transform"
captures both of these possibilities at once: values changing, and
dimensions changing.

**4. What is a diagonal matrix, and how does it affect a vector?**

A diagonal matrix has non-zero values *only* along its main diagonal
(top-left to bottom-right) — everywhere else is zero. When such a matrix
multiplies a vector, each component of the vector is scaled **entirely
independently** by its own diagonal value, with zero "cross-talk" between
components. This is exactly what makes diagonal matrices the natural tool
for scaling (Sections further below).

**5. How do matrices represent scaling, reflection, and rotation?**

| Transformation | How the matrix encodes it |
| --- | --- |
| Scaling | A diagonal matrix, where each diagonal value is the stretch/shrink factor for that axis |
| Reflection | A matrix with `1`s and `-1`s placed to flip the sign of one or more coordinates (or swap them) |
| Rotation | A matrix built from `sin` and `cos` of the rotation angle, arranged in a specific pattern that preserves the vector's length while changing its direction |

---

## Part B — Task



Write a script that:

1. Defines a vector
2. Applies:
   - scaling
   - non-uniform scaling
   - reflection
   - rotation
3. Prints results clearly
4. Explains transformation

### HINTS

- Use the `@` operator
- Use small vectors (2D)
- Compare input vs. output

---

## Solution (Explanation)

### What's actually happening when we multiply?

Suppose we have a 2D matrix $M$ of dimensions $m \times n$, and a vector
$x$ of dimension $n \times 1$.

**Key rules to remember:**

- Multiplication between $M$ and $x$ is only possible if the number of
  **columns** in $M$ matches the number of **rows** in $x$.
- When we compute $y = Mx$, the result $y$ will have dimensions
  $m \times 1$.
- So: multiplying a matrix of dimensions $m \times n$ by a vector of
  dimensions $n \times 1$ produces a **new** vector $y$ of dimensions
  $m \times 1$.


```

![Flowchart](/resources/ch-11-numpy-august-2026-vector-matrices-02.png)


**The important insight:** matrix-to-vector multiplication doesn't just
change the *individual values* in the vector — it can also change the
vector's *dimensions* entirely (if $m \ne n$). Every matrix therefore does
two things at once: (1) it changes the vector's contents, and (2) it
produces a genuinely new vector. This combined change is exactly what's
meant by calling it a **transformation**.

**A practical note for this project's script:** every matrix used below is
square ($2 \times 2$), and the vector is $2 \times 1$ (well, `(2,)` as a
plain NumPy array) — so in every case here, $m = n = 2$, and the *shape*
of the vector never changes, only its values. You'll see matrices that
*do* change a vector's dimensions later on in this book.

---

## Types of Transformations

Having understood what a transformation is, we can look at the specific
types of transformation a matrix can apply to a vector:

| Type | Matrix form | Effect |
| --- | --- | --- |
| Scaling | Diagonal | Stretch or shrink |
| Reflection | Special `1`/`-1` pattern | Flip direction |
| Rotation | Trigonometric (`sin`/`cos`) | Rotate the vector |

For a $2 \times 2$ matrix specifically, here are the common transformations
this project's script will demonstrate:

| Operation | Matrix | Effect |
| --- | --- | --- |
| Uniform scaling | `[[k, 0], [0, k]]` | Stretch equally on both axes |
| Non-uniform scaling | `[[a, 0], [0, b]]` | Stretch differently on each axis |
| Reflection (X-axis) | `[[1, 0], [0, -1]]` | Flip vertically |
| Reflection (Y-axis) | `[[-1, 0], [0, 1]]` | Flip horizontally |
| Rotation | `[[cos θ, -sin θ], [sin θ, cos θ]]` | Rotate by angle θ |

---

## Script

The following script demonstrates every transformation above, applied to
the *same* starting vector, so the results are directly comparable.

```python
# Matrix-Vector Transformations in NumPy
import numpy as np

# ---------------------------------------------------
# Step 1 - Define the vector we'll transform throughout this script.
# Kept as a plain 1D array (shape (2,)) rather than reshaped to (2, 1) —
# NumPy's @ operator automatically treats a 1D array as a column vector
# when multiplying it against a 2D matrix, so this works correctly, and
# the result also comes back as a plain 1D array for easy printing.
# ---------------------------------------------------
x = np.array([1, 2])
print("Original vector:", x)   # Output: [1 2]


# ---------------------------------------------------
# Step 2 - Uniform scaling.
# M1 is a diagonal matrix with the SAME scaling factor (3) on both
# diagonal positions, so it stretches both the x and y components
# equally when multiplied against the vector.
# ---------------------------------------------------
M1 = np.array([[3, 0],
               [0, 3]])

y1 = M1 @ x
print("\nUniform scaling (x3):", y1)   # [3, 6]


# ---------------------------------------------------
# Step 3 - Non-uniform scaling.
# M2 is a diagonal matrix with DIFFERENT scaling factors on each
# diagonal position, so it stretches the x-component by 3 and the
# y-component by 5 — an unequal stretch along each axis.
# ---------------------------------------------------
M2 = np.array([[3, 0],
               [0, 5]])

y2 = M2 @ x
print("\nNon-uniform scaling:", y2)   # [3, 10]


# ---------------------------------------------------
# Step 4 - Reflection about the X-axis.
# M3 leaves the x-component untouched but inverts the sign of the
# y-component, which is exactly what reflecting across the X-axis means.
# ---------------------------------------------------
M3 = np.array([[1, 0],
               [0, -1]])

y3 = M3 @ x
print("\nReflection about X-axis:", y3)   # [1, -2]


# ---------------------------------------------------
# Step 5 - Reflection about the Y-axis.
# M4 leaves the y-component untouched but inverts the sign of the
# x-component, reflecting the vector across the Y-axis instead.
# ---------------------------------------------------
M4 = np.array([[-1, 0],
               [0, 1]])

y4 = M4 @ x
print("\nReflection about Y-axis:", y4)   # [-1, 2]


# ---------------------------------------------------
# Step 6 - Rotation by 90 degrees.
# np.pi / 2 radians = 90 degrees (NumPy's trig functions expect radians,
# not degrees). M5 is built from cos(theta) and sin(theta), arranged in
# the standard rotation-matrix pattern, and rotates the vector 90
# degrees counter-clockwise while preserving its length.
# ---------------------------------------------------
theta = np.pi / 2

M5 = np.array([[np.cos(theta), -np.sin(theta)],
               [np.sin(theta),  np.cos(theta)]])

y5 = M5 @ x
print("\nRotation (90 degrees):", y5)   # approx [-2, 1]


# ---------------------------------------------------
# Interpretation
# ---------------------------------------------------
# Every matrix above changed the SAME starting vector x differently,
# depending only on the numbers inside that matrix.
# -> This act of a matrix changing a vector is called a TRANSFORMATION.
```

**Beginner tip:** the rotation result prints as *approximately*
`[-2, 1]`, not exactly — this is completely normal. `np.cos(np.pi / 2)`
doesn't come out to exactly `0` due to how computers represent decimal
numbers internally (it's an extremely small number very close to zero
instead). If you want a tidier printout, wrap the result in
`np.round(y5, 4)`.

---

## The following figures show the transformation of a 2D vector by a 2×2 matrix

### Uniform scaling

![Uniform Scaling](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-uniform-scaling-matrix-vector.png)

### Non-uniform scaling

![Non-Uniform scaling](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-non-uniform-scaling-matrix-vector.png)

### Reflection on X-axis

![Reflection on X axis](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-reflection-x-axis-matrix-vector.png)

### Reflection on Y-axis

![Reflection on Y-axis](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-reflection-y-axis-matrix-vector.png)

### Rotation by 90 degrees

![Rotation by 90 degrees](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-rotation-90-matrix-vector.png)

> **Note:** the "Reflection on X-axis" image link had a small Markdown
> syntax error in the original (`![...[(url)` instead of `![...](url)`),
> which would have prevented that image from displaying. It's corrected
> above.

---

## Summary

| Question | Short answer |
| --- | --- |
| What does `matrix @ vector` do? | Produces a new vector, whose values (and possibly dimensions) depend entirely on the matrix |
| What makes a matrix a "scaler"? | It's diagonal, with each diagonal value being that axis's stretch factor |
| What makes a matrix a "reflector"? | `1`s and `-1`s placed to flip or swap coordinates |
| What makes a matrix a "rotator"? | Built from `sin`/`cos` of the rotation angle, arranged in the standard rotation pattern |
| Why compare all four in one script? | It makes clear that they're all the *same* operation (`@`) — only the matrix's contents differ |

---

## Follow-up questions for practice

*(These are additional, optional questions for self-testing — they don't
replace or change the original research questions or task above.)*

1. Apply **two** transformations to `x` in a row — for example, scale it
   with `M1`, then rotate the *result* with `M5`. Does doing it as
   `M5 @ (M1 @ x)` give the same answer as combining the matrices first,
   `(M5 @ M1) @ x`?
2. What matrix would you need to reflect a vector across **both** axes at
   once (i.e. `(x, y)` becomes `(-x, -y)`)? Build it and test it against
   the vector `[1, 2]` used in this script.
3. The uniform scaling matrix `M1` used a factor of `3` for both axes.
   What would the matrix — and the result — look like for a *shrinking*
   transformation, using a factor of `0.5` instead?
4. Using `np.round(y5, 4)` as suggested in the beginner tip, confirm that
   the 90-degree rotation result is genuinely `[-2, 1]` rather than
   something like `[-2.0000000001, 1.0]`. Why does floating-point
   arithmetic produce that tiny discrepancy in the first place?





