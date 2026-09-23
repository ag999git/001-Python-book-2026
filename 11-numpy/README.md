# Chapter 11: NumPy

The online companion to Chapter 11 of the book. NumPy is the foundation of numerical work in Python: arrays, vectorized arithmetic and linear algebra. Almost everything in data science and machine learning is built on it. The printed chapter introduces the array and its operations. These pages carry thirty-nine conceptual questions, forty script exercises, and a series of projects that take the ideas as far as eigenvalues, singular value decomposition and image compression.

By the end of these pages you should know why an array is faster than a list and be able to say what "vectorized" means, understand broadcasting well enough to predict what two differently shaped arrays will do, work confidently with three-dimensional arrays and the axis argument, and read the linear algebra that machine learning rests on.

You need Chapter 18 (Lists) first. The plotting projects also use Matplotlib, from Chapter 15.

## Foundations

| Page | What it covers | Best for |
| --- | --- | --- |
| [Python Lists versus NumPy Arrays](010-ch11-numpy-list.md) | What an array gives you that a list does not, and what it costs | Start here |
| [Creating NumPy Arrays: A Complete Reference](020-arrays.md) | Every way to make an array, in one place | Reference |
| [The shape Attribute](030-shape-attribute.md) | What `shape` tells you, why `(3,)` and `(3, 1)` differ, and `reshape()` | Before broadcasting |
| [Row Vectors versus Column Vectors](040-row-column-vector.md) | A shape of `(3,)` is not the same as `(3, 1)`, and why that matters | Early, and again later |
| [3D Arrays and Axis Operations](045-ch11-3d-array-axis-ops.md) | What `axis=0` actually means, shown in three dimensions | When `axis` starts to confuse you |
| [Broadcasting](050-ch11-broadcasting.md) | The rules that let arrays of different shapes work together | The most important page here |
| [Broadcasting in AI](055-ch11-broadcasting-in-ai.md) | Where broadcasting turns up in real machine-learning code | After broadcasting |
| [The Golden Rules of Vectorization](060-golden-rules-vectorization.md) | How to replace a loop with an array operation, and when not to | After broadcasting |
| [Modern Random Number Generation](053-ch11-random-default-rng.md) | `default_rng()`, the current way to make random numbers, and why the old `np.random` calls are discouraged | Before any simulation |

## Joining and Reshaping

| Page | What it covers |
| --- | --- |
| [hstack(), vstack() and concatenate()](065-1d-array.md) | Three ways to join arrays, and how they differ |
| [Combining Arrays into a New Dimension with np.stack()](070-ch11-np-stack.md) | When you want a new axis rather than a longer one |
| [Case Study: A Photo Archive as a Tensor](080-photo-collection-tensor.md) | A real reason to hold four-dimensional data |

## Linear Algebra

| Page | What it covers |
| --- | --- |
| [Matrix-Vector Mathematics](095-ch11-matrix-vector-math.md) | Matrices as transformations rather than as grids of numbers |
| [Matrix-Vector Multiplication as Transformations](100-ch1-matrix-vector-multiply.md) | The same idea worked through as a project |
| [Eigen Decomposition](110-ch11-eigen.md) | Eigenvalues and eigenvectors, explained and computed |
| [Singular Value Decomposition](120-ch11-svd.md) | SVD, what the three pieces mean, and what it is for |
| [Beyond the Text: SVD Image Compression](150-ch11-svd-image-compress.md) | Compressing a photograph with SVD, and finding the point where it stops being recognisable |
| [Visualizing Surfaces with NumPy and Matplotlib](090-ch11-3dplots.md) | Drawing a surface from a grid of values |

## Questions

| Page | What it covers |
| --- | --- |
| [Conceptual Questions with Answers](130-ch11-conceptual-qa.md) | Thirty-nine questions, from memory layout to views and copies |
| [Forty Script-Based Exercises](140-ch11-script-qa.md) | Forty programs to write, each with a worked answer |

## Suggested Reading Order

1. **Lists versus Arrays**, then **Creating Arrays** as a reference.
2. **The shape Attribute**, then **Row versus Column Vectors** and **3D Arrays and Axis Operations**. Shape is the thing beginners get wrong, and all three pages are about shape.
3. **Broadcasting**, carefully, then **Broadcasting in AI** and **Vectorization**. This trio is the heart of the chapter.
4. **The joining pages** when you need them.
5. **The linear algebra pages in order**: matrix-vector, then eigen decomposition, then SVD, then the image compression project, which uses everything before it.
6. **The two question pages** throughout, for revision and practice.

## Three Points Worth Extra Care

**A slice of an array is a view, not a copy.** Change the slice and you change the original. This is the opposite of what a list does, and question 5 on the conceptual page calls it a common source of bugs for good reason. Use `.copy()` when you mean a copy.

**Shape `(3,)` is not shape `(3, 1)`.** One is a flat array of three numbers; the other is a column. Broadcasting treats them differently, and most "why did I get a 3 by 3 matrix?" surprises start here.

**Use `default_rng()` for random numbers.** The older `np.random.seed()` and `np.random.rand()` still work, but they share one global state, which makes results hard to reproduce. The random-numbers page shows the modern form.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell.

NumPy does not come with Python. Install it once with `pip install numpy`. The plotting and image pages also need Matplotlib, and the image compression project needs a photograph of your own — any JPEG will do.

Scripts that use random numbers will give different values on your machine unless the page sets a seed. Timing comparisons depend on your hardware; only the size of the difference is meant to match.
