

# Chapter 11 — Eigen Decomposition: A Detailed Guide

> *Note:* The topic of eigen decomposition may appear mathematical.
> However, it is essential for understanding advanced topics like
> Singular Value Decomposition (SVD). If you are not interested in SVD,
> you may skip this section.

## About this chapter

Eigen decomposition takes a single square matrix and rewrites it as three
simpler pieces multiplied together — a rotation, a scaling, and a reversal
of that same rotation. That might sound abstract, but it's one of the most
useful ideas in applied linear algebra: it's the mathematical foundation
behind Principal Component Analysis (PCA), a large part of how Singular
Value Decomposition works, and a common tool for analysing the stability
of systems in engineering and physics.

The original version of this chapter presented the theory on its own,
without any NumPy code. Since this is a *Python* book, this improved
version keeps every piece of the original mathematics exactly as written,
and adds a working NumPy script at the end — so the equations
$A\vec{v} = \lambda\vec{v}$ and $A = Q\Lambda Q^{-1}$ aren't just symbols on
a page, but things you can compute and verify for yourself in a few lines
of code.

> **Quick glossary, before we start**
> - **Eigenvector** — a special vector that a given matrix only *stretches
>   or shrinks*, without changing its direction, when multiplied against
>   it.
> - **Eigenvalue** — the number (usually written $\lambda$, the Greek
>   letter "lambda") by which that stretching or shrinking happens.
> - **Scalar** — a single plain number, as opposed to a vector or matrix.
> - **Diagonal matrix** — a matrix with non-zero values only along its main
>   diagonal; used here to hold all the eigenvalues together in one place.
> - **Invertible matrix** — a matrix that has a genuine "undo" matrix
>   (its inverse, $Q^{-1}$), such that multiplying the two together gives
>   back the identity matrix. See
>   [Khan Academy's introduction to matrix inverses](https://www.khanacademy.org/math/algebra-home/alg-matrices/alg-intro-to-matrix-inverses/a/intro-to-matrix-inverses).
> - **Decomposition** — breaking a single mathematical object down into a
>   product (or combination) of simpler pieces, the way this chapter breaks
>   a matrix $A$ into $Q$, $\Lambda$, and $Q^{-1}$.

---

## 1. The Core Concept

Previously, we established that if:

- $A$ is a square matrix
- $\vec{v}$ is a non-zero vector
- $\lambda$ is a scalar

then:

$$A\vec{v} = \lambda \vec{v}$$

### Interpretation

- The matrix $A$ acts on vector $\vec{v}$
- The result is a **scaled version of the same vector**

This means:

- The **direction remains unchanged**
- Only the **magnitude changes**, by a factor of $\lambda$.

```mermaid
flowchart LR
    A["Vector v"] --> B["Multiply by matrix A"]
    B --> C["Result: lambda * v<br/>SAME direction, scaled magnitude"]
```

*(Plain boxes and arrows only, no subgraphs, so every diagram in this
chapter should import cleanly into [draw.io](https://app.diagrams.net/) as
well as render on GitHub/GitBook.)*

**Beginner tip:** this is precisely what makes $\vec{v}$ special — for
*almost any* vector, multiplying it by a matrix $A$ changes its direction
as well as its length. An eigenvector is one of the rare vectors (for a
given matrix) where the direction is left completely untouched.

---

### Cases of Eigenvalues

| Condition | Meaning |
| --- | --- |
| $\lambda = 1$ | Vector remains unchanged |
| $\lambda > 1$ | Vector is stretched |
| $0 < \lambda < 1$ | Vector is compressed |
| $\lambda < 0$ | Direction is reversed |

---

## 2. The Logic Behind Decomposition

Why do we decompose a matrix?

The logic is similar to how a machine works by taking it apart into its
components. It is just like breaking a machine into parts to understand
it.

**A little more context on *why* this is worth doing:** once a matrix is
broken into its eigenvalues and eigenvectors, many operations that are
difficult or slow on the original matrix become dramatically simpler on
the decomposed pieces — for example, raising a matrix to a large power, or
understanding how a system behaves after many repeated transformations.
This is also the mathematical basis for **Principal Component Analysis
(PCA)**, a widely used technique for reducing the number of variables in a
dataset while keeping as much meaningful information as possible.

---

### Step 1: Eigenvalues and Eigenvectors

For a matrix $A$ of dimensions $n \times n$:

- Suppose the eigenvalues are:
  $$\lambda_1, \lambda_2, \dots, \lambda_n$$
- And the corresponding eigenvectors are:
  $$\vec{v_1}, \vec{v_2}, \dots, \vec{v_n}$$

---

### Step 2: Construct Matrix $Q$

We can arrange the eigenvectors as columns into a matrix $Q$:

$$Q = [\vec{v_1} \quad \vec{v_2} \quad \dots \quad \vec{v_n}]$$

**Columns are eigenvectors.**

---

### Step 3: Construct Diagonal Matrix $\Lambda$

Next, we arrange the eigenvalues into a diagonal matrix $\Lambda$
(the capital Greek letter "lambda"):

$$\Lambda = \begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{bmatrix}$$

---

### Step 4: Key Equation

Using the definition $A\vec{v} = \lambda \vec{v}$, we write a combined
matrix equation for all eigenvalues simultaneously:

$$AQ = Q\Lambda$$

If $Q$ is invertible:

$$A = Q \Lambda Q^{-1}$$

```mermaid
flowchart TD
    A1["Matrix A, shape (n,n)"] --> B1["Find eigenvalues: lambda1...lambdaN"]
    A1 --> B2["Find eigenvectors: v1...vN"]
    B1 --> C1["Arrange into diagonal matrix Lambda"]
    B2 --> C2["Arrange as columns into matrix Q"]
    C1 --> D["Combine: A = Q x Lambda x Q-inverse"]
    C2 --> D
```

---

### Interpretation

Eigen decomposition represents:

```text
A = Rotation → Scaling → Rotation back
```

**In plain terms:** $Q^{-1}$ first rotates (or more precisely, changes the
coordinate system of) a vector into the special "eigenvector-aligned"
view; $\Lambda$ then simply stretches or shrinks each coordinate
independently (exactly the diagonal-matrix scaling from earlier in this
chapter); and $Q$ rotates the result back into the original coordinate
system. The net effect of doing all three, in order, is mathematically
identical to just applying $A$ directly — decomposition doesn't change
*what* the matrix does, only reveals *how* it does it.

---

## 3. Turning This Into NumPy Code

NumPy's `np.linalg.eig()` function computes a matrix's eigenvalues and
eigenvectors directly, so you don't need to work them out by hand. The
script below uses it to verify every equation covered above, with the same
matrix throughout.

```python
import numpy as np

# ---------------------------------------------------
# Step 1 - Define a square matrix A to decompose.
# ---------------------------------------------------
A = np.array([
    [2, 1],
    [1, 2]
])
print("Matrix A:\n", A)


# ---------------------------------------------------
# Step 2 - Compute the eigenvalues and eigenvectors using NumPy.
# np.linalg.eig() returns two things:
#   eigenvalues  -> a 1D array, e.g. [lambda1, lambda2]
#   eigenvectors -> a 2D array whose COLUMNS are the eigenvectors,
#                   in the same order as the eigenvalues
# This eigenvectors array IS the matrix Q from the theory above.
# ---------------------------------------------------
eigenvalues, Q = np.linalg.eig(A)

print("\nEigenvalues (lambda1, lambda2):", eigenvalues)
print("\nEigenvector matrix Q (columns are eigenvectors):\n", Q)


# ---------------------------------------------------
# Step 3 - Verify A @ v = lambda * v for ONE eigenvector, to confirm
# what "eigenvector" and "eigenvalue" actually mean in practice.
# ---------------------------------------------------
v1 = Q[:, 0]          # the FIRST column of Q -> the first eigenvector
lambda1 = eigenvalues[0]

left_side = A @ v1            # A applied to the eigenvector
right_side = lambda1 * v1     # the eigenvector, simply scaled by lambda1

print("\nA @ v1:       ", left_side)
print("lambda1 * v1: ", right_side)
print("Equal (within floating-point rounding)?", np.allclose(left_side, right_side))
# Output: True -- confirming A @ v1 really does equal lambda1 * v1,
# exactly as the definition A*v = lambda*v promised.


# ---------------------------------------------------
# Step 4 - Build the diagonal matrix Lambda from the eigenvalues.
# np.diag() turns the flat list of eigenvalues into the diagonal
# matrix described in Step 3 of the theory above.
# ---------------------------------------------------
Lambda = np.diag(eigenvalues)
print("\nDiagonal matrix Lambda:\n", Lambda)


# ---------------------------------------------------
# Step 5 - Reconstruct A from Q, Lambda, and the inverse of Q,
# to verify the key equation: A = Q @ Lambda @ Q_inverse
# ---------------------------------------------------
Q_inverse = np.linalg.inv(Q)
A_reconstructed = Q @ Lambda @ Q_inverse

print("\nOriginal A:\n", A)
print("\nReconstructed A = Q @ Lambda @ Q_inverse:\n", A_reconstructed)
print("\nMatches original A (within floating-point rounding)?",
      np.allclose(A, A_reconstructed))
# Output: True -- the decomposition, multiplied back together,
# genuinely reproduces the original matrix.
```

**Expected output (values may show tiny floating-point differences, e.g.
`1.9999999999999998` instead of exactly `2`):**

```
Matrix A:
 [[2 1]
 [1 2]]

Eigenvalues (lambda1, lambda2): [3. 1.]

Eigenvector matrix Q (columns are eigenvectors):
 [[ 0.70710678 -0.70710678]
 [ 0.70710678  0.70710678]]

A @ v1:        [2.12132034 2.12132034]
lambda1 * v1:  [2.12132034 2.12132034]
Equal (within floating-point rounding)? True

Diagonal matrix Lambda:
 [[3. 0.]
 [0. 1.]]

Original A:
 [[2 1]
 [1 2]]

Reconstructed A = Q @ Lambda @ Q_inverse:
 [[2. 1.]
 [1. 2.]]

Matches original A (within floating-point rounding)? True
```

**Beginner tip:** always compare floating-point results with
`np.allclose()` rather than `==`. Because of how computers store decimal
numbers internally, a value that is *mathematically* exactly `2` might
actually be stored as `1.9999999999999998` after a chain of
multiplications and inversions — `np.allclose()` checks for equality
*within a small, sensible tolerance*, rather than demanding bit-for-bit
exactness.

---

## Summary

| Concept | Key takeaway |
| --- | --- |
| $A\vec{v} = \lambda\vec{v}$ | An eigenvector's *direction* is unchanged by $A$; only its length changes, by a factor of $\lambda$ |
| $Q$ | A matrix whose columns are the eigenvectors of $A$ |
| $\Lambda$ | A diagonal matrix holding all of $A$'s eigenvalues |
| $A = Q\Lambda Q^{-1}$ | The full decomposition: rotate into eigenvector space, scale, rotate back |
| `np.linalg.eig(A)` | NumPy's direct tool for computing eigenvalues and eigenvectors, without solving by hand |
| Why it matters | Foundational to PCA, closely related to SVD, and simplifies many repeated-transformation problems |

---

## Follow-up questions for practice

*(These are additional, optional questions for self-testing.)*

1. Using the script above, verify $A\vec{v} = \lambda\vec{v}$ for the
   **second** eigenvector (`Q[:, 1]` and `eigenvalues[1]`) instead of the
   first. Does `np.allclose()` still confirm a match?
2. What eigenvalues would you expect for a pure scaling matrix like
   `np.array([[4, 0], [0, 4]])`? Run `np.linalg.eig()` on it and check
   your prediction — does this match the "Cases of Eigenvalues" table
   above?
3. Try running `np.linalg.eig()` on a matrix that represents a 90-degree
   rotation, `np.array([[0, -1], [1, 0]])`. What do you notice about the
   eigenvalues? (Hint: a pure rotation has no real direction that stays
   unchanged — see if the result gives you a clue why.)
4. Using `np.diag()` and the reconstructed-matrix approach from Step 5,
   what would happen if you deliberately used the *wrong* order of columns
   in `Q` (e.g. swapped `Q[:, 0]` and `Q[:, 1]`) without also swapping the
   matching eigenvalues in `Lambda`? Would the reconstruction still work?
   Why or why not?






