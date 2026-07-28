# Eigen Decomposition: A Detailed Guide

> *Note:* The topic of eigen decomposition may appear mathematical. However, it is essential for understanding advanced topics like Singular Value Decomposition (SVD). If you are not interested in SVD, you may skip this section.

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
- Only the **magnitude changes** by a factor of $\lambda$.

---

### Cases of Eigenvalues

| Condition | Meaning |
|---|---|
| $\lambda = 1$ | Vector remains unchanged |
| $\lambda > 1$ | Vector is stretched |
| $0 < \lambda < 1$ | Vector is compressed |
| $\lambda < 0$ | Direction is reversed |

---

## 2. The Logic Behind Decomposition

Why do we decompose a matrix?

The logic is similar to how a machine works by taking it apart into its components.
It is just like breaking a machine into parts to understand it.

---

### Step 1: Eigenvalues and Eigenvectors

For a matrix $A$ of dimensions $n \times n$:

- Suppose the Eigenvalues are:  
  $$\lambda_1, \lambda_2, \dots, \lambda_n$$

- And the corresponding Eigenvectors are:  
  $$\vec{v_1}, \vec{v_2}, \dots, \vec{v_n}$$

---

### Step 2: Construct Matrix $Q$

We can arrange the eigenvectors as columns into a matrix $Q$:

$$Q = [\vec{v_1} \quad \vec{v_2} \quad \dots \quad \vec{v_n}]$$

**Columns are eigenvectors**

---

### Step 3: Construct Diagonal Matrix $\Lambda$

Next, we arrange the eigenvalues into a diagonal matrix $\Lambda$:

$$\Lambda = \begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{bmatrix}$$

---

### Step 4: Key Equation

Using the definition $A\vec{v} = \lambda \vec{v}$, we write a combined matrix equation for all eigenvalues simultaneously:

$$AQ = Q\Lambda$$

If $Q$ is invertible:

$$A = Q \Lambda Q^{-1}$$

---

### Interpretation

Eigen Decomposition represents:

```text
A = Rotation → Scaling → Rotation back
